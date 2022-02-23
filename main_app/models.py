from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


LAKES = (
    ('Pines', 'Lake O The Pines'),
    ('Caddo', 'Caddo Lake'),
    ('Lone Star', 'Lake Lone Star'),
    ('Sandlin', 'Lake Bob Sandlin')
)
LOGS = (
    ('Pines', 'Lake O The Pines'),
    ('Caddo', 'Caddo Lake'),
    ('Lone Star', 'Lake Lone Star'),
    ('Sandlin', 'Lake Bob Sandlin')
)

# Create your models here.
class Gear(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gear_detail', kwargs={'gear_id': self.id})


        
class Fish(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField('Image URL')
    gears = models.ManyToManyField(Gear)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fish_detail', kwargs={'fish_id': self.id})



class Lake(models.Model):
    name = models.CharField(
        max_length=100,
        choices=LAKES,
        default=LAKES[0][0]
    )

    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_name_display()}"



class Log(models.Model):
    date = models.DateField()
    location = models.CharField(
        max_length=100,
        choices=LOGS,
        default=LOGS[0][0]
    )
    length = models.IntegerField()
    weight = models.FloatField()

    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} at {self.get_location_display()} was {self.length} and {self.weight}"

    class Meta:
        ordering = ['-date']