from django.urls import path
from .views import word_list, \
    word_index, \
    WordAPIView, \
    WordIndex, \
    GenericAPIView

urlpatterns = [
    # path('cards/', word_list),
    path('cards/', WordAPIView.as_view()),
    path('generic/cards/<int:id>', GenericAPIView.as_view()),
    # path('index/<int:pk>/', word_index),
    path('index/<int:id>/', WordIndex.as_view())
]
