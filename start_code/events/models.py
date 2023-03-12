from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='images/')

    def __str__(self): 
        return (self.title)