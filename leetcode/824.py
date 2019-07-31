class Solution:
    def toGoatLatin(self, S: str) -> str:
        if not S:
            return S
        words = S.split(' ')
        words = [w for w in words if w]
        if not words:
            return S
        new_words = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        for idx, word in enumerate(words, start=1):
            if not word:
                continue
            if word[0].lower() in vowels:
                new_word = word + 'ma'
            else:
                new_word = word[1:] + word[0] + 'ma'
            new_word += 'a' * idx
            new_words.append(new_word)

        return ' '.join(new_words)
