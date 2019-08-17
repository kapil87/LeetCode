def inorderIterative(tree):
    stack, result = [], []
    
    while stack or tree:
        if tree:
            stack.apppend(tree)
            #Go to the left subtree
            tree = tree.left
        else:
            #Go up in the tree
            tree = stack.pop()
            result.append(tree.data)
            #Go to the right subtree
            tree = tree.right
    return result

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Root, left, right
        if not root:
            return []
        treeElements = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            treeElements.append(curr.val)
            curr = curr.right
            
        return treeElements
        
