# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # bfs
        if not root:
            return []
        queue = [(root, 0)] # (node, level)
        answer = []
        
        while queue:
            node, level = queue.pop(0)
            if level >= len(answer):
                answer.append([])
            answer[level].append(node.val) # store visited node value
            
            # expand current node
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
                             
        return answe
