from django.core.management.base import BaseCommand

from website.models import Contract
from website.team_sync import sync_contract_team_membership


class Command(BaseCommand):
    help = 'Sync team assignments from self-organized contracts into Team records.'

    def handle(self, *args, **options):
        created = 0
        linked = 0
        skipped = 0

        queryset = Contract.objects.exclude(team_name='')
        for contract in queryset.order_by('feishu_record_id', 'id'):
            team, was_created = sync_contract_team_membership(contract)
            if not team:
                skipped += 1
                continue
            linked += 1
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(
            f'Synced team assignments: {linked} linked, {created} teams created, {skipped} skipped.'
        ))
