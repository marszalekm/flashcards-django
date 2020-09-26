from django.urls import path

from .views import Words_learn, Words_manage, WordIndex, word_manage


urlpatterns = [
    path('cards/', Words_learn.as_view(), name='cards'),
    path('manage/', Words_manage.as_view(), name='manage'),
    path('manage/<int:id>', WordIndex.as_view(), name='detail')
]
