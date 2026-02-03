# Q2. 3Sum Closest
# Solved
# Medium

# Topics
# premium lock icon
# Companies
# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        best = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                # update best if closer
                if abs(s - target) < abs(best - target):
                    best = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s  # exact hit

        return best
