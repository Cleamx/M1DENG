from django.urls import path
from .views import login_view, welcome_view, logout_view, signup_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('welcome/', welcome_view, name='welcome'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]