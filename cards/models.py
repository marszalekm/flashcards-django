from django.db import models


class Word(models.Model):
    original = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    deck = models.CharField(max_length=20)

    def __str__(self):
        return self.original