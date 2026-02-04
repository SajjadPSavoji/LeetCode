# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = r = 0
        mf = 0          # max frequency in current window
        ans = 0
        n = len(s)

        while r < n:
            # window is [l, r) with length r-l
            if (r - l) - mf <= k:
                # current window is valid → record it, then expand by one
                ans = max(ans, r - l)

                ch = s[r]
                count[ch] += 1
                mf = max(mf, count[ch])
                r += 1
            else:
                # invalid → shrink by one
                left = s[l]
                count[left] -= 1
                if count[left] == 0:
                    del count[left]

                mf = max(count.values(), default=0)  # safe when empty
                l += 1

        # after loop, last window might be the best valid one
        if (r - l) - mf <= k:
            ans = max(ans, r - l)

        return ans
      
