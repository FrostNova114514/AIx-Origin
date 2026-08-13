from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import traceback

from .models import Contract
from .questionnaire_fields import QUESTIONNAIRE_FIELD_ORDER


def home(request):
    index_path = settings.BASE_DIR / 'frontend' / 'dist' / 'index.html'
    if not index_path.exists():
        raise Http404('Vue frontend has not been built yet.')
    html = index_path.read_text(encoding='utf-8')
    if request.path.startswith('/'):
        html = html.replace('./assets/', '/assets/')
    return HttpResponse(html, content_type='text/html; charset=utf-8')


@csrf_exempt
@require_POST
def submit_contract(request):
    data = request.POST

    def value(name, fallback=''):
        return data.get(name, fallback).strip()

    def values(name):
        return [item.strip() for item in data.getlist(name) if item.strip()]

    def rating(name):
        raw = value(name)
        if not raw:
            return None
        try:
            score = int(raw)
        except ValueError:
            raise ValueError(f'{name} 必须是 1-4 的数字')
        if score not in (1, 2, 3, 4):
            raise ValueError(f'{name} 必须是 1-4 的数字')
        return score

    def normalize_url(raw):
        raw = raw.strip()
        if not raw:
            return ''
        if raw.startswith(('http://', 'https://')):
            return raw
        return f'https://{raw}'

    required_fields = {
        'name': '姓名',
        'phone': '手机号',
        'email': '电子邮箱',
        'background': '学校背景/工作背景',
        'participation_city': '参加方式',
        'post_event_followup': '赛后项目推进意愿',
    }

    github_homepage = normalize_url(value('github_homepage') or value('github'))

    for field, label in required_fields.items():
        if not value(field):
            return JsonResponse({'ok': False, 'error': f'请填写{label}'}, status=400)

    participation_city = value('participation_city')
    track_shenzhen = value('track_shenzhen')
    track_hong_kong = value('track_hong_kong')
    if '深圳' in participation_city and not track_shenzhen:
        return JsonResponse({'ok': False, 'error': '请选择深圳赛道'}, status=400)
    if '香港' in participation_city and not track_hong_kong:
        return JsonResponse({'ok': False, 'error': '请选择香港赛道'}, status=400)
    if '深圳' in participation_city:
        track_hong_kong = ''
    if '香港' in participation_city:
        track_shenzhen = ''

    required_ratings = (
        'skill_programming',
        'skill_hardware',
        'skill_research',
        'skill_design',
        'skill_collaboration',
    )
    for field in required_ratings:
        if not value(field):
            return JsonResponse({'ok': False, 'error': '请完成技能评价'}, status=400)

    hardware_skills = values('hardware_skills')
    software_ai_skills = values('software_ai_skills') or values('software_skills')
    if not hardware_skills:
        return JsonResponse({'ok': False, 'error': '请选择至少一项硬实力'}, status=400)
    if not software_ai_skills:
        return JsonResponse({'ok': False, 'error': '请选择至少一项软实力'}, status=400)

    portfolio_resume = request.FILES.get('portfolio_resume')
    if not portfolio_resume or not getattr(portfolio_resume, 'name', '') or not getattr(portfolio_resume, 'size', 0):
        portfolio_resume = None

    try:
        submitted_at = timezone.now()
        identity = values('identity') or values('role')
        team_method = value('team_method')
        hardware_skills = hardware_skills
        software_ai_skills = software_ai_skills
        raw_fields = {
            '编号': '',
            '提交人': '',
            '提交时间': submitted_at.isoformat(),
            '姓名': value('name'),
            '你还记得吗': value('remember'),
            '你的作品集，简历': portfolio_resume.name if portfolio_resume else '',
            '请在这里粘贴你最活跃的社交媒体链接（如有，可以写1-3个）': value('social_links'),
            '在过去18个月内，你做过哪些有趣的事？请尽可能详尽地描述。': value('past_18_months'),
            '是否参与过完整的创业项目或开发项目': value('complete_project'),
            '电子邮箱': value('email'),
            '参加方式': participation_city,
            '参与赛道（香港）': track_hong_kong,
            '参与赛道（深圳）': track_shenzhen,
            '手机号': value('phone'),
            '项目简述': value('project_description'),
            '请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）': team_method,
            '请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）-自行组队（请补充队友姓名/联系方式）-补充内容': value('team_method_extra'),
            '若自行组队，请输入队名': value('team_name'),
            '你的GitHub/个人主页': github_homepage,
            '学校背景/工作背景': value('background'),
            '技能评价': '',
            '技能评价-其他-Text': value('skill_other'),
            '技能评价-项目协作（进度把控、跨学科沟通、文档整理）-Text': value('skill_collaboration'),
            '技能评价-编程能力（如 C/C++/Python/Java 等）-Text': value('skill_programming'),
            '技能评价-硬件开发（如 PCB设计、电路调试、嵌入式系统）-Text': value('skill_hardware'),
            '技能评价-产品/用户研究（需求挖掘、洞察）-Text': value('skill_research'),
            '技能评价-设计表达（UI/UX、3D建模、视觉传达）-Text': value('skill_design'),
            '你的“硬”实力 (Hardware Skills)': hardware_skills,
            '你的“硬”实力 (Hardware Skills)-其他-Text': value('hardware_other'),
            '你的“软”实力 (Software & AI)': software_ai_skills,
            '你的“软”实力 (Software & AI)-其他-Text': value('software_other'),
            '你是否愿意在赛后将你的优秀项目进一步推进落地？': value('post_event_followup'),
            '你是否愿意在赛后将你的优秀项目进一步推进落地？-其他-Text': value('post_event_followup_other'),
            '是否愿意信息公开联系方式给合作方公司用于招聘/投资对接': value('public_contact'),
            '你的身份 2': identity,
            '你的身份-其他-Text': value('identity_other'),
            '总结': '',
            '是否通过审核': '',
            '是否发送邮件': '',
        }
        contract = Contract.objects.create(
            submitter='',
            name=value('name'),
            remember=value('remember'),
            phone=value('phone'),
            email=value('email'),
            identity=identity,
            identity_other=value('identity_other'),
            background=value('background'),
            team_method=team_method,
            team_method_extra=value('team_method_extra'),
            team_name=value('team_name'),
            participation_city=participation_city,
            track_shenzhen=track_shenzhen,
            track_hong_kong=track_hong_kong,
            complete_project=value('complete_project'),
            github_homepage=github_homepage,
            portfolio_resume=portfolio_resume,
            project_description=value('project_description'),
            post_event_followup=value('post_event_followup'),
            post_event_followup_other=value('post_event_followup_other'),
            skill_programming=rating('skill_programming'),
            skill_hardware=rating('skill_hardware'),
            skill_research=rating('skill_research'),
            skill_design=rating('skill_design'),
            skill_collaboration=rating('skill_collaboration'),
            skill_other=value('skill_other'),
            hardware_skills=hardware_skills,
            hardware_other=value('hardware_other'),
            software_ai_skills=software_ai_skills,
            software_other=value('software_other'),
            social_links=value('social_links'),
            past_18_months=value('past_18_months'),
            public_contact=value('public_contact'),
            feishu_raw_record={
                'source': 'website',
                'fields': {key: raw_fields.get(key, '') for key in QUESTIONNAIRE_FIELD_ORDER},
            },
        )
    except ValueError as exc:
        return JsonResponse({'ok': False, 'error': str(exc)}, status=400)
    except Exception as exc:
        traceback.print_exc()
        return JsonResponse({'ok': False, 'error': f'提交失败：{exc}'}, status=500)

    return JsonResponse({'ok': True, 'id': contract.id})
