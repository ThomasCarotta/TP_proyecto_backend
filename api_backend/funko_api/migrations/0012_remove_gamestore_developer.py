# Generated by Django 5.0.3 on 2024-05-16 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funko_api', '0011_remove_gamedeveloper_games_game_developer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamestore',
            name='developer',
        ),
    ]