from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from rest_framework.parsers import JSONParser
from .models import Word
from .serializers import WordSerializer
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer, \
    JSONRenderer, \
    BrowsableAPIRenderer



class WordViewSet(viewsets.ModelViewSet):

    queryset = Word.objects.all()

    serializer_class = WordSerializer
    template_name = "deck.html"
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    @action(detail=False, renderer_classes=[TemplateHTMLRenderer, JSONRenderer])
    def get(self, request, *args, **kwargs):
        serializer = WordSerializer()
        context = {'cards': serializer}
        return Response(context)

class WordAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "deck.html"

    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        # return Response(serializer.data)
        return Response({'cards': words})

    def post(self, request):
        serializer = WordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     queryset = Word.objects.all()
    #     template_name = "deck.html"
    #     # return Response({'cards': queryset})
    #     return render(request, template_name, {'cards': queryset})

        # request, 'app/my.html', {'data': serializer_class.data,}

# class GenericAPIView(generics.GenericAPIView,
#                      mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.DestroyModelMixin):
#     serializer_class = WordSerializer
#     queryset = Word.objects.all()
#     lookup_field = 'id'
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
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



#
#
# class WordIndex(APIView):
#
#     def get_object(self, id):
#         try:
#             return Word.objects.get(id=id)
#
#         except Word.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, id):
#         word = self.get_object(id)
#         serializer = WordSerializer(word)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         word = self.get_object(id)
#         serializer = WordSerializer(word, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         word = self.get_object(id)
#         word.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def word_list(request):
#
#     if request.method == 'GET':
#         words = Word.objects.all()
#         serializer = WordSerializer(words, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = WordSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def word_index(request, pk):
#     try:
#         word = Word.objects.get(pk=pk)
#
#     except Word.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = WordSerializer(word)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = WordSerializer(word, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         word.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
