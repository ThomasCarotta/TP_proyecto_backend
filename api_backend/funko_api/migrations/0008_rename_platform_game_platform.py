# Generated by Django 5.0.3 on 2024-04-18 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funko_api', '0007_rename_operativesistem_game_platform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='Platform',
            new_name='platform',
        ),
    ]
