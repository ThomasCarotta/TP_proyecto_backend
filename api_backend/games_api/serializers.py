from rest_framework import serializers
from games_api.models import Game,GameDeveloper,GameStore

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDeveloper
        fields = '__all__'

class GameStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameStore
        fields = '__all__'
