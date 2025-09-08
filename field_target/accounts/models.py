from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class UserProfile(models.Model):
    CHOICES = (
        ('PCP', 'PCP'),
        ('SPRINGER', 'SPRINGER'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shooter_class = models.CharField(max_length=20, choices=CHOICES)
    rifle = models.CharField(max_length=100)
    scope = models.CharField(max_length=100)
    pellets = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


    def __str__(self):
        return self.user.username
