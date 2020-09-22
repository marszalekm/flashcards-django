from django.db import models


class Word(models.Model):
    original = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    deck = models.CharField(max_length=20)
    # owner = models.ForeignKey('auth.User', related_name='cards', on_delete=models.CASCADE)
    # highlighted = models.TextField()

    def __str__(self):
        return self.original
