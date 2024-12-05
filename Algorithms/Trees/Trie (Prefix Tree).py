# Insert Word: O(1) where 1 is really the length of the word | Search Word: O(1) | Search Prefix: O(1)
# Application: search engines (start typing a few characters and get autocomplete for strings matching that prefix), every letter has it's own trie of every letter

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        # assume first node is empty and pointing at all possible child root nodes
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.word

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True