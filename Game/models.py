from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Game(models.Model):
    Name = models.CharField(max_length=264)
    Size = models.IntegerField()
    Developer = models.CharField(max_length=256)
    Description = models.CharField(max_length=1024)
    cover_image = models.CharField(max_length=256)
    price = models.IntegerField()
    Popular = models.BooleanField(default=False)


'''class users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games = models.ForeignObject(Game, on_delete=models.DO_NOTHING, from_fields=Game.Name,)'''
