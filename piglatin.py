
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
            if word[0] in 'aeiou':
                translated_word = word + 'nay'
            else:
                first_vowel_idx = next((i for i, letter in enumerate(word) if letter in 'aeiou'), len(word))
                translated_word = word[first_vowel_idx:] + word[:first_vowel_idx] + 'ay'
            translated_words.append(translated_word)
        return ' '.join(translated_words)

