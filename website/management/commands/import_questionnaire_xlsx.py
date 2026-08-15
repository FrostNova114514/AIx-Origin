import json
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from website.models import Contract
from website.questionnaire_fields import QUESTIONNAIRE_FIELD_ORDER


FIELD_MAP = {
    'submitter': '提交人',
    'name': '姓名',
    'remember': '你还记得吗',
    'phone': '手机号',
    'email': '电子邮箱',
    'identity': '你的身份 2',
    'identity_other': '你的身份-其他-Text',
    'background': '学校背景/工作背景',
    'team_method': '请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）',
    'team_method_extra': '请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）-自行组队（请补充队友姓名/联系方式）-补充内容',
    'team_name': '若自行组队，请输入队名',
    'participation_city': '参加方式',
    'track_shenzhen': '参与赛道（深圳）',
    'track_hong_kong': '参与赛道（香港）',
    'complete_project': '是否参与过完整的创业项目或开发项目',
    'github_homepage': '你的GitHub/个人主页',
    'project_description': '项目简述',
    'post_event_followup': '你是否愿意在赛后将你的优秀项目进一步推进落地？',
    'post_event_followup_other': '你是否愿意在赛后将你的优秀项目进一步推进落地？-其他-Text',
    'skill_programming': '技能评价-编程能力（如 C/C++/Python/Java 等）-Text',
    'skill_hardware': '技能评价-硬件开发（如 PCB设计、电路调试、嵌入式系统）-Text',
    'skill_research': '技能评价-产品/用户研究（需求挖掘、洞察）-Text',
    'skill_design': '技能评价-设计表达（UI/UX、3D建模、视觉传达）-Text',
    'skill_collaboration': '技能评价-项目协作（进度把控、跨学科沟通、文档整理）-Text',
    'skill_other': '技能评价-其他-Text',
    'hardware_skills': '你的“硬”实力 (Hardware Skills)',
    'hardware_other': '你的“硬”实力 (Hardware Skills)-其他-Text',
    'software_ai_skills': '你的“软”实力 (Software & AI)',
    'software_other': '你的“软”实力 (Software & AI)-其他-Text',
    'social_links': '请在这里粘贴你最活跃的社交媒体链接（如有，可以写1-3个）',
    'past_18_months': '在过去18个月内，你做过哪些有趣的事？请尽可能详尽地描述。',
    'public_contact': '是否愿意信息公开联系方式给合作方公司用于招聘/投资对接',
    'feishu_summary': '总结',
    'is_approved': '是否通过审核',
    'approval_email_sent': '是否发送邮件',
}


