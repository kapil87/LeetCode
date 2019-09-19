class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def lengthOfLIS(nums, prev, curpos):
            if curpos == len(nums):
                return 0
            taken = 0
            if nums[curpos] > prev:
                taken = 1 + lengthOfLIS(nums, nums[curpos], curpos + 1)
            
            nottaken = lengthOfLIS(nums, prev, curpos+1)
            return max(taken, nottaken)
        
        min_ = -sys.maxsize-1
        return lengthOfLIS(nums, min_, 0)
