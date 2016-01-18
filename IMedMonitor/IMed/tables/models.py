from __future__ import unicode_literals

from django.db import models

data = [
    {"name": "Me!"},
    {"name": "Myself!"},
]

# Create your models here.
class Person(models.Model):
    name = models.CharField(verbose_name="full name", max_length = 20)

table = Person(data)