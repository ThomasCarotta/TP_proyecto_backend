from django.db import models

# Create your models here.

class GameDeveloper(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'

class GameStore(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.name}'

class Game(models.Model):
    name = models.CharField(max_length=128)
    developer= models.ManyToManyField(GameDeveloper,blank=False)
    store= models.ManyToManyField(GameStore,blank=False)
    def __str__(self):
        return f'{self.name}'

