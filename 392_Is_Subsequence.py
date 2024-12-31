# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        s_idx, t_idx = 0, 0
        while (t_idx < len(t) and s_idx < len(s)):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
        
        if s_idx == len(s):
            return True
        return False
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
class Solution:
    def __init__(self):
        # We will store the preprocessed results here
        # and the 't' we used to build them
        self.nextPos = None
        self.preprocessed_t = None
    
    def preprocess_t(self, t: str):
        """
        Build a 2D list nextPos where nextPos[i][c] gives the index of
        the next occurrence of character c in t at or after index i.
        If there is no such occurrence, store -1.
        """
        n = len(t)
        # nextPos will have (n+1) rows and 26 columns for 'a'..'z'
        self.nextPos = [[-1] * 26 for _ in range(n+1)]
        
        # Function to convert character to index (0..25)
        def char_to_index(c):
            return ord(c) - ord('a')
        
        # Initialize the last row with -1
        for c in range(26):
            self.nextPos[n][c] = -1
        
        # Fill from the end of t
        for i in range(n - 1, -1, -1):
            # Copy the row below
            for c in range(26):
                self.nextPos[i][c] = self.nextPos[i+1][c]
            # Overwrite for the current character
            curr_char_idx = char_to_index(t[i])
            self.nextPos[i][curr_char_idx] = i
        
        # Remember which t we used for preprocessing
        self.preprocessed_t = t

    def check_subsequence(self, s: str) -> bool:
        """
        Using the precomputed self.nextPos to check if s is a subsequence
        of the already preprocessed string t.
        """
        idx = 0  # Pointer in t
        n = len(self.nextPos) - 1  # Because nextPos has n+1 rows
        def char_to_index(c):
            return ord(c) - ord('a')
        
        for char in s:
            c_idx = char_to_index(char)
            if idx > n:
                return False
            # Find next occurrence of this character at or after idx
            idx = self.nextPos[idx][c_idx]
            if idx == -1:
                # No occurrence found
                return False
            # Move to the character right after matched one
            idx += 1
        return True

    def isSubsequence(self, s, t: str):
        """
        Main function that handles BOTH:
          1) If s is a string, it returns a single True/False.
          2) If s is a list of strings, it returns a list of True/False.

        Internally uses the same preprocessed data structure nextPos.
        If 't' has changed since last time, re-preprocess it.
        """
        # Preprocess 't' only if we haven't or if 't' is different from last time
        if t != self.preprocessed_t:
            self.preprocess_t(t)
        
        # If s is just a single string, return a single boolean
        if isinstance(s, str):
            return self.check_subsequence(s)
        
        # Otherwise, assume s is a list of strings and return a list of booleans
        results = []
        for subsequence_candidate in s:
            results.append(self.check_subsequence(subsequence_candidate))
        return results
