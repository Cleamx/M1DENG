from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(user_login=username)
            if user.user_password == password:
                request.session['user_id'] = user.user_id
                request.session['user_login'] = user.user_login
                return redirect('welcome')  
            else:
                messages.error(request, 'Mot de passe incorrect')
        except User.DoesNotExist:
            messages.error(request, 'Utilisateur non trouvé')

    return render(request, 'login_app/login.html')


def welcome_view(request):
    user_login = request.session.get('user_login')

    if user_login:
        return render(request, 'login_app/welcome.html', {'user_login': user_login})
    else:
        return redirect('login') 
