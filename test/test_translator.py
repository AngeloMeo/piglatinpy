from unittest import TestCase

from src.translator import PigLatinTranslator

class TestPigLatinTranslator(TestCase):

    def test_something(self):
        # Test method example
        pass

    def test_getPhrase(self):
        translator = PigLatinTranslator("hello world")
        self.assertEqual(translator.get_phrase(), "hello world")