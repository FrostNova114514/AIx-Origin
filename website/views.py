from django.conf import settings
from django.http import FileResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import traceback

from .models import Contract


def home(request):
    index_path = settings.BASE_DIR / 'frontend' / 'dist' / 'index.html'
    if not index_path.exists():
        raise Http404('Vue frontend has not been built yet.')
    return FileResponse(index_path.open('rb'), content_type='text/html')


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
        contract = Contract.objects.create(
            name=value('name'),
            phone=value('phone'),
            email=value('email'),
            identity=values('identity') or values('role'),
            background=value('background'),
            team_method=value('team_method'),
            team_name=value('team_name'),
            participation_city=participation_city,
            track_shenzhen=track_shenzhen,
            track_hong_kong=track_hong_kong,
            complete_project=value('complete_project'),
            github_homepage=github_homepage,
            portfolio_resume=portfolio_resume,
            project_description=value('project_description'),
            post_event_followup=value('post_event_followup'),
            skill_programming=rating('skill_programming'),
            skill_hardware=rating('skill_hardware'),
            skill_research=rating('skill_research'),
            skill_design=rating('skill_design'),
            skill_collaboration=rating('skill_collaboration'),
            skill_other=value('skill_other'),
            hardware_skills=hardware_skills,
            software_ai_skills=software_ai_skills,
            social_links=value('social_links'),
            past_18_months=value('past_18_months'),
            public_contact=value('public_contact'),
        )
    except ValueError as exc:
        return JsonResponse({'ok': False, 'error': str(exc)}, status=400)
    except Exception as exc:
        traceback.print_exc()
        return JsonResponse({'ok': False, 'error': f'提交失败：{exc}'}, status=500)

    return JsonResponse({'ok': True, 'id': contract.id})
