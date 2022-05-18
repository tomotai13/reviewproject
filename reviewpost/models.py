from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ScoreModel(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True, default=0)
