from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view, permission_classes, authentication_classes, renderer_classes
from .models import Word
from .serializers import WordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .forms import WordForm
from django.contrib import messages

class WordsLearn(APIView):

    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    template_name = "deck.html"

    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response({'cards': words})

class WordsManage(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "manage.html"

    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response({'serializer': serializer, 'cards': words})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@renderer_classes([TemplateHTMLRenderer])
def word_add(request):

    form = WordForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = WordForm()
        messages.success(request, 'Word added successfully.')
    context = {'form': form}
    return render(request, "add.html", context)

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

    def post(self, request, id):
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


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
def word_delete(request, id):
    try:
        word = Word.objects.get(id=id)

    except Word.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':

        word.delete()
        return redirect('../')
    else:
        pass
