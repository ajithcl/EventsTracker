from django.db import models


# Create your models here.
class Entity(models.Model):
    EntityName = models.CharField(max_length=20)
    CreatedDate = models.DateField()
    UpdatedDate = models.DateField()
    Comments = models.CharField(max_length=1000)
    ImageFileName = models.CharField(max_length=50)
    UserId = models.CharField(max_length=20, default='blank_user')

