from django import forms

DECK_LIMIT_RANGE = ((10, 10),(15, 15),(20, 20),(25, 25),(30, 30),(35, 35),(40, 40))
HAND_LIMIT_RANGE = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10))
DECK_TYPE = ((1, "Attaque"), (2, "Defense"), (3, "Hybride"))
CARD_PER_TURN = ((1, 1), (2, 2), (3, 3))
CARD_PER_DRAW = ((1, 1), (2, 2))
TYPE_KICKOFF = ((1, "SHI FU MI"), (2, "Lancer de pièce"))


class FormCreateCustomGame(forms.form):
    turnTimer = forms.IntegerField(label="Temps de décision avant la fin du tour:", max_length = 3)
    turnCount = forms.IntegerField(label="Nombre de tours avant la fin de la partie:", max_length = 3)
    deckLimit = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=DECK_LIMIT_RANGE,
    )
    handLimit = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=HAND_LIMIT_RANGE,
    )
    typeDeck = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=DECK_TYPE,
    )
    cardsPerTurn = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CARD_PER_TURN,
    )
    cardsPerDraw = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CARD_PER_DRAW,
    )
    typeKickOff = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TYPE_KICKOFF,
    )