# Generated by Django 5.1.1 on 2024-12-17 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0005_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.user')),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]