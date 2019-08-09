# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))
        def lca_helper(root, p, q):
            if not root:
                return Status(0, None)
            
            left_result = lca_helper(root.left, p, q)
            
            if left_result.num_target_nodes == 2:
                return left_result
            
            right_result = lca_helper(root.right, p, q)
            
            if right_result.num_target_nodes == 2:
                return right_result
            

            num_target_nodes = left_result.num_target_nodes + right_result.num_target_nodes + int(root in (p, q))
            
            return Status(num_target_nodes, root if num_target_nodes == 2 else None)
        
        return lca_helper(root, p, q).ancestor
    
