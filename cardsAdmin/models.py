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
    maxAlcohol = models.FloatField()


class CharacterCardDescriptors(admin.ModelAdmin):
    list_display = ['name', 'weakness', 'strength', 'maxAlcohol', 'price']
    list_filter = ['name', 'weakness', 'strength', 'maxAlcohol', 'price']
    ordering = ['name']

    fieldsets = ((
            'Card data',
            {'fields': ['name', 'text', 'imageSource', 'price']}
        ),
        (
            'Card effects',
            {'fields': ['weakness', 'strength', 'maxAlcohol']}
        )
    )


class Alcohol(models.Model):
    name = models.CharField(max_length=30)

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

class Deck(models.Model):
    idUser = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    cardList = models.ManyToManyField(ActionCard)
    TypeDeck = models.ForeignKey('TypeDeck', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class TypeKickOff(models.Model):
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


class Parameters(models.Model):
    deckLimit = models.IntegerField()
    handSize = models.IntegerField()
    cardsPerTurn = models.IntegerField()
    cardsPerDraw = models.IntegerField()
    turnTimer = models.IntegerField()
    alcoholLimit = models.IntegerField()
    typeStart = models.ForeignKey('TypeStart', on_delete=models.DO_NOTHING,)
    typeDeck = models.ForeignKey('TypeDeck', on_delete=models.DO_NOTHING,)
    typeKickOff = models.ForeignKey('TypeKickOff', on_delete=models.DO_NOTHING,)
    endDeckEffect = models.ForeignKey('EndDeckEffect', on_delete=models.DO_NOTHING,)
    typeEnding = models.ForeignKey('TypeEnding', on_delete=models.DO_NOTHING,)
