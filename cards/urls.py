from django.urls import path

from .views import WordsLearnCards, \
    WordsLearnDecks, \
    DecksManage, \
    WordsManage, \
    WordIndex, \
    word_delete, \
    word_add, \
    deck_add


urlpatterns = [
    path('decks/', WordsLearnDecks.as_view(), name='decks'),
    path('decks/<int:deck>/', WordsLearnCards.as_view(), name='singledeck'),
    path('manage/', DecksManage.as_view(), name='manage'),
    path('manage/<int:deck>/', WordsManage.as_view(), name='managedeck'),
    path('add/word', word_add, name='word_add'),
    path('add/deck', deck_add, name='deck_add'),
    path('manage/<int:deck>/<int:id>', WordIndex.as_view(), name='detail'),
    path('manage/<int:deck>/<int:id>/delete', word_delete, name='delete')
]
