from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255, required=True)
    author = models.CharField(max_length=255, required=True)
    release_date = models.DateField(required=True)
    synopsis = models.TextField(required=True)
