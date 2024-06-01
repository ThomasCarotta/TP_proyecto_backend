from django.urls import path
from games_api import views


urlpatterns = [
    path('games_info/', views.indexGames, name='games_info'),
    # path('gamestore_info/', views.indexGameStore, name='index_game_store'),
    # path('gamedev_info/', views.indexGameDev, name='index_game_developer'),
    path('games_rest/', views.games_rest, name='games_rest'),
    path('game_dev_rest/', views.game_developer_rest, name='game_dev_rest'),
    path('game_store_rest/', views.game_store_rest, name='games_store_rest'),
    # path('add_games/', views.add_games_view, name='add_games'),
    # path('add_game_store/', views.add_game_store_view, name='add_games'),
    # path('add_game_dev/', views.add_game_developer_view, name='add_games'),
    path('new_game_dev/', views.NewGameDevView.as_view(), name='new_game_dev'),
    path('new_game_store/', views.NewGameStoreView.as_view(), name='new_game_store'),
    path('new_game/', views.NewGameView.as_view(), name='new_game'),
    
]