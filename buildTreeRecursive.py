# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == [] or inorder == []:
            return None
        
        root = TreeNode(preorder.pop(0))
        rootIdx = inorder.index(root.val)
        left = inorder[:rootIdx]
        right = inorder[rootIdx+1:]
        root.left = self.buildTree(preorder, left)
        root.right = self.buildTree(preorder, right)
        return root
    
