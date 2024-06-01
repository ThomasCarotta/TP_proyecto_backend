from django.http import JsonResponse
from django.shortcuts import render
from games_api.models import Game,GameDeveloper,GameStore
from django.views.generic import CreateView
from games_api.serializers import GameSerializer,GameDeveloperSerializer,GameStoreSerializer

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

from games_api.Forms import GamesForm,GameStoreForm,GameDeveloperForm
from django.middleware.csrf import get_token

# Create your views here.

def get_all_Games():
    Games=Game.objects.all().order_by('name')
    Game_Serializer= GameSerializer(Games, many=True)
    return Game_Serializer.data

def get_all_game_developers():
    developers = GameDeveloper.objects.all().order_by('name')
    developers_serializers = GameDeveloperSerializer(developers, many=True)
    return developers_serializers.data

def get_all_game_stores():
    stores = GameStore.objects.all().order_by('name')
    stores_serializers = GameStoreSerializer(stores, many=True)
    return stores_serializers.data


def indexGames(request):
    games = Game.objects.all().order_by('name')
    developers = GameDeveloper.objects.all().order_by('name')
    stores = GameStore.objects.all().order_by('name')
    return render(request, 'indexGames.html', {'games': games, 'game_developers': developers, 'game_stores': stores})

def games_rest(request):
    Games = get_all_Games()
    return JsonResponse(Games, safe=False)

def game_developer_rest(request):
    Dev=get_all_game_developers()
    return JsonResponse(Dev, safe=False)

def game_store_rest(request):
    Store=get_all_game_stores()
    return JsonResponse(Store, safe=False)

# def add_games_view(request):
    
#     if request.method == 'POST':
#         games_form = GamesForm(request.POST)
#         if games_form.is_valid():
#             games = games_form.save()
#             return HttpResponseRedirect('/')
#     if request.method == 'GET':
#         games_form = GamesForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {games_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)

# def add_game_store_view(request):
    
#     if request.method == 'POST':
#         gamesStore_form = GameStoreForm(request.POST)
#         if gamesStore_form.is_valid():
#             gameStore = gamesStore_form.save()
#             return HttpResponseRedirect('/')
#     if request.method == 'GET':
#         gamesStore_form = GameStoreForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {gamesStore_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)
    
# def add_game_developer_view(request):
    
#     if request.method == 'POST':
#         gamesDev_form = GameDeveloperForm(request.POST)
#         if gamesDev_form.is_valid():
#             gamesDev_form = gamesDev_form.save()
#             return HttpResponseRedirect('/')
#     if request.method == 'GET':
#         gamesDev_form = GameDeveloperForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {gamesDev_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)
    
# def indexGameStore(request):
#     GameStore = get_all_game_stores()
#     return render(request, 'indexGames.html', {'GameStore': GameStore})

# def indexGameDev(request):
#     GameDev = get_all_game_developers()
#     return render(request, 'indexGames.html', {'GameDeveloper': GameDev})

# def Gamesindex(request):
#     Games = get_all_Games()
#     GameStore = get_all_game_stores()
#     GameDeveloper = get_all_game_developers()
#     return render(request, 'indexGames.html', {'games': Games, 'game_store': GameStore, 'game_developer': GameDeveloper})

class NewGameDevView(CreateView):
    form_class = GameDeveloperForm
    template_name = 'form_gameDev.html'
    success_url = '/'

class NewGameStoreView(CreateView):
    form_class = GameStoreForm
    template_name = 'form_gameStore.html'
    success_url = '/'

class NewGameView(CreateView):
    form_class = GamesForm
    template_name = 'form_game.html'
    success_url = '/'