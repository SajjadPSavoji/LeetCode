# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

# Example 1:


# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # or handle empty-tree scenario as needed

        # Use deque for efficient pops from the left
        queue = deque([(root, 1)])
        level_sums = {}

        # BFS
        while queue:
            node, level = queue.popleft()

            level_sums[level] = level_sums.get(level, 0) + node.val

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # Find the level with the maximum sum (and smallest level in a tie)
        # This could be done in one pass:
        max_sum = float('-inf')
        answer_level = 0
        for lvl, total in level_sums.items():
            if total > max_sum:
                max_sum = total
                answer_level = lvl
            elif total == max_sum and lvl < answer_level:
                # In case of tie, pick the smaller level
                answer_level = lvl

        return answer_level
