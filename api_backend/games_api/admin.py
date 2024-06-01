from django.contrib import admin
from games_api.models import Game,GameDeveloper,GameStore

# Register your models here.

admin.site.register(Game)
admin.site.register(GameDeveloper)
admin.site.register(GameStore)