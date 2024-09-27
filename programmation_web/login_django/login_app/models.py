from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_login = models.TextField()
    user_password = models.TextField()
    user_compte_id = models.IntegerField(unique=True)
    user_mail = models.TextField()
    user_date_new = models.DateTimeField(auto_now_add=True)
    user_date_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_login
