from django.db import models
from django.urls import reverse

# Create your models here.
class Fish(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField('Image URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fish_detail', kwargs={'fish_id': self.id})




class Gear(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gear_detail', kwargs={'gear_id': self.id})