from django.urls import path

from .views import WordsLearn, \
    WordsManage, \
    WordIndex, \
    word_delete, \
    word_add


urlpatterns = [
    path('cards/', WordsLearn.as_view(), name='cards'),
    path('manage/', WordsManage.as_view(), name='manage'),
    path('manage/add/', word_add, name='add'),
    path('manage/<int:id>', WordIndex.as_view(), name='detail'),
    path('manage/<int:id>/delete', word_delete, name='delete')
]
