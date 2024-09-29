from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import SignupForm

def login_view(request):
    # Vérifie si la requête est de type POST (soumission du formulaire)
    if request.method == 'POST':
        # Récupère le nom d'utilisateur et le mot de passe du formulaire
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Vérification de l'existence de l'utilisateur dans la base de données
        try:
            user = User.objects.get(user_login=username)  # Récupère l'utilisateur par son login
            if user.user_password == password:  # Vérifie si le mot de passe est correct
                # Stocke les informations de l'utilisateur dans la session
                request.session['user_id'] = user.user_id
                request.session['user_login'] = user.user_login
                return redirect('welcome')  # Redirige vers la vue 'welcome'
            else:
                # Affiche un message d'erreur si le mot de passe est incorrect
                messages.error(request, 'Mot de passe incorrect')
        except User.DoesNotExist:
            # Affiche un message d'erreur si l'utilisateur n'est pas trouvé
            messages.error(request, 'Utilisateur non trouvé')

    # Rendre le template de connexion
    return render(request, 'login_app/login.html')


def welcome_view(request):
    # Récupère le nom d'utilisateur de la session
    user_login = request.session.get('user_login')

    if user_login:
        # Rendre le template de bienvenue avec le nom d'utilisateur
        return render(request, 'login_app/welcome.html', {'user_login': user_login})
    else:
        # Redirige vers la page de connexion si l'utilisateur n'est pas authentifié
        return redirect('login')


def logout_view(request):
    # Efface toutes les données de session (comme user_id et user_login)
    request.session.flush()
    # Redirige l'utilisateur vers la page de connexion
    return redirect('login')


def signup_view(request):
    # Vérifie si la requête est de type POST (soumission du formulaire)
    if request.method == 'POST':
        # Crée une instance du formulaire avec les données soumises
        form = SignupForm(request.POST)
        if form.is_valid():  # Vérifie si le formulaire est valide
            form.save()  # Enregistre le nouvel utilisateur dans la base de données
            # Affiche un message de succès
            messages.success(request, "Votre compte a été créé avec succès.")
            # Redirige vers la page de connexion
            return redirect('login')
    else:
        # Si la requête n'est pas POST, crée un formulaire vide
        form = SignupForm()

    # Rendre le template de création de compte avec le formulaire
    return render(request, 'login_app/signup.html', {'form': form})
