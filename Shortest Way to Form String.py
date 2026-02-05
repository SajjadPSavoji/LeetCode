# 1055. Shortest Way to Form String
# Solved
# Medium

# Topics
# conpanies icon
# Companies

# Hint
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

# Example 1:

# Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
# Example 2:

# Input: source = "abc", target = "acdbc"
# Output: -1
# Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
# Example 3:

# Input: source = "xyz", target = "xzyxz"
# Output: 3
# Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

# Constraints:

# 1 <= source.length, target.length <= 1000
# source and target consist of lowercase English letters.
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 109,373/177.8K
# Acceptance Rate
# 61.5%

from typing import List

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        m, n = len(source), len(target)

        # Quick impossibility check
        source_set = set(source)
        for ch in target:
            if ch not in source_set:
                return -1

        # next_pos[i][c] = smallest index >= i where source[index] == c, else -1
        # Build from back
        next_pos = [[-1] * 26 for _ in range(m + 1)]
        for c in range(26):
            next_pos[m][c] = -1

        for i in range(m - 1, -1, -1):
            next_pos[i] = next_pos[i + 1][:]          # copy row
            next_pos[i][ord(source[i]) - 97] = i      # update current char

        ans = 1
        i = 0  # pointer in source for current subsequence
        for ch in target:
            c = ord(ch) - 97
            j = next_pos[i][c]
            if j == -1:
                # Need a new subsequence starting from 0
                ans += 1
                i = 0
                j = next_pos[i][c]  # must exist due to pre-check
            i = j + 1  # move past matched char
            if i == m:
                i = m  # keep at end; next lookup from m will force new subseq if needed

        return ans
