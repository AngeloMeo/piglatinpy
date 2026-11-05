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

    def test_translate_word_starting_with_vowel_ending_y(self):
        translator = PigLatinTranslator("any")
        self.assertEqual("anynay", translator.translate())

    def test_translate_word_starting_with_vowel_ending_with_vowel(self):
        translator = PigLatinTranslator("apple")
        self.assertEqual("appleyay", translator.translate())

    def test_translate_word_starting_with_vowel_ending_with_consonant(self):
        translator = PigLatinTranslator("ask")
        self.assertEqual("askay", translator.translate())

    def test_translate_word_starting_with_consonant(self):
        translator = PigLatinTranslator("hello")
        self.assertEqual("ellohay", translator.translate())