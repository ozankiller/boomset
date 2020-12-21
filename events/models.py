from django.db import models

from django.urls import reverse

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    timezone = models.IntegerField()
 
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('read_event', kwargs={'pk': self.pk})

class Session(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    speaker = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('read_session', kwargs={'pk': self.pk})