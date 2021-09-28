from django.db import models


# Create your models here.
class Event(models.Model):
    EventDate = models.DateField()
    EntityName = models.CharField(max_length=25)
    EventName = models.CharField(max_length=25)
    Comments = models.CharField(max_length=500)
    UserId = models.CharField(max_length=25)
    EntityId = models.UUIDField()   # Field for storing ID from Entity model
    # Need to add events links in seperate model
