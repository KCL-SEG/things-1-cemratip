from django.db import models

class Thing(models.Model):
    name = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
