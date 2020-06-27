# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        
        result = []
        
        def countLonelyNodes(root):
            if not root:
                return 
            if root.left is None or root.right is None:
                if root.left is not None:
                    result.append(root.left.val)
                    countLonelyNodes(root.left)
                if root.right is not None:
                    result.append(root.right.val)
                    countLonelyNodes(root.right)
            else:
                countLonelyNodes(root.left)
                countLonelyNodes(root.right)
            
        
        countLonelyNodes(root)
        return result
