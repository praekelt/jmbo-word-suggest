from django.test import TestCase
from jmbowordsuggest.models import AcceptedWord,AcceptedWordCategory
from jmbowordsuggest.utils import suggest_words


class SuggestWordsTestCase(TestCase):
    fixtures = [
        'fixtures/sample.json',
    ]

    def setUp(self):
        pass

    def test_correct_word_suggested(self):
        words = suggest_words('skills', 'domastic')
        word, rank = words[0]
        self.assertEqual(word, 'Domestic Worker')
        
        words = suggest_words('skills', 'pluumbar')
        word, rank = words[0]
        self.assertEqual(word, 'Plumber')
        
        words = suggest_words('skills', 'grass cutter')
        word, rank = words[0]
        self.assertEqual(word, 'Grass Cutting')
        
        words = suggest_words('skills', 'news reader')
        word, rank = words[0]
        self.assertEqual(word, 'Radio news reader')
        
        words = suggest_words('jobs', 'markketing')
        word, rank = words[0]
        self.assertEqual(word, 'Marketting and Sales')
        
        words = suggest_words('jobs', 'waitress')
        word, rank = words[0]
        self.assertEqual(word, 'Waiter')
        
    def test_searched_word_not_exist(self):
        words = suggest_words('skills', 'electrician')
        self.assertEqual(words, [])
        
        words = suggest_words('skills', 'journalist')
        self.assertEqual(words, [])
