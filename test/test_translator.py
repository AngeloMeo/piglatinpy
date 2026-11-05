from unittest import TestCase

import translator
from src.translator import PigLatinTranslator

class TestPigLatinTranslator(TestCase):

    def test_something(self):
        # Test method example
        pass

    def test_getPhrase(self):
        translator = PigLatinTranslator("hello world")
        self.assertEqual(translator.get_phrase(), "hello world")

    def test_translate_empty_phrase(self):
        translator = PigLatinTranslator("")
        self.assertEqual("nil", translator.translate())