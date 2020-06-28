from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=50, blank=False)
    desc = models.CharField(max_length=2000, blank=False)
    price = models.IntegerField()

    def __str__(self):
        return self.name
