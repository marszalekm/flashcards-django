from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .models import Word
from .serializers import WordSerializer
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .forms import WordForm

class Words_learn(APIView):

    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    template_name = "deck.html"

    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        # return Response(serializer.data)
        return Response({'cards': words})

class Words_manage(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "manage.html"

    style = {'template_pack': 'rest_framework/vertical/'}

    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        # return Response(serializer.data)
        return Response({'serializer': serializer, 'cards': words})
        # return Response({'cards': words})

    def post(self, request):

        serializer = WordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # form = WordForm()
        # context = {'form': form}

# class GenericAPIView(generics.GenericAPIView,
#                      mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.DestroyModelMixin):
#     serializer_class = WordSerializer
#     queryset = Word.objects.all()
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
#     template_name = "index.html"
#
#     style = {'template_pack': 'rest_framework/vertical/'}
#
#     lookup_field = 'id'
#
#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#     def put(self, request, id=None):
#         return self.update(request, id)
#
#     def delete(self, request, id=None):
#         return self.destroy(request, id)


class WordIndex(APIView):


    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "index.html"


    def get_object(self, id):
        try:
            return Word.objects.get(id=id)

        except Word.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        word = get_object_or_404(Word, id=id)
        serializer = WordSerializer(word)
        return Response({'serializer': serializer, 'word': word})

    def put(self, request, id):
        word = get_object_or_404(Word, id=id)
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'word': word})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        word = self.get_object(id)
        word.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    # def post(self, request):
    #     word = get_object_or_404(Word, pk=pk)
    #     serializer = WordSerializer(word)
    #
    #     # if serializer.is_valid():
    #     #     serializer.save()
    #     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'word': word})
    #     serializer.save()
    #     return redirect('word-list')


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def word_manage(request):

    if request.method == 'GET':
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        # return Response(serializer.data)
        return Response({'cards': words}, template_name="manage.html")
        # return Response({'cards': serializer}, template_name="manage.html")

    elif request.method == 'POST':
        form = WordForm(request.POST)

        serializer = WordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def word_index(request, pk):
    try:
        word = Word.objects.get(pk=pk)

    except Word.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordSerializer(word)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        word.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)





