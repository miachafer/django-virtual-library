from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_date = models.DateField()
    synopsis = models.TextField()

    def __str__(self):
        return f'"{self.name}" by {self.author}'