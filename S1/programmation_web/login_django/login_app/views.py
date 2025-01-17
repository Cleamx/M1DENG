import json
from django.http import JsonResponse
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from .models import Score, User
from .forms import SignupForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(user_login=username)
            if check_password(password, user.user_password):
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


def logout_view(request):
    request.session.flush()
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_password = make_password(
                form.cleaned_data['user_password'])
            user.save()

            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'login_app/signup.html', {'form': form})


def game_view(request):
    return render(request, 'login_app/game.html')


def highscores(request):
    scores = Score.objects.all().order_by('-score')[:10]
    return render(request, 'login_app/highscores.html', {'scores': scores})


@csrf_exempt
def save_score(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            score_value = data.get('score')
            user_login = request.session.get('user_login')

            if user_login:
                user = User.objects.get(user_login=user_login)
                Score.objects.create(user=user, score=score_value)
                return JsonResponse({'status': 'success'})
            return JsonResponse({'status': 'error', 'message': 'User not found'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
