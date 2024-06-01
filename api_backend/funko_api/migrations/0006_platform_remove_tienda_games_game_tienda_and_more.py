# Generated by Django 5.0.3 on 2024-04-18 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funko_api', '0005_operativesistem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
            ],
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='games',
        ),
        migrations.AddField(
            model_name='game',
            name='tienda',
            field=models.ManyToManyField(to='funko_api.tienda'),
        ),
        migrations.RemoveField(
            model_name='game',
            name='operativeSistem',
        ),
        migrations.DeleteModel(
            name='OperativeSistem',
        ),
        migrations.AddField(
            model_name='game',
            name='operativeSistem',
            field=models.ManyToManyField(to='funko_api.platform'),
        ),
    ]