# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #Simple inorder traversal solution with O(n) time and space
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        return inorder(root)[k-1]
