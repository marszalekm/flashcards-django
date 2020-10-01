from django.contrib import admin
from .models import Word, Pack
# Register your models here.

class WordProfile(admin.ModelAdmin):

    list_display = ['original', 'translation', 'deck']


class PackProfile(admin.ModelAdmin):

    list_display = ['name', 'description', 'author']

admin.site.register(Word, WordProfile)

admin.site.register(Pack, PackProfile)
