
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"
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
        if word[-1] in '.,:;\'?!()':
            punctuation = word[-1]
            word = word[:-1]
        if word[0] in 'aeiou':
            if word[-1] == 'y':
                return word + 'nay' + punctuation
            elif word[-1] in 'aeiou':
                return word + 'yay' + punctuation
            else:
                return word + 'ay' + punctuation
        else:
            first_vowel_idx = next((i for i, char in enumerate(word) if char in 'aeiou'), None)
            if first_vowel_idx is None:
                return word + 'ay' + punctuation
            elif first_vowel_idx == 0:
                return word + 'ay' + punctuation
            else:
                return word[first_vowel_idx:] + word[:first_vowel_idx] + 'ay' + punctuation

