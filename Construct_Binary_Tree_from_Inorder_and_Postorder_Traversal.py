# Q2. Construct Binary Tree from Inorder and Postorder Traversal
# Solved
# Medium

# Topics
# premium lock icon
# Companies
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        idx = {v: i for i, v in enumerate(inorder)}  # O(1) lookup
        post_i = len(postorder) - 1                  # global pointer

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal post_i
            if in_left > in_right:
                return None

            root_val = postorder[post_i]
            post_i -= 1
            root = TreeNode(root_val)

            mid = idx[root_val]

            # must build right first
            root.right = helper(mid + 1, in_right)
            root.left = helper(in_left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)
