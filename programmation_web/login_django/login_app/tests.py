from django.test import TestCase
from django.urls import reverse
from .models import User


class UserModelTests(TestCase):
    def setUp(self):
        # Créer un utilisateur pour les tests
        self.user = User.objects.create(
            user_login='testuser',
            user_password='testpassword',
            user_mail='test@example.com'
        )

    def test_user_creation(self):
        """Vérifie si un utilisateur est créé correctement."""
        self.assertEqual(self.user.user_login, 'testuser')
        self.assertEqual(self.user.user_mail, 'test@example.com')

    def test_login_view(self):
        """Teste la vue de connexion."""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Vérifie que la redirection se fait
        self.assertRedirects(response, reverse('welcome'))  # Vérifie que la redirection est correcte

    def test_signup_view(self):
        """Teste la vue d'inscription."""
        response = self.client.post(reverse('signup'), {
            'user_login': 'newuser',
            'user_mail': 'newuser@example.com',
            'user_password': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  # Vérifie que la redirection se fait
        self.assertRedirects(response, reverse('login'))  # Vérifie que la redirection est correcte

    def test_logout_view(self):
        """Teste la vue de déconnexion."""
        self.client.login(username='testuser', password='testpassword')  # Connecter l'utilisateur
        response = self.client.get(reverse('logout'))  # Appel de la vue de déconnexion
        self.assertEqual(response.status_code, 302)  # Vérifie que la redirection se fait
        self.assertRedirects(response, reverse('login'))  # Vérifie que la redirection est correcte

#python manage.py test login_app pour run les tests
