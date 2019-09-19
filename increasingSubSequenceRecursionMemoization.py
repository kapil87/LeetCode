class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
                
        def lengthofLIS(num, previndex, curpos, memo):
            
            if curpos == len(nums):
                return 0
            
            if memo[previndex + 1][curpos] >=0:
                return memo[previndex +1][curpos]
            
            taken = 0
            if previndex < 0 or (nums[curpos] > nums[previndex]):
                taken = 1 + lengthofLIS(nums, curpos, curpos+1, memo)
            
            nottaken = lengthofLIS(nums, previndex, curpos+1, memo)
            memo[previndex+1][curpos] = max(taken, nottaken)
            return memo[previndex +1][curpos]
        
        memo = [[-1 for i in range(len(nums))] for j in range(len(nums)+1)]
        return lengthofLIS(nums, -1, 0, memo)

        
