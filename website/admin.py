import io
import zipfile
from datetime import datetime
from xml.sax.saxutils import escape

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.utils import timezone
from django.utils.html import format_html, format_html_join

from .models import Contract
from .questionnaire_fields import QUESTIONNAIRE_FIELD_ORDER


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    change_list_template = 'admin/website/contract/change_list.html'
    actions = ('export_selected_as_xlsx',)
    list_display = (
        'questionnaire_number',
        'submitter',
        'submitted_at',
        'name',
        'remember_preview',
        'portfolio_resume_link',
        'social_links_preview',
        'past_18_months_preview',
        'complete_project',
        'email',
        'participation_city',
        'track_hong_kong',
        'track_shenzhen',
        'phone',
        'project_preview',
        'team_method',
        'team_method_extra_preview',
        'team_name',
        'github_homepage_link',
        'background_preview',
        'skill_other',
        'skill_collaboration',
        'skill_programming',
        'skill_hardware',
        'skill_research',
        'skill_design',
        'hardware_skills_display',
        'hardware_other',
        'software_ai_skills_display',
        'software_other',
        'post_event_followup',
        'post_event_followup_other',
        'public_contact',
        'identity_display',
        'identity_other',
        'feishu_summary',
        'is_approved',
        'approval_email_sent',
    )
    search_fields = (
        'name',
        'phone',
        'email',
        'background',
        'team_name',
        'feishu_record_id',
        'github_homepage',
        'project_description',
        'past_18_months',
        'feishu_summary',
    )
    list_filter = (
        'participation_city',
        'team_method',
        'complete_project',
        'post_event_followup',
        'public_contact',
        'is_approved',
        'approval_email_sent',
        'created_at',
    )
    readonly_fields = (
        'feishu_record_id',
        'feishu_raw_record',
        'feishu_fields_display',
        'portfolio_resume_link',
        'created_at',
        'updated_at',
    )
    ordering = ('-created_at',)
    list_per_page = 20

    fieldsets = (
        ('问卷信息', {
            'fields': (
                'submitter',
                'created_at',
                'name',
                'remember',
                'portfolio_resume',
                'portfolio_resume_link',
                'social_links',
                'past_18_months',
                'complete_project',
                'email',
                'participation_city',
                'track_hong_kong',
                'track_shenzhen',
                'phone',
                'project_description',
                'team_method',
                'team_method_extra',
                'team_name',
                'github_homepage',
                'background',
                'skill_programming',
                'skill_hardware',
                'skill_research',
                'skill_design',
                'skill_collaboration',
                'skill_other',
                'hardware_skills',
                'hardware_other',
                'software_ai_skills',
                'software_other',
                'post_event_followup',
                'post_event_followup_other',
                'public_contact',
                'identity',
                'identity_other',
                'feishu_summary',
                'is_approved',
                'approval_email_sent',
            )
        }),
        ('系统信息', {
            'fields': (
                'feishu_record_id',
                'feishu_raw_record',
                'updated_at',
            )
        }),
        ('飞书完整问卷内容', {
            'fields': (
                'feishu_fields_display',
            )
        }),
    )

    questionnaire_field_order = QUESTIONNAIRE_FIELD_ORDER

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'export-form/',
                self.admin_site.admin_view(self.export_form),
                name='website_contract_export_form',
            ),
        ]
        return custom_urls + urls

    def export_form(self, request):
        rows = [QUESTIONNAIRE_FIELD_ORDER]
        for index, contract in enumerate(self.get_queryset(request).order_by('created_at', 'id'), start=1):
            rows.append(self.contract_to_export_row(contract, index))

        content = build_xlsx(rows, sheet_name='问卷')
        filename = f'contact-form-export-{timezone.localtime().strftime("%Y%m%d-%H%M%S")}.xlsx'
        response = HttpResponse(
            content,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = f"attachment; filename*=UTF-8''{filename}"
        return response

    @admin.action(description='导出选中的表单为 Excel')
    def export_selected_as_xlsx(self, request, queryset):
        rows = [QUESTIONNAIRE_FIELD_ORDER]
        for index, contract in enumerate(queryset.order_by('created_at', 'id'), start=1):
            rows.append(self.contract_to_export_row(contract, index))

        content = build_xlsx(rows, sheet_name='问卷')
        filename = f'contact-form-selected-{timezone.localtime().strftime("%Y%m%d-%H%M%S")}.xlsx'
        response = HttpResponse(
            content,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = f"attachment; filename*=UTF-8''{filename}"
        return response

    def contract_to_export_row(self, obj, index):
        fields = (obj.feishu_raw_record or {}).get('fields') or {}

        def field(label, fallback=''):
            value = fields.get(label, fallback)
            return self.export_value(value)

        return [
            field('编号', obj.feishu_record_id or index),
            field('提交人', obj.submitter),
            field('提交时间', timezone.localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S') if obj.created_at else ''),
            field('姓名', obj.name),
            field('你还记得吗', obj.remember),
            field('你的作品集，简历', obj.portfolio_resume.name if obj.portfolio_resume else ''),
            field('请在这里粘贴你最活跃的社交媒体链接（如有，可以写1-3个）', obj.social_links),
            field('在过去18个月内，你做过哪些有趣的事？请尽可能详尽地描述。', obj.past_18_months),
            field('是否参与过完整的创业项目或开发项目', obj.complete_project),
            field('电子邮箱', obj.email),
            field('参加方式', obj.participation_city),
            field('参与赛道（香港）', obj.track_hong_kong),
            field('参与赛道（深圳）', obj.track_shenzhen),
            field('手机号', obj.phone),
            field('项目简述', obj.project_description),
            field('请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）', obj.team_method),
            field('请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）-自行组队（请补充队友姓名/联系方式）-补充内容', obj.team_method_extra),
            field('若自行组队，请输入队名', obj.team_name),
            field('你的GitHub/个人主页', obj.github_homepage),
            field('学校背景/工作背景', obj.background),
            field('技能评价', ''),
            field('技能评价-其他-Text', obj.skill_other),
            field('技能评价-项目协作（进度把控、跨学科沟通、文档整理）-Text', obj.skill_collaboration),
            field('技能评价-编程能力（如 C/C++/Python/Java 等）-Text', obj.skill_programming),
            field('技能评价-硬件开发（如 PCB设计、电路调试、嵌入式系统）-Text', obj.skill_hardware),
            field('技能评价-产品/用户研究（需求挖掘、洞察）-Text', obj.skill_research),
            field('技能评价-设计表达（UI/UX、3D建模、视觉传达）-Text', obj.skill_design),
            field('你的“硬”实力 (Hardware Skills)', obj.hardware_skills),
            field('你的“硬”实力 (Hardware Skills)-其他-Text', obj.hardware_other),
            field('你的“软”实力 (Software & AI)', obj.software_ai_skills),
            field('你的“软”实力 (Software & AI)-其他-Text', obj.software_other),
            field('你是否愿意在赛后将你的优秀项目进一步推进落地？', obj.post_event_followup),
            field('你是否愿意在赛后将你的优秀项目进一步推进落地？-其他-Text', obj.post_event_followup_other),
            field('是否愿意信息公开联系方式给合作方公司用于招聘/投资对接', obj.public_contact),
            field('你的身份 2', obj.identity),
            field('你的身份-其他-Text', obj.identity_other),
            field('总结', obj.feishu_summary),
            '是' if obj.is_approved else '否',
            '是' if obj.approval_email_sent else '否',
        ]

    def export_value(self, value):
        if value in (None, '', [], {}):
            return ''
        if isinstance(value, list):
            return '、'.join(str(item) for item in value if item)
        if isinstance(value, dict):
            return str(value)
        if isinstance(value, datetime):
            if timezone.is_aware(value):
                value = timezone.localtime(value)
            return value.strftime('%Y-%m-%d %H:%M:%S')
        return str(value)

    @admin.display(description='编号')
    def questionnaire_number(self, obj):
        return obj.feishu_record_id or obj.id

    @admin.display(description='提交时间')
    def submitted_at(self, obj):
        return obj.created_at

    @admin.display(description='你还记得吗')
    def remember_preview(self, obj):
        return self.truncate(obj.remember, 32)

    @admin.display(description='参与赛道')
    def selected_track(self, obj):
        return obj.track_shenzhen or obj.track_hong_kong or '-'

    @admin.display(description='你的身份')
    def identity_display(self, obj):
        return self.join_values(obj.identity)

    @admin.display(description='学校背景/工作背景')
    def background_preview(self, obj):
        return self.truncate(obj.background, 42)

    @admin.display(description='你的GitHub/个人主页')
    def github_homepage_link(self, obj):
        if not obj.github_homepage:
            return '-'
        return format_html(
            '<a href="{}" target="_blank" rel="noopener">{}</a>',
            obj.github_homepage,
            self.truncate(obj.github_homepage, 28),
        )

    @admin.display(description='作品集/简历')
    def portfolio_resume_link(self, obj):
        if not obj.portfolio_resume:
            return '-'
        return format_html(
            '<a href="{}" target="_blank" rel="noopener">查看/下载：{}</a>',
            obj.portfolio_resume.url,
            obj.portfolio_resume.name.rsplit('/', 1)[-1],
        )

    @admin.display(description='项目简述')
    def project_preview(self, obj):
        return self.truncate(obj.project_description, 36)

    @admin.display(description='请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）-自行组队（请补充队友姓名/联系方式）-补充内容')
    def team_method_extra_preview(self, obj):
        return self.truncate(obj.team_method_extra, 42)

    @admin.display(description='技能评价')
    def skills_preview(self, obj):
        parts = []
        ratings = [
            ('编程', obj.skill_programming),
            ('硬件', obj.skill_hardware),
            ('研究', obj.skill_research),
            ('设计', obj.skill_design),
            ('协作', obj.skill_collaboration),
        ]
        parts.extend(f'{label}:{score}' for label, score in ratings if score)
        if obj.hardware_skills:
            parts.append('硬实力:' + '、'.join(obj.hardware_skills[:2]))
        if obj.software_ai_skills:
            parts.append('软实力:' + '、'.join(obj.software_ai_skills[:2]))
        return self.truncate(' | '.join(parts), 70)

    @admin.display(description='你的“硬”实力 (Hardware Skills)')
    def hardware_skills_display(self, obj):
        return self.truncate(self.join_values(obj.hardware_skills), 48)

    @admin.display(description='你的“软”实力 (Software & AI)')
    def software_ai_skills_display(self, obj):
        return self.truncate(self.join_values(obj.software_ai_skills), 48)

    @admin.display(description='请在这里粘贴你最活跃的社交媒体链接（如有，可以写1-3个）')
    def social_links_preview(self, obj):
        return self.truncate(obj.social_links, 42)

    @admin.display(description='在过去18个月内，你做过哪些有趣的事？请尽可能详尽地描述。')
    def past_18_months_preview(self, obj):
        return self.truncate(obj.past_18_months, 42)

    @admin.display(description='飞书完整问卷内容')
    def feishu_fields_display(self, obj):
        fields = (obj.feishu_raw_record or {}).get('fields') or {}
        if not fields:
            return '-'

        rows = []
        for question, answer in fields.items():
            if answer in (None, '', [], {}):
                answer = '空'
            elif isinstance(answer, list):
                answer = '、'.join(str(item) for item in answer)
            elif isinstance(answer, dict):
                answer = str(answer)
            rows.append((question, answer))

        return format_html(
            '<table style="width:100%;border-collapse:collapse;">{}</table>',
            format_html_join(
                '',
                '<tr>'
                '<th style="width:260px;text-align:left;vertical-align:top;border:1px solid #e5e7eb;padding:8px;background:#f8fafc;">{}</th>'
                '<td style="white-space:pre-wrap;border:1px solid #e5e7eb;padding:8px;">{}</td>'
                '</tr>',
                rows,
            )
        )

    def truncate(self, value, length):
        value = str(value or '').strip()
        if len(value) <= length:
            return value or '-'
        return value[:length] + '...'

    def join_values(self, value):
        if not value:
            return '-'
        if isinstance(value, list):
            return '、'.join(str(item) for item in value if item) or '-'
        return str(value)


def build_xlsx(rows, sheet_name='Sheet1'):
    shared_strings = []
    shared_index = {}

    def shared(value):
        value = '' if value is None else str(value)
        if value not in shared_index:
            shared_index[value] = len(shared_strings)
            shared_strings.append(value)
        return shared_index[value]

    def col_name(index):
        name = ''
        while index:
            index, remainder = divmod(index - 1, 26)
            name = chr(65 + remainder) + name
        return name

    sheet_rows = []
    for row_number, row in enumerate(rows, start=1):
        cells = []
        for column_number, value in enumerate(row, start=1):
            ref = f'{col_name(column_number)}{row_number}'
            cells.append(f'<c r="{ref}" t="s"><v>{shared(value)}</v></c>')
        sheet_rows.append(f'<row r="{row_number}">{"".join(cells)}</row>')

    sheet_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<sheetData>{"".join(sheet_rows)}</sheetData>'
        '</worksheet>'
    )
    shared_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        f'count="{len(shared_strings)}" uniqueCount="{len(shared_strings)}">'
        + ''.join(f'<si><t>{escape(value)}</t></si>' for value in shared_strings)
        + '</sst>'
    )
    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<sheets>'
        f'<sheet name="{escape(sheet_name)}" sheetId="1" r:id="rId1"/>'
        '</sheets>'
        '</workbook>'
    )
    workbook_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
        '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings" Target="sharedStrings.xml"/>'
        '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        '</Relationships>'
    )
    rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        '</Relationships>'
    )
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        '<Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/>'
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        '</Types>'
    )
    styles_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>'
        '<fills count="1"><fill><patternFill patternType="none"/></fill></fills>'
        '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
        '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
        '<cellXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/></cellXfs>'
        '</styleSheet>'
    )

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('[Content_Types].xml', content_types)
        archive.writestr('_rels/.rels', rels)
        archive.writestr('xl/workbook.xml', workbook_xml)
        archive.writestr('xl/_rels/workbook.xml.rels', workbook_rels)
        archive.writestr('xl/worksheets/sheet1.xml', sheet_xml)
        archive.writestr('xl/sharedStrings.xml', shared_xml)
        archive.writestr('xl/styles.xml', styles_xml)
    return buffer.getvalue()
