# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.convert(nums, 0, len(nums))
    
    def convert(self, nums, left, right):
        if left >=right:
            return 
        mid = left + (right-left)/2
        node = TreeNode(nums[mid])
        node.left = self.convert(nums, left, mid)
        node.right = self.convert(nums, mid+1, right)
        return node
