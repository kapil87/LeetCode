# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def _equals(s, t):
            if s == None and t == None:
                return True
            if s == None or t == None:
                return False
            print(s.val)
            return s.val == t.val and _equals(s.left, t.left) and _equals(s.right, t.right)
        
        def _traverse(s, t):
            return s!= None and (_equals(s,t) or _traverse(s.left, t) or _traverse(s.right, t))
        
        return _traverse(s,t)
                
