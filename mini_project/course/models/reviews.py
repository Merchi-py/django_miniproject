from django.db import models

class Reviews(models.Model):
    review = models.TextField(max_length=500)