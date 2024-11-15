from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_login = models.TextField(max_length=150, unique=True)
    user_password = models.TextField()
    user_mail = models.TextField(unique=True)
    user_date_new = models.DateTimeField(auto_now_add=True)
    user_date_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_login


# Liste des types d'objets pour l'inventaire
ITEM_TYPES = [
    ('potion', 'Potion'),
    ('plante', 'Plante'),
    ('arme', 'Arme'),
    ('cle', 'Clé'),
    ('armure', 'Pièce d\'armure'),
]

class Item(models.Model):
    # Clé étrangère pour lier l'objet à un utilisateur
    # Lien avec le modèle User
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100) 
    item_type = models.CharField(
        max_length=20, choices=ITEM_TYPES)  
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} ({self.quantity})'
