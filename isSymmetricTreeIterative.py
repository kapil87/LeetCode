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
        def isMirrorIterative(root):
            queue = []
            queue.append(root)
            queue.append(root)
            while queue:
                leftSubtree = queue.pop(0)
                rightSubtree = queue.pop(0)
                
                if leftSubtree == None and rightSubtree == None:
                    continue
                if leftSubtree == None or rightSubtree == None:
                    return False
                if leftSubtree.val != rightSubtree.val:
                    return False
                #Compare left subtree with right subtree
                queue.append(leftSubtree.left)
                queue.append(rightSubtree.right)
                #Compare right subtree with left subtree
                queue.append(leftSubtree.right)
                queue.append(rightSubtree.left)
                
            return True
                
        return isMirrorIterative(root)
        
        
