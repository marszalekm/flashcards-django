from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WordViewSet, WordAPIView # GenericAPIView
    # WordIndex, \
    # word_list, \
    # word_index, \

# router = DefaultRouter()
# router.register('cards', WordViewSet, basename='cards')

urlpatterns = [
    # path(r'', include(router.urls)),
    # path('<int:pk>', include(router.urls))
    # path('cards/', word_list),
    path('cards/', WordAPIView.as_view(), name='cards'),
    # path('generic/cards/<int:id>', GenericAPIView.as_view()),
    # path('index/<int:pk>/', word_index),
    # path('index/<int:id>/', WordIndex.as_view())
]
