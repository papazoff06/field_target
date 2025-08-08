from django.db import models


class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name
