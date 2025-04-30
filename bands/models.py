from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()
    def __str__(self):
        return f'Musician {self.id}: {self.first_name} {self.last_name}'
    
class Band(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return f'Band {self.id}: {self.name}'
    musicians = models.ManyToManyField(Musician)
    def __str__(self):
        return f'Band {self.id}: {self.name}'
