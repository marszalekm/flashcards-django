from django import forms
from django.forms import Textarea

from .models import Word, Pack

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['original', 'translation', 'deck', 'visible']

    # def __init__(self, user, *args, **kwargs):
    #     super(WordForm, self).__init__(*args, **kwargs)
    #     self.fields['deck'].queryset = Word.objects.all().filter(deck='deck__author')


class DeckForm(forms.ModelForm):

    class Meta:
        model = Pack
        fields = ['name', 'description']
        exclude = ('author',)
        widgets = {
            'description': Textarea(
                {
                'class': "form-control form-control-lg",
                'rows': 2,
                'cols': 30,
                }
            )
        }

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('author', None)
        super(DeckForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(DeckForm, self).save(commit=False)
        inst.author = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst