from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    members = models.ManyToManyField(User)