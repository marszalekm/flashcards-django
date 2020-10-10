from django.test import SimpleTestCase
from cards.forms import WordForm, DeckForm


class TestWordForm(SimpleTestCase):

    # def test_word_form_valid(self):
    #     form = WordForm(data={
    #         'original': '1st_word',
    #         'translation': '2nd_word',
    #         'deck': 12,
    #         'visible': True
    #     })
    #
    #     self.assertTrue(form.is_valid())

    def test_word_form_invalid(self):
        form = WordForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

class TestPackForm(SimpleTestCase):

    def test_word_form_valid(self):

        form = DeckForm(data={
            'name': 'title_text',
            'description': 'description_text',
            'author': 'test_user',
        })

        self.assertTrue(form.is_valid())

    def test_word_form_invalid(self):
        form = WordForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
