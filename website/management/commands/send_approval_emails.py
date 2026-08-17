from django.core.management.base import BaseCommand, CommandError

from website.emailing import send_approval_email
from website.models import Contract


class Command(BaseCommand):
    help = 'Send approval emails for approved contract records.'

    def add_arguments(self, parser):
        parser.add_argument('--ids', nargs='*', type=int, help='Optional contract IDs to send')
        parser.add_argument('--approved-only', action='store_true', help='Only send for approved records')
        parser.add_argument('--limit', type=int, default=0, help='Limit number of records to send')

    def handle(self, *args, **options):
        qs = Contract.objects.all().order_by('created_at', 'id')
        if options['approved_only']:
            qs = qs.filter(is_approved=True)
        if options['ids']:
            qs = qs.filter(id__in=options['ids'])

        limit = options['limit'] or 0
        if limit:
            qs = qs[:limit]

        sent = 0
        skipped = 0

        for contract in qs:
            if not contract.email:
                skipped += 1
                continue
            try:
                send_approval_email(contract, approved=contract.is_approved)
                contract.approval_email_sent = True
                contract.save(update_fields=['approval_email_sent', 'updated_at'])
                sent += 1
            except Exception as exc:
                raise CommandError(f'Failed to send email for {contract.id}: {exc}') from exc

        self.stdout.write(self.style.SUCCESS(f'Sent {sent} emails, skipped {skipped}.'))
