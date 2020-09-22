from .models import Word
from .serializers import WordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer


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
