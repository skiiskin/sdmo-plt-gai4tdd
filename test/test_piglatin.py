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

    def test_translation_starting_vowel_ending_vowel(self):
        translator = PigLatin("apple")
        self.assertEqual("appleyay", translator.translate())

    def test_translation_starting_vowel_ending_consonant(self):
        translator = PigLatin("ask")
        self.assertEqual("askay", translator.translate())

    def test_translation_starting_single_consonant(self):
        translator = PigLatin("hello")
        self.assertEqual("ellohay", translator.translate())

    def test_translation_starting_several_consonants(self):
        translator = PigLatin("known")
        self.assertEqual("ownknay", translator.translate())

    def test_translation_several_words_separated_by_space(self):
        translator = PigLatin("hello world")
        self.assertEqual("ellohay orldway", translator.translate())

    def test_translation_composite_words(self):
        translator = PigLatin("well-being")
        self.assertEqual("ellway-eingbay", translator.translate())

    def test_translation_several_words_with_punctuation(self):
        translator = PigLatin("hello world!")
        self.assertEqual("ellohay orldway!", translator.translate())

    def test_translation_illegal_punctuation(self):
        translator = PigLatin("world#")
        self.assertRaises(PigLatinError, translator.translate)

    def test_translation_starting_with_uppercase(self):
        translator = PigLatin("Hello")
        self.assertEqual("Ellohay", translator.translate())

    def test_translation_title_case(self):
        translator = PigLatin("APPLE")
        self.assertEqual("APPLEYAY", translator.translate())

    def test_translation_mixed_cases(self):
        translator = PigLatin("biRd")
        self.assertRaises(PigLatinError, translator.translate)