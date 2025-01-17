from django import forms
from .models import User

# Formulaire pour la connexion des utilisateurs


class LoginForm(forms.Form):

    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput)


# Formulaire pour l'inscription des nouveaux utilisateurs
class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['user_login', 'user_mail', 'user_password']
        widgets = {
            'user_login': forms.TextInput(),
            'user_mail': forms.TextInput(),
            'user_password': forms.PasswordInput(),
        }
        labels = {
            'user_login': 'Nom d\'utilisateur',
            'user_mail': 'Email',
            'user_password': 'Mot de passe',
        }
        error_messages = {
            'user_login': {
                'unique': "Ce nom d'utilisateur est déjà pris.",
            },
            'user_mail': {
                'unique': "Cette adresse e-mail est déjà utilisée.",
            },
        }
