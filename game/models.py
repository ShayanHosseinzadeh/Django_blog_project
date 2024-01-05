from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Game(models.Model):
    STATUS_CHOICES = (
        ('Released','Released'),
        ('not Released','Not Released'),

    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    year_released = models.IntegerField()
    company = models.CharField(max_length=20)
    status = models.CharField(choices=STATUS_CHOICES,max_length=12)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Game_detail_view',args=[self.id])
