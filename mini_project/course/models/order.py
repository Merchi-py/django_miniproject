from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=150, null=True)
