from django.db import models

# Create your models here.
class Clock(models.Model):
    time_left = models.IntegerField(default=90)
    time_start = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20)
