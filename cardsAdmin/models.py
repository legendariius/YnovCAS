from django.db import models
from django.contrib import admin
from user.models import User


class Card(models.Model):
    name = models.CharField(max_length=40)
    imageSource = models.CharField(max_length=255)
    text = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        abstract = True


class ActionCard(Card):
    duration = models.IntegerField()
    type = models.ForeignKey('TypeCard', on_delete=models.DO_NOTHING)
    value = models.FloatField()
    alcohol = models.ForeignKey('Alcohol', on_delete=models.DO_NOTHING)


class ActionCardDescriptors(admin.ModelAdmin):
    list_display = ['name', 'type', 'value', 'alcohol', 'price']
    list_filter = ['name', 'type', 'value', 'alcohol', 'price']
    ordering = ['name']

    fieldsets = ((
            'Card data',
            {'fields': ['name', 'text', 'imageSource', 'price']}
        ),
        (
            'Card effects',
            {'fields': ['type', 'value', 'alcohol', 'duration']}
        )
    )


class TypeCard(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CharacterCard(Card):
    weakness = models.ForeignKey('Alcohol', on_delete=models.DO_NOTHING, related_name='weakness')
    strength = models.ForeignKey('Alcohol', on_delete=models.DO_NOTHING, related_name='strength')


class CharacterCardDescriptors(admin.ModelAdmin):
    list_display = ['name', 'weakness', 'strength', 'price']
    list_filter = ['name', 'weakness', 'strength', 'price']
    ordering = ['name']

    fieldsets = ((
            'Card data',
            {'fields': ['name', 'text', 'imageSource', 'price']}
        ),
        (
            'Card effects',
            {'fields': ['weakness', 'strength']}
        )
    )


class Alcohol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Deck(models.Model):
    idUser = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    cardList = models.ManyToManyField(ActionCard)
    TypeDeck = models.ForeignKey('TypeDeck', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class TypeStart(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class TypeDeck(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class TypeEnding(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class EndDeckEffect(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Match(models.Model):
    player1 = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name='player1')
    score1 = models.IntegerField
    alcoholLevel1 = models.FloatField
    character1 = models.ForeignKey('CharacterCard', on_delete=models.DO_NOTHING, related_name='character1')
    player2 = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name='player2')
    score2 = models.IntegerField
    alcoholLevel2 = models.FloatField
    character2 = models.ForeignKey('CharacterCard', on_delete=models.DO_NOTHING, related_name='character2')
