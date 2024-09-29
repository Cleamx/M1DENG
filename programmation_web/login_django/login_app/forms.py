from django import forms
from .models import User

# Formulaire pour la connexion des utilisateurs
class LoginForm(forms.Form):
    # Champ pour le nom d'utilisateur
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)

    # Champ pour le mot de passe, masqué pour la sécurité
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput)


# Formulaire pour l'inscription des nouveaux utilisateurs
class SignupForm(forms.ModelForm):

    class Meta:
        model = User  # Spécifie le modèle à utiliser pour ce formulaire
        # Les champs à inclure dans le formulaire
        fields = ['user_login', 'user_mail', 'user_password']
        widgets = {
            'user_login': forms.TextInput(),  # Champ de texte pour le nom d'utilisateur
            'user_mail': forms.TextInput(),    # Champ de texte pour l'email
            'user_password': forms.PasswordInput(),  # Champ de mot de passe
        }
        labels = {
            'user_login': 'Nom d\'utilisateur',  # Étiquette pour le champ nom d'utilisateur
            'user_mail': 'Email',                  # Étiquette pour le champ email
            'user_password': 'Mot de passe',       # Étiquette pour le champ mot de passe
        }
