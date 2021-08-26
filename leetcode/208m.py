class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.end = object()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie
        if not word:
            return
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end] = self.end

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
