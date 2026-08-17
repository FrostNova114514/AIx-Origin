from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def render_email_subject(contract, approved=True):
    if approved:
        return f'AIxOrigin 申请结果通知 - {contract.name}'
    return f'AIxOrigin 申请更新通知 - {contract.name}'


def render_email(contract, approved=True):
    subject = render_email_subject(contract, approved=approved)
    context = {
        'contract': contract,
        'subject': subject,
        'approved': approved,
        'logo_url': getattr(
            settings,
            'EMAIL_LOGO_URL',
            'https://aixorigin.innoai.org.cn/static/images/aix-origin-logo-smooth.png',
        ),
        'site_url': getattr(settings, 'SITE_URL', 'https://aixorigin.innoai.org.cn'),
    }
    html = render_to_string('emails/approval.html', context)
    text = strip_tags(html)
    return subject, html, text


def send_approval_email(contract, approved=True):
    subject, html, text = render_email(contract, approved=approved)
    message = EmailMultiAlternatives(
        subject=subject,
        body=text,
        from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', None),
        to=[contract.email],
    )
    message.attach_alternative(html, 'text/html')
    return message.send(fail_silently=False)
