# Hard

# Topics
# premium lock icon
# Companies

# Hint
# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 

# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
# Example 2:

# Input: nums = [2,4,3,5,1]
# Output: 3
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -231 <= nums[i] <= 231 - 1



from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tmp = [0] * len(nums)

        def sort_count(l: int, r: int) -> int:
            if l >= r:
                return 0

            mid = (l + r) // 2
            count = sort_count(l, mid) + sort_count(mid + 1, r)

            # count cross pairs
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # merge two sorted halves into tmp
            i, j, k = l, mid + 1, l
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    tmp[k] = nums[i]
                    i += 1
                else:
                    tmp[k] = nums[j]
                    j += 1
                k += 1

            while i <= mid:
                tmp[k] = nums[i]
                i += 1
                k += 1
            while j <= r:
                tmp[k] = nums[j]
                j += 1
                k += 1

            # copy back
            nums[l:r+1] = tmp[l:r+1]
            return count

        return sort_count(0, len(nums) - 1)
