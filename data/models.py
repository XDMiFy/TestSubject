from django.db import models
from django.db.models.fields import CharField

class Enemy(models.Model):
    name = CharField(max_length=100)
    damage = models.IntegerField()
    HP = models.IntegerField()
    Speed = models.IntegerField()
    avatar = models.ImageField(blank=True)