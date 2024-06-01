# Generated by Django 5.0.3 on 2024-04-18 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funko_api', '0003_alter_user_funkos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('operativeSistem', models.CharField(max_length=130)),
                ('desarollador', models.CharField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('games', models.ManyToManyField(blank=True, to='funko_api.game')),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('games', models.ManyToManyField(blank=True, to='funko_api.game')),
            ],
        ),
    ]