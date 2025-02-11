# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Set of vowels for quick lookup
        v = {'a', 'e', 'i', 'o', 'u'}
        # Count vowels in the first window of size k
        c = 0
        for i in range(k):
            if s[i] in v:
                c += 1
        # Track the current maximum
        m = c
        # Slide the window through the rest of the string
        for i in range(k, len(s)):
            # Remove the leftmost character if it is a vowel
            if s[i - k] in v:
                c -= 1
            # Add the new rightmost character if it is a vowel
            if s[i] in v:
                c += 1
            # Update the maximum count
            if c > m:
                m = c
            # If we've hit the upper bound (k), return immediately
            if m == k:
                return k
        return m
