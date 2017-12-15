from django.db import models
from cardsAdmin.models import Deck

class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    wallet = models.IntegerField(default=0)
    deckList = models.ManyToManyField(Deck, null=True)