from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from field_target.accommodation.models import Accommodation
from field_target.accounts.models import UserProfile
from field_target.competitions.validators import validate_competition_name


class Competition(models.Model):
    name = models.CharField(
        max_length=100,
    validators=[validate_competition_name],
    )
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
    first_day_score = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        error_messages={
            'max_value': 'Score cannot be more than 50',
        },
        null=True,
        blank=True,
    )
    second_day_score = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        error_messages={
            'max_value': 'Score cannot be more than 50',
        },
        null=True,
        blank=True,
    )
    tird_day_score = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        error_messages={
            'max_value': 'Score cannot be more than 50',
        },
        null=True,
        blank=True,
    )

    @property
    def total_score(self):
        return self.first_day_score + self.second_day_score + self.tird_day_score

    def __str__(self):
        return f'{self.shooter.user.get_full_name()} {self.competition}'


