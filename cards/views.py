from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view, permission_classes, authentication_classes, renderer_classes
from .models import Word, Pack
from .serializers import WordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .forms import WordForm, DeckForm
from django.contrib import messages

class WordsLearnDecks(APIView):

    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    template_name = "decks.html"

    def get(self, request):
        decks = Pack.objects.all().filter(author=self.request.user)
        serializer = WordSerializer(decks, many=True)
        return Response({'serializer': serializer, 'decks': decks})

class WordsLearnCards(APIView):

    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    template_name = "cards.html"

    def get(self, request, deck):
        try:
            words = Word.objects.all().filter(deck=deck, visible=True)
            if words[0].deck.author == request.user:
                serializer = WordSerializer(words, many=True)
                return Response({'serializer': serializer, 'cards': words})
            else:
                return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return render(request, "empty_deck.html", {})

class DecksManage(APIView):

    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "manage_decks.html"

    def get(self, request):
        decks = Pack.objects.all().filter(author=self.request.user)
        serializer = WordSerializer(decks, many=True)
        return Response({'serializer': serializer, 'decks': decks})

class WordsManage(APIView):

    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "manage_cards.html"

    def get(self, request, deck):
        try:
            words = Word.objects.all().filter(deck=deck)
            if words[0].deck.author == request.user:
                serializer = WordSerializer(words, many=True)
                return Response({'serializer': serializer, 'cards': words})
            else:
                return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return render(request, "empty_deck.html", {})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@renderer_classes([TemplateHTMLRenderer])
def word_add(request):

    form = WordForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = WordForm()
        messages.success(request, 'Word added successfully.')
    context = {'form': form}
    return render(request, "add_card.html", context)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@renderer_classes([TemplateHTMLRenderer])
def deck_add(request):

    form = DeckForm(request.POST, author=request.user)
    if form.is_valid():
        form.save()
        form = DeckForm()
        messages.success(request, 'Deck added successfully.')
    else:
        form = DeckForm(author=request.user)
    context = {'form': form}
    return render(request, "add_deck.html", context)

class WordIndex(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "index.html"

    def get_object(self, deck, id):
        try:
            return Word.objects.get(id=id)

        except Word.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, deck, id):
        word = get_object_or_404(Word, id=id)
        if word.deck.author == request.user:
            serializer = WordSerializer(word)
            return Response({'serializer': serializer, 'word': word})
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)


    def post(self, request, deck, id):
        word = get_object_or_404(Word, id=id)
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            if word.deck.author == request.user:
                serializer.save()
                return Response({'serializer': serializer, 'word': word})
            else:
                return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication, BasicAuthentication])
def word_delete(request, deck, id):
    try:
        word = Word.objects.get(id=id)

    except Word.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':

        if word.deck.author == request.user:
            word.delete()
            return redirect('../')
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    else:
        pass
