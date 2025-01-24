# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.



# Example 1:

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
# Example 2:

# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Explanation: The only word "havana" will be always suggested while typing the search word.


# Constraints:

# 1 <= products.length <= 1000
# 1 <= products[i].length <= 3000
# 1 <= sum(products[i].length) <= 2 * 104
# All the strings of products are unique.
# products[i] consists of lowercase English letters.
# 1 <= searchWord.length <= 1000
# searchWord consists of lowercase English letters.



# solve using binary search
from typing import List
import bisect

class Solution:
  def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
      # 1. Sort products lexicographically
      products.sort()
      
      result = []
      prefix = ""
      
      for char in searchWord:
          # Build the prefix incrementally
          prefix += char
          
          # 2. Use bisect to find the start index (left boundary) 
          # for products that could match 'prefix'
          # 'bisect_left(products, prefix)' gives the insertion position
          # where 'prefix' would fit. This is effectively the first product 
          # that is NOT smaller than 'prefix' lex order.
          start_idx = bisect.bisect_left(products, prefix)
          
          # 3. The next prefix would be prefix with an ASCII character 
          # that is just bigger than 'z'. 
          # But simpler: we can do prefix_with_next_char = prefix + '{'
          # since '{' has ASCII value 123, just after 'z'=122
          # prefix_with_next_char = prefix[:-1] + chr(ord(prefix[-1]) + 1) if prefix else '{'
          # Or more commonly:
          # prefix_with_next_char = prefix + '{'  
          # ensures we find the first product that is strictly greater than
          # all strings with prefix "prefix"
          
          # 4. Use bisect to find the end of the range
          end_idx = bisect.bisect_left(products, prefix + '{')
          
          # 5. Now products[start_idx : end_idx] are all strings with that prefix.
          # We only want up to 3 suggestions.
          matched = products[start_idx : min(start_idx + 3, end_idx)]
          
          result.append(matched)
      
      return result


# Solve using Trie
from typing import List
class TrieNode:
  __slots__ = ['children', 'suggestions']  # Slight memory optimization
  def __init__(self):
      self.children = {}
      # Store up to 3 product names (strings) that pass through this node
      self.suggestions = []

class Trie:
  def __init__(self):
      self.root = TrieNode()
  
  def insert(self, product: str) -> None:
      """
      Insert a product into the Trie. Because 'products' is already sorted,
      we simply push 'product' into each node's suggestions list if that
      node has fewer than 3 suggestions.
      """
      current = self.root
      for char in product:
          if char not in current.children:
              current.children[char] = TrieNode()
          current = current.children[char]
          # Keep only up to 3 suggestions
          if len(current.suggestions) < 3:
              current.suggestions.append(product)
  
  def get_suggestions(self, searchWord: str) -> List[List[str]]:
      """
      Return a list of lists of suggestions, one sub-list for each character
      typed in searchWord. If we hit a mismatch, break and fill the
      remaining sub-lists with empty lists.
      """
      result = []
      current = self.root
      
      for i, char in enumerate(searchWord):
          # If there's no matching child, fill remainder with empty lists
          if char not in current.children:
              result.append([])
              # Fill the rest of the characters with []
              result.extend([[] for _ in range(i+1, len(searchWord))])
              break
          # Otherwise, descend and add that node's top-3 suggestions
          current = current.children[char]
          result.append(current.suggestions)
      return result


class Solution:
  def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
      # 1. Sort products so each Trie node's suggestions are in lexicographic order
      products.sort()
      
      # 2. Build the Trie
      trie = Trie()
      for product in products:
          trie.insert(product)
      
      # 3. Retrieve suggestions after typing each character in searchWord
      return trie.get_suggestions(searchWord)

