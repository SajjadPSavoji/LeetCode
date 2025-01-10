# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def attach(self, parent, cur, nxt):
        """
        Attaches the 'nxt' node as a child of 'parent' based on the value of 'cur'.
        """
        if parent.val > cur.val:
            parent.left = nxt
        else:
            parent.right = nxt

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes a node with the given key from the binary search tree and returns the new root.
        """
        if root is None:
            return root

        # Create a dummy parent to handle deletion of the root node
        dummy_parent = TreeNode(root.val + 1, root, None)
        parent = dummy_parent
        current = root

        # Traverse the tree to find the node to delete
        while current is not None and current.val != key:
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right

        # If the key is not found, return the original tree
        if current is None:
            return dummy_parent.left

        # Nodes to attach after deletion
        left_subtree = current.left
        right_subtree = current.right

        # Case 1: Node has no left child
        if left_subtree is None:
            self.attach(parent, current, right_subtree)
        
        # Case 2: Node has no right child
        elif right_subtree is None:
            self.attach(parent, current, left_subtree)
        
        # Case 3: Node has both children
        else:
            self.attach(parent, current, right_subtree)
            # Find the leftmost node in the right subtree
            successor = right_subtree
            while successor.left is not None:
                successor = successor.left
            # Attach the left subtree to the successor
            successor.left = left_subtree

        # Return the new root of the tree
        return dummy_parent.left
