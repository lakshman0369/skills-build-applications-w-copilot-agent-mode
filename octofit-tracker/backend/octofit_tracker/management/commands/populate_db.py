from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', age=16)
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=17)

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1.id, user2.id])

        # Create test activities
        Activity.objects.create(user=user1, type='Running', duration=30, date='2025-04-23')
        Activity.objects.create(user=user2, type='Cycling', duration=45, date='2025-04-22')

        # Create test leaderboard
        Leaderboard.objects.create(team=team1, points=100)

        # Create test workouts
        Workout.objects.create(name='Push-ups', description='Do 20 push-ups')
        Workout.objects.create(name='Sit-ups', description='Do 30 sit-ups')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
