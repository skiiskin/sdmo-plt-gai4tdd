import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        translator = PigLatin("hello world")
        self.assertEqual("hello world", translator.get_phrase())

    def test_translation_empty(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    def test_translation_starting_vowel_ending_y(self):
        translator = PigLatin("any")
        self.assertEqual("anynay", translator.translate())


