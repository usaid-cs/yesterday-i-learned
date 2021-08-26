class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.end = object()

    def insert(self, word: str, val=None) -> None:
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
        if val is None:
            node[self.end] = self.end
        else:
            node[self.end] = val

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



class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        # What's val for?
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        node = self.trie.trie
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]
        return self.get_keys(node)

    def get_keys(self, node) -> int:
        if isinstance(node, int):
            return node
        keys = node.keys()
        count = 0 # len([k for k in keys if k != self.trie.end])
        for key in keys:
            count += self.get_keys(node[key])
        return count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
