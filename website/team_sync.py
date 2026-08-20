from django.db.models import Max


def normalize_team_name(value):
    return str(value or '').strip()


def sync_contract_team_membership(contract):
    from .models import Team

    team_name = normalize_team_name(contract.team_name)
    if not team_name:
        return None, False

    team = Team.objects.filter(name=team_name).first()
    created = False
    if team is None:
        max_number = Team.objects.aggregate(max_number=Max('number'))['max_number'] or 0
        team = Team.objects.create(name=team_name, number=max_number + 1)
        created = True

    for other_team in contract.teams.exclude(id=team.id):
        other_team.members.remove(contract)
    team.members.add(contract)
    return team, created
