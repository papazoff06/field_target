from django.db import models

from field_target.accommodation.models import Accommodation
from field_target.accounts.models import UserProfile



class Competition(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Registration(models.Model):
    shooter = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.SET_NULL, null=True, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.shooter.user.first_name} {self.shooter.user.last_name} {self.competition}'
