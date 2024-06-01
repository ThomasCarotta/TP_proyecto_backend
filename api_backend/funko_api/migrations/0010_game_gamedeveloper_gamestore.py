# Generated by Django 5.0.3 on 2024-05-16 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funko_api', '0009_remove_game_platform_remove_game_tienda_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='GameDeveloper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('games', models.ManyToManyField(to='funko_api.game')),
            ],
        ),
        migrations.CreateModel(
            name='GameStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('developer', models.ManyToManyField(to='funko_api.gamedeveloper')),
                ('games', models.ManyToManyField(to='funko_api.game')),
            ],
        ),
    ]