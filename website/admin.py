from django.contrib import admin
from django.utils.html import format_html, format_html_join

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'feishu_record_id',
        'name',
        'phone',
        'email',
        'participation_city',
        'selected_track',
        'team_method',
        'portfolio_resume_link',
        'project_preview',
        'skills_preview',
        'public_contact',
        'created_at',
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
        'created_at',
    )
    readonly_fields = (
        'feishu_record_id',
        'feishu_summary',
        'feishu_raw_record',
        'feishu_fields_display',
        'portfolio_resume_link',
        'created_at',
        'updated_at',
    )
    ordering = ('-created_at',)
    list_per_page = 20

    fieldsets = (
        ('基础信息', {
            'fields': (
                'name',
                'feishu_record_id',
                'phone',
                'email',
                'identity',
                'background',
            )
        }),
        ('组队与赛道', {
            'fields': (
                'team_method',
                'team_name',
                'participation_city',
                'track_shenzhen',
                'track_hong_kong',
            )
        }),
        ('项目与作品', {
            'fields': (
                'complete_project',
                'github_homepage',
                'portfolio_resume',
                'portfolio_resume_link',
                'project_description',
                'post_event_followup',
                'social_links',
                'past_18_months',
                'public_contact',
                'feishu_summary',
                'feishu_raw_record',
            )
        }),
        ('技能评价', {
            'fields': (
                'skill_programming',
                'skill_hardware',
                'skill_research',
                'skill_design',
                'skill_collaboration',
                'skill_other',
                'hardware_skills',
                'software_ai_skills',
            )
        }),
        ('系统信息', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
        ('飞书完整问卷内容', {
            'fields': (
                'feishu_fields_display',
            )
        }),
    )

    @admin.display(description='参与赛道')
    def selected_track(self, obj):
        return obj.track_shenzhen or obj.track_hong_kong or '-'

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

    @admin.display(description='技能概览')
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
