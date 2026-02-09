# Q1. Shortest Palindrome
# Solved
# Hard

# Topics
# conpanies icon
# Companies
# You are given a string s. You can convert s to a palindrome by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.

 

# Example 1:

# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: s = "abcd"
# Output: "dcbabcd"
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of lowercase English letters only.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def longest_proper_prefix_suffic(s: str) -> str:
            j = 0
            lps = [0] * len(s)
            for i in range(1, len(s)):
                while j > 0 and s[i] != s[j]:
                    j = lps[j-1]
                
                if s[i] == s[j]:
                    j += 1
                
                lps[i] = j

            return lps[-1]

        t = s + "#" + s[::-1]
        j = longest_proper_prefix_suffic(t)
        return s[j:][::-1] + s
