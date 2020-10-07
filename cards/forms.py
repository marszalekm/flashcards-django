from django import forms

from .models import Word, Pack

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['original', 'translation', 'deck', 'visible']

    # def __init__(self, user, *args, **kwargs):
    #     super(WordForm, self).__init__(*args, **kwargs)
    #     self.fields['deck'].queryset = Word.objects.all().filter(deck='deck__author')

class DeckForm(forms.ModelForm):

    name = forms.CharField()
    description = forms.CharField(
        widget=forms.Textarea(
            attrs=
            {
                'class': "form-control form-control-lg",
                'rows': 3,
                'cols': 30,
            }
        )
    )

    class Meta:
        model = Pack
        fields = ['name', 'description']
        exclude = ["author"]