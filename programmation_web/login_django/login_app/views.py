from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from .models import User, Item
from .forms import SignupForm, ItemForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(user_login=username)
            # Vérifier si le mot de passe saisi correspond au mot de passe haché en base
            if check_password(password, user.user_password):
                # Si le mot de passe est correct, stocker les informations dans la session
                request.session['user_id'] = user.user_id
                request.session['user_login'] = user.user_login

                return redirect('welcome')
            else:
                messages.error(request, 'Mot de passe incorrect')
        except User.DoesNotExist:
            messages.error(request, 'Utilisateur non trouvé')

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
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Hasher le mot de passe avant de sauvegarder le nouvel utilisateur
            user = form.save(commit=False)
            user.user_password = make_password(
                form.cleaned_data['user_password'])
            user.save()

            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'login_app/signup.html', {'form': form})

# Lister les objets de l'inventaire de l'utilisateur connecté


@login_required
def inventory_list(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')

    user = User.objects.get(user_id=user_id)

    items = Item.objects.filter(user=user)

    return render(request, 'login_app/list.html', {'items': items})


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # On ne sauvegarde pas tout de suite pour associer l'utilisateur
            item = form.save(commit=False)
            item.user = request.user  # Associer l'objet à l'utilisateur connecté
            item.save()
            messages.success(request, 'Objet ajouté avec succès !')
            return redirect('list')  # Redirige vers la liste des objets
    else:
        form = ItemForm()
    return render(request, 'login_app/add_item.html', {'form': form})

# Mettre à jour la quantité d'un objet


@login_required
@login_required
def update_item(request, item_id):
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    item = get_object_or_404(Item, id=item_id, user=user)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Objet mis à jour avec succès !')
            return redirect('list')
    else:
        form = ItemForm(instance=item)

    return render(request, 'login_app/update_item.html', {'form': form})


@login_required
def delete_item(request, item_id):
    user = request.user

    # Afficher des informations pour le débogage
    print(f'Utilisateur connecté: {user}')
    print(f'ID de l\'objet à supprimer: {item_id}')

    # Récupérer l'objet à supprimer, en s'assurant qu'il appartient à l'utilisateur connecté
    item = get_object_or_404(Item, id=item_id, user=user)

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Objet supprimé avec succès !')
        return redirect('list')

    return render(request, 'login_app/delete_item.html', {'item': item})
