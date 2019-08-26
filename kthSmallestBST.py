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
        '''
        #Simple inorder traversal solution with O(n) time and space
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        return inorder(root)[k-1]
        '''
        #Simple iterative solution with O(h+k) where we keep the h+k nodes in the stack. In worst case wen have O(n) time complexity 
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -=1
            if not k:
                return root.val
            root = root.right
