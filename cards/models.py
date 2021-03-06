from django.db import models
from django.conf import settings


class Pack(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=20)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Deck name")

    def __str__(self):
        return self.name


class Word(models.Model):
    original = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    deck = models.ForeignKey(Pack, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True, blank=False)

    class Meta:
        verbose_name = ("Word")

    def __str__(self):
        return self.original

