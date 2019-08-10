class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Base case when nums array is empty
        if not nums:
            return 0
        #Create DP array to hold sum at each index
        dp = [0]*len(nums)
        dp[0] = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            #Get sum either by including next value or not including it in contiguous array
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            #Keep track of max so far
            result = max(result, dp[i])
        return result
        
