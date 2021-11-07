"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

"""
# You were supposed to use a Trie lol
from collections import defaultdict

class WordDictionary:

    def __init__(self):
        self.words = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.words[len(word)].append(word)

    def search(self, word: str) -> bool:
        def match(word_in_dict, idx):
            return word[idx] in [word_in_dict[idx], '.']

        candidates = self.words[len(word)]
        for candidate in candidates:
            if all(match(candidate, idx) for idx, char in enumerate(candidate)):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
