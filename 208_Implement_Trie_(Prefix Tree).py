# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

# implement using dictionaries
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['#'] = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return '#' in current

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

# # implement using tree
# class Node:
#     def __init__(self):
#         self.child = {}
#         self.is_end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = Node()

#     def insert(self, word: str) -> None:
#         current = self.root
#         for char in word:
#             if char not in current.child:
#                 current.child[char] = Node()
#             current = current.child[char]
#         current.is_end_of_word = True

#     def _find_node(self, prefix: str) -> Node:
#         """Returns the node that ends the given prefix, or None if not found."""
#         current = self.root
#         for char in prefix:
#             if char not in current.child:
#                 return None
#             current = current.child[char]
#         return current

#     def search(self, word: str) -> bool:
#         node = self._find_node(word)
#         return node is not None and node.is_end_of_word

#     def startsWith(self, prefix: str) -> bool:
#         return self._find_node(prefix) is not None
