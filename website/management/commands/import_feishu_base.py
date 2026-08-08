import base64
import gzip
import json
import re
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from website.models import Contract


FIELD_MAP = {
    'name': 'fldwjCjowp',
    'phone': 'fld1sh3h1s',
    'email': 'fldl3k6MI3',
    'identity': 'fldVoniFBX',
    'identity_other': 'fldbrV4Av3',
    'background': 'fldSlWUzk0',
    'team_method': 'fldgIzQr2T',
    'team_method_extra': 'fldS0FoH4D',
    'team_name': 'fldhH7eKll',
    'participation_city': 'fldZuFtbkF',
    'track_shenzhen': 'fldqzAIjRF',
    'track_hong_kong': 'fldr7SSS4x',
    'complete_project': 'fldKjmXMCd',
    'github_homepage': 'fldUFGZdSE',
    'project_description': 'fldicq4OdP',
    'post_event_followup': 'fldE4cB1Q4',
    'post_event_followup_other': 'fldFQwuY0p',
    'skill_programming': 'fldw77abhO',
    'skill_hardware': 'fld9ZQRdUk',
    'skill_research': 'fldA2cjumX',
    'skill_design': 'fldTiy4Pfv',
    'skill_collaboration': 'fldk4GJBx1',
    'skill_other': 'fldwxHoB15',
    'hardware_skills': 'fldvt624HK',
    'hardware_other': 'fldNefbGWj',
    'software_ai_skills': 'fldA5IebX2',
    'software_other': 'fldUffCaDK',
    'social_links': 'fld6phvfcX',
    'past_18_months': 'fldTbf20MP',
    'public_contact': 'fldds3I5Uu',
    'feishu_summary': 'fldtX0LJRQ',
}


class Command(BaseCommand):
    help = 'Import records from a Feishu .base snapshot into the contract table.'

    def add_arguments(self, parser):
        parser.add_argument('path', help='Path to the exported .base file')

    def handle(self, *args, **options):
        path = Path(options['path']).expanduser()
        if not path.exists():
            raise CommandError(f'File not found: {path}')

        schema = self.load_schema(path)
        table = schema['data']['table']
        field_map = table['fieldMap']
        record_map = schema['data']['recordMap']
        record_meta = schema['data'].get('recordMeta', {})

        created = 0
        updated = 0

        for record_id, record in record_map.items():
            payload = self.build_payload(record_id, record, record_meta.get(record_id, {}), field_map)
            _, was_created = Contract.objects.update_or_create(
                feishu_record_id=record_id,
                defaults=payload,
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(
            f'Imported {len(record_map)} records: {created} created, {updated} updated.'
        ))

    def load_schema(self, path):
        try:
            data = json.loads(path.read_text())
            snapshot = gzip.decompress(base64.b64decode(data['gzipSnapshot'])).decode('utf-8')
            return json.loads(snapshot)[0]['schema']
        except (KeyError, IndexError, ValueError, OSError, json.JSONDecodeError) as exc:
            raise CommandError(f'Could not read Feishu base file: {exc}') from exc

    def build_payload(self, record_id, record, meta, field_map):
        def get(key):
            return self.extract_value(record.get(FIELD_MAP[key]), field_map.get(FIELD_MAP[key], {}))

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

        return {
            'name': get('name') or f'飞书记录 {record_id}',
            'phone': get('phone') or '',
            'email': get('email') or '',
            'identity': identity,
            'background': get('background') or '',
            'team_method': team_method or '',
            'team_name': get('team_name') or '',
            'participation_city': get('participation_city') or '',
            'track_shenzhen': get('track_shenzhen') or '',
            'track_hong_kong': get('track_hong_kong') or '',
            'complete_project': get('complete_project') or '',
            'github_homepage': self.as_url(get('github_homepage')),
            'project_description': get('project_description') or '',
            'post_event_followup': post_event_followup or '',
            'skill_programming': self.as_rating(get('skill_programming')),
            'skill_hardware': self.as_rating(get('skill_hardware')),
            'skill_research': self.as_rating(get('skill_research')),
            'skill_design': self.as_rating(get('skill_design')),
            'skill_collaboration': self.as_rating(get('skill_collaboration')),
            'skill_other': get('skill_other') or '',
            'hardware_skills': hardware_skills,
            'software_ai_skills': software_ai_skills,
            'social_links': get('social_links') or '',
            'past_18_months': get('past_18_months') or '',
            'public_contact': get('public_contact') or '',
            'feishu_summary': get('feishu_summary') or '',
            'feishu_raw_record': self.build_raw_record(record_id, record, meta, field_map),
        }

    def build_raw_record(self, record_id, record, meta, field_map):
        readable = {}
        for field_id, value in record.items():
            field = field_map.get(field_id, {})
            name = field.get('name') or field_id
            readable[name] = self.extract_value(value, field)
        return {
            'record_id': record_id,
            'meta': meta,
            'fields': readable,
        }

    def extract_value(self, cell, field):
        if not cell:
            return ''
        value = cell.get('value') if isinstance(cell, dict) else cell
        if value in (None, ''):
            return ''

        options = {
            option.get('id'): option.get('name')
            for option in (field.get('property') or {}).get('options') or []
        }

        if isinstance(value, list):
            if value and all(isinstance(item, str) for item in value):
                return [options.get(item, item) for item in value]
            return ''.join(
                item.get('text', '') if isinstance(item, dict) else str(item)
                for item in value
            )

        if isinstance(value, str):
            return options.get(value, value)

        if isinstance(value, (int, float)):
            if field.get('type') == 1001:
                return timezone.datetime.fromtimestamp(value, tz=timezone.get_current_timezone()).isoformat()
            return str(value)

        if isinstance(value, dict):
            if 'users' in value:
                return ', '.join(user.get('name', '') for user in value.get('users', []) if user.get('name'))
            if 'link' in value:
                return value.get('link') or ''
            return value

        return str(value)

    def as_list(self, value):
        if not value:
            return []
        if isinstance(value, list):
            return value
        return [str(value)]

    def as_rating(self, value):
        try:
            score = int(str(value).strip())
        except (TypeError, ValueError):
            return None
        return score if score in (1, 2, 3, 4) else None

    def as_url(self, value):
        value = str(value or '').strip()
        if not value:
            return ''
        match = re.search(r'https?://[^\s，,。；;）)]+', value)
        if match:
            return match.group(0)
        if value.startswith(('http://', 'https://')):
            return value
        if '.' in value and ' ' not in value:
            return f'https://{value}'
        return ''
