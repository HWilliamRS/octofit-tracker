from django.core.management.base import BaseCommand
from core.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate octofit_db with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create users (superheroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com'},
            {'username': 'superman', 'email': 'superman@dc.com'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com'},
        ]

        marvel_users = [User.objects.create(username=h['username'], email=h['email'], team=marvel) for h in marvel_heroes]
        dc_users = [User.objects.create(username=h['username'], email=h['email'], team=dc) for h in dc_heroes]

        # Create activities for each user
        for user in marvel_users + dc_users:
            Activity.objects.create(user=user, type='Running', duration=30, date=date.today())
            Activity.objects.create(user=user, type='Cycling', duration=45, date=date.today())

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='A quick morning cardio routine.')
        Workout.objects.create(name='Strength Training', description='Full body strength workout.')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, score=250)
        Leaderboard.objects.create(team=dc, score=200)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully with Marvel and DC superheroes.'))
