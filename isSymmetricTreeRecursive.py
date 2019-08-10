# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(leftSubtree, rightSubtree):
            #base case or when we are at leaf nodes
            if leftSubtree == None and rightSubtree == None:
                return True
            #When tree is unequal 
            if leftSubtree == None or rightSubtree == None:
                return False
            
            return ((leftSubtree.val == rightSubtree.val) #Check current root value
        and isMirror(leftSubtree.left, rightSubtree.right) #Check left subtree's left is equal to right subtress's right 
        and isMirror(leftSubtree.right, rightSubtree.left)) #Check left subtree's right is equal to right subtree's left
        
        return isMirror(root, root)
