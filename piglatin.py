
from error import PigLatinError

class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"
        if any(char in self.phrase for char in '#@$%^&*={}[]|\\<>'):
            raise PigLatinError("Illegal punctuation found.")
        words = self.phrase.split()
        translated_words = []
        for word in words:
            if '-' in word:
                subwords = word.split('-')
                translated_subwords = [self.translate_subword(subword) for subword in subwords]
                translated_word = '-'.join(translated_subwords)
            else:
                translated_word = self.translate_subword(word)
            translated_words.append(translated_word)
        return ' '.join(translated_words)

    def translate_subword(self, word):
        punctuation = ""
        capitalization = False
        if word[-1] in '.,:;\'?!()':
            punctuation = word[-1]
            word = word[:-1]
        if word[0].isupper():
            capitalization = True
            word = word.lower()
        if word[0] in 'aeiou':
            if word[-1] == 'y':
                result = word + 'nay'
            elif word[-1] in 'aeiou':
                result = word + 'yay'
            else:
                result = word + 'ay'
        else:
            first_vowel_idx = next((i for i, char in enumerate(word) if char in 'aeiou'), None)
            if first_vowel_idx is None:
                result = word + 'ay'
            else:
                result = word[first_vowel_idx:] + word[:first_vowel_idx] + 'ay'
        if capitalization:
            result = result.capitalize()
        return result + punctuation

