# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Recursive solution for Problem 226
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        #print root.val
        root.left = right
        root.right = left
        return root
