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


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']
