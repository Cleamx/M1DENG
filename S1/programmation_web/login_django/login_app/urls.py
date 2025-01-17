from django.urls import path
from .views import login_view, welcome_view, logout_view, signup_view, game_view, highscores, save_score  # Ajoutez game_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('welcome/', welcome_view, name='welcome'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('game/', game_view, name='game'),
    path('game/save-score/', save_score, name='save_score'),
    path('highscores/', highscores, name='highscores'),
]
