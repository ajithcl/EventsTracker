from django.db import models


# Create your models here.
class Entity(models.Model):
    EntityName = models.CharField(max_length=20)
    CreatedDate = models.DateField()
    UpdatedDate = models.DateField()
    Comments = models.CharField(max_length=1000)
    ImagePath = models.CharField(max_length=200)
