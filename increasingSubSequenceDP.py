class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Base case
        if len(nums) == 0:
            return 0
        #Prepare DP array
        dp = [0 for i in range(len(nums))]
        #1st element is always counted
        dp[0] = 1
        #So we have atelast max ans as 1, because of previous step
        maxans = 1
        #[10,9,2,5,3,7,101,18]
        for i in range(1, len(nums)):
            maxval = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            
            dp[i] = maxval +1
            maxans = max(maxans, dp[i])

        return maxans
