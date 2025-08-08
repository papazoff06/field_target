from django.db import models

# Create your models here.
from django.db import models

from field_target.competitions.models import Competition


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsors/')
    website = models.URLField()
    competitions = models.ManyToManyField(Competition, blank=True)

    def __str__(self):
        return self.name
