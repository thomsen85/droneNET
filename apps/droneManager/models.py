from django.db import models

# Create your models here.
class Drone(models.Model):
    name = models.CharField(max_length=30)
    x_pos = models.IntegerField(default=0)
    y_pos = models.IntegerField(default=0)
    speed = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    altimeter = models.IntegerField(default=0)
    task = models.CharField(max_length=50,default="ERR")