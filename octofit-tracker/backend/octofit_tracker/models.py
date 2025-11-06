from django.db import models

# Example models for users, teams, activities, leaderboard, workouts

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.type}"


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    score = models.IntegerField()

    def __str__(self):
        return f"{self.team.name}: {self.score}"
