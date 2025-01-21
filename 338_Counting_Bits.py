# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105
 

# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


class Solution:
    # # using concats and repeated patterns
    # def countBits(self, n: int) -> List[int]:
    #     counts = [0]
    #     i = 1
    #     while i <n:
    #         counts = counts + [c+1 for c in counts]
    #         i*=2
    #     r = n-i+1
    #     if r > 0:
    #         counts = counts + [counts[k]+1 for k in range(r)]
    #     if r < 0:
    #         counts = counts[:r]
    #     return counts

    # # using a constanct memeory
    # def countBits(self, n: int) -> List[int]:
    #     counts = [0] * (n + 1)
        
    #     # Current power-of-two block start
    #     start = 1
    #     while start <= n:
    #         end = min(2 * start - 1, n)
    #         for i in range(start, end + 1):
    #             # The offset from the start is i - start, 
    #             # and counts[i] = counts[i - start] + 1
    #             counts[i] = counts[i - start] + 1
    #         start *= 2
        
    #     return counts

    # use bitwise operations + dp
    def countBits(self, n: int) -> List[int]:
        """
        Returns an array 'counts' where counts[i] is the number of 1-bits in i.
        This uses a classic DP relation:
            counts[i] = counts[i >> 1] + (i & 1)
        which effectively says:
            - The number of set bits of i is the number of set bits of i//2
              plus 1 if i is odd (i.e., the least significant bit of i is 1).
        """
        counts = [0] * (n + 1)
        for i in range(1, n + 1):
            # shift i right by 1 (i // 2) and add the least significant bit (i & 1)
            counts[i] = counts[i >> 1] + (i & 1)
        return counts 
