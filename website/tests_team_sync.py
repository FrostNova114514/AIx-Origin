from django.test import TestCase

from .models import Contract, Team


class TeamSyncTests(TestCase):
    def test_team_created_and_member_linked_on_save(self):
        contract = Contract.objects.create(
            name='Test User',
            phone='12345678901',
            email='test@example.com',
            background='bg',
            participation_city='深圳（Anchor+Weave）',
            github_homepage='https://example.com',
            post_event_followup='是',
            team_method='自行组队（请补充队友姓名/联系方式）',
            team_name='Alpha Team',
        )

        team = Team.objects.get(name='Alpha Team')
        self.assertEqual(team.members.count(), 1)
        self.assertEqual(team.members.first(), contract)

    def test_existing_team_is_reused(self):
        team = Team.objects.create(name='Beta Team')
        contract = Contract.objects.create(
            name='Test User 2',
            phone='12345678902',
            email='test2@example.com',
            background='bg',
            participation_city='深圳（Anchor+Weave）',
            github_homepage='https://example.com',
            post_event_followup='是',
            team_method='自行组队（请补充队友姓名/联系方式）',
            team_name='Beta Team',
        )

        self.assertEqual(Team.objects.filter(name='Beta Team').count(), 1)
        team.refresh_from_db()
        self.assertIn(contract, team.members.all())

    def test_team_membership_moves_to_new_named_team(self):
        first = Team.objects.create(name='Old Team')
        second = Team.objects.create(name='New Team')
        contract = Contract.objects.create(
            name='Test User 3',
            phone='12345678903',
            email='test3@example.com',
            background='bg',
            participation_city='深圳（Anchor+Weave）',
            github_homepage='https://example.com',
            post_event_followup='是',
            team_method='自行组队（请补充队友姓名/联系方式）',
            team_name='Old Team',
        )

        contract.team_name = 'New Team'
        contract.save()

        first.refresh_from_db()
        second.refresh_from_db()
        self.assertNotIn(contract, first.members.all())
        self.assertIn(contract, second.members.all())
