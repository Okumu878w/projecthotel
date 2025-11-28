from django.db import models

# Create your models here.
class order(models.Model):
    food=models.CharField(max_length=70)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
