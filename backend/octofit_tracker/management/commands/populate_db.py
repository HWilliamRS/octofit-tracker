from django.core.management.base import BaseCommand
from core.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate octofit_db with test data'

    def handle(self, *args, **kwargs):
        # Create users
        user1 = User.objects.create(username='alice', email='alice@example.com')
        user2 = User.objects.create(username='bob', email='bob@example.com')
        # Create teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)
        # Create activities
        Activity.objects.create(user=user1, type='Running', duration=30, date=date.today())
        Activity.objects.create(user=user2, type='Cycling', duration=45, date=date.today())
        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='A quick morning cardio routine.')
        # Create leaderboard
        Leaderboard.objects.create(team=team1, score=100)
        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