class Command(BaseCommand):
    help = 'Import questionnaire records from a Feishu-exported .xlsx file.'

    def add_arguments(self, parser):
        parser.add_argument('path', help='Path to the exported .xlsx file')

    def handle(self, *args, **options):
        path = Path(options['path']).expanduser()
        if not path.exists():
            raise CommandError(f'File not found: {path}')

        rows = self.read_xlsx(path)
        if not rows:
            raise CommandError('No rows found in workbook.')

        headers = rows[0]
        records = [self.row_to_record(headers, row) for row in rows[1:]]
        records = [record for record in records if any(record.values())]

        created = 0
        updated = 0
        skipped = 0

        for record in records:
            payload = self.build_payload(record)
            matches = self.find_matches(payload)
            if matches.count() == 1:
                obj = matches.first()
                for key, value in payload.items():
                    setattr(obj, key, value)
                obj.save()
                updated += 1
            elif matches.count() == 0:
                Contract.objects.create(**payload)
                created += 1
            else:
                skipped += 1

        self.stdout.write(self.style.SUCCESS(
            f'Imported {len(records)} records: {created} created, {updated} updated, {skipped} skipped.'
        ))

    def build_payload(self, record):
        def get(key):
            return self.clean(record.get(FIELD_MAP[key]))

        identity = self.as_list(get('identity'))
        identity_other = get('identity_other')
        if identity_other:
            identity.append(identity_other)

        team_method = get('team_method')
        team_method_extra = get('team_method_extra')
        if team_method_extra:
            team_method = f'{team_method}：{team_method_extra}' if team_method else team_method_extra

        post_event_followup = get('post_event_followup')
        post_event_followup_other = get('post_event_followup_other')
        if post_event_followup_other:
            post_event_followup = f'{post_event_followup}：{post_event_followup_other}' if post_event_followup else post_event_followup_other

        hardware_skills = self.as_list(get('hardware_skills'))
        hardware_other = get('hardware_other')
        if hardware_other:
            hardware_skills.append(hardware_other)

        software_ai_skills = self.as_list(get('software_ai_skills'))
        software_other = get('software_other')
        if software_other:
            software_ai_skills.append(software_other)

        payload = {
            'submitter': get('submitter') or '',
            'name': get('name') or '未填写姓名',
            'remember': get('remember') or '',
            'phone': get('phone') or '',
            'email': get('email') or '',
            'identity': identity,
            'identity_other': identity_other or '',
            'background': get('background') or '',
            'team_method': team_method or '',
            'team_method_extra': team_method_extra or '',
            'team_name': get('team_name') or '',
            'participation_city': get('participation_city') or '',
            'track_shenzhen': get('track_shenzhen') or '',
            'track_hong_kong': get('track_hong_kong') or '',
            'complete_project': get('complete_project') or '',
            'github_homepage': self.as_url(get('github_homepage')),
            'project_description': get('project_description') or '',
            'post_event_followup': post_event_followup or '',
            'post_event_followup_other': post_event_followup_other or '',
            'skill_programming': self.as_rating(get('skill_programming')),
            'skill_hardware': self.as_rating(get('skill_hardware')),
            'skill_research': self.as_rating(get('skill_research')),
            'skill_design': self.as_rating(get('skill_design')),
            'skill_collaboration': self.as_rating(get('skill_collaboration')),
            'skill_other': get('skill_other') or '',
            'hardware_skills': hardware_skills,
            'hardware_other': hardware_other or '',
            'software_ai_skills': software_ai_skills,
            'software_other': software_other or '',
            'social_links': get('social_links') or '',
            'past_18_months': get('past_18_months') or '',
            'public_contact': get('public_contact') or '',
            'feishu_summary': get('feishu_summary') or '',
            'is_approved': self.as_bool(get('is_approved')),
            'approval_email_sent': self.as_bool(get('approval_email_sent')),
            'feishu_raw_record': {
                'source': 'xlsx',
                'fields': self.build_fields_in_question_order(record),
            },
        }
        return payload

    def build_fields_in_question_order(self, record):
        ordered = {}
        for key in QUESTIONNAIRE_FIELD_ORDER:
            if key in record:
                ordered[key] = self.clean(record.get(key))
        for key, value in record.items():
            if key not in ordered:
                ordered[key] = self.clean(value)
        return ordered

    def find_matches(self, payload):
        email = payload.get('email')
        if email:
            return Contract.objects.filter(email=email)
        name = payload.get('name')
        phone = payload.get('phone')
        if name and phone:
            return Contract.objects.filter(name=name, phone=phone)
        return Contract.objects.none()

    def read_xlsx(self, path):
        try:
            with zipfile.ZipFile(path) as archive:
                workbook = ET.fromstring(archive.read('xl/workbook.xml'))
                relationships = ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))
                relmap = {
                    rel.attrib['Id']: self.workbook_relative_path(rel.attrib['Target'])
                    for rel in relationships
                }
                sheet = workbook.find(
                    '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheets/'
                    '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheet'
                )
                if sheet is None:
                    return []
                rel_id = sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
                sheet_path = relmap[rel_id]
                shared_strings = self.read_shared_strings(archive)
                sheet_root = ET.fromstring(archive.read(sheet_path))
        except (KeyError, OSError, ET.ParseError, zipfile.BadZipFile) as exc:
            raise CommandError(f'Could not read workbook: {exc}') from exc

        rows = []
        sheet_data = sheet_root.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheetData')
        if sheet_data is None:
            return rows

        for row in sheet_data:
            values = {}
            for cell in row:
                column_index = self.cell_column_index(cell.attrib['r'])
                values[column_index] = self.cell_value(cell, shared_strings)
            if values:
                rows.append([values.get(index) for index in range(1, max(values) + 1)])
        return rows

    def read_shared_strings(self, archive):
        if 'xl/sharedStrings.xml' not in archive.namelist():
            return []
        root = ET.fromstring(archive.read('xl/sharedStrings.xml'))
        return [
            ''.join(text.text or '' for text in item.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t'))
            for item in root
        ]

    def workbook_relative_path(self, target):
        target = target.lstrip('/')
        if target.startswith('xl/'):
            return target
        return f'xl/{target}'

    def cell_value(self, cell, shared_strings):
        cell_type = cell.attrib.get('t')
        value = cell.findtext('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
        if cell_type == 's' and value is not None:
            return shared_strings[int(value)]
        if cell_type == 'inlineStr':
            return ''.join(text.text or '' for text in cell.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t'))
        return value

    def cell_column_index(self, reference):
        column = re.match(r'([A-Z]+)', reference).group(1)
        index = 0
        for char in column:
            index = index * 26 + ord(char) - 64
        return index

    def row_to_record(self, headers, row):
        return {
            header: row[index] if index < len(row) else None
            for index, header in enumerate(headers)
            if header
        }

    def clean(self, value):
        if value is None:
            return ''
        return str(value).strip()

    def as_list(self, value):
        if not value:
            return []
        return [item.strip() for item in re.split(r'[,，]', value) if item.strip()]

    def as_rating(self, value):
        value = self.clean(value)
        match = re.search(r'[1-4]', value)
        return int(match.group(0)) if match else None

    def as_url(self, value):
        value = self.clean(value)
        if not value:
            return ''
        match = re.search(r'https?://[^\s，,。；;）)]+', value)
        if match:
            return match.group(0)
        if '.' in value and ' ' not in value:
            return f'https://{value}'
        return ''

    def as_bool(self, value):
        value = self.clean(value).lower()
        return value in {'1', 'true', 'yes', 'y', '是', '通过', '已通过', '发送', '已发送'}
