from django import forms

from games_api.models import Game,GameStore,GameDeveloper


class GamesForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = [
            'name',
            'developer',
            'store',
        ]

class GameStoreForm(forms.ModelForm):

    class Meta:
        model = GameStore
        fields = [
            'name'
        ]

class GameDeveloperForm(forms.ModelForm):

    class Meta:
        model = GameDeveloper
        fields = [
            'name'
        ]