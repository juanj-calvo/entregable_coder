from django.db import models

# Create your models here.
class family(models.Model):
    integrant = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date = models.DateField(auto_now_add= True)