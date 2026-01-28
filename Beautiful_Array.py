# Q1. Beautiful Array
# Solved
# Medium

# Topics
# premium lock icon
# Companies
# An array nums of length n is beautiful if:

# nums is a permutation of the integers in the range [1, n].
# For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
# Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

 

# Example 1:

# Input: n = 4
# Output: [2,1,4,3]
# Example 2:

# Input: n = 5
# Output: [3,1,2,5,4]
 

# Constraints:

# 1 <= n <= 1000

from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # Iterative parity-based construction:
        # Start with [1], repeatedly map to odds then evens, keeping values <= n.
        arr = [1]
        while len(arr) < n:
            odds = [2 * x - 1 for x in arr if 2 * x - 1 <= n]
            evens = [2 * x for x in arr if 2 * x <= n]
            arr = odds + evens
        return arr
