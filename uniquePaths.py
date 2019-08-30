class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*n]*m
        
        for row in range(len(dp)):
            dp[row][0] = 1
        
        for col in range(len(dp[0])):
            dp[0][col] = 1
        
        for row in range(1, len(dp)):
            for col in range(1, len(dp[row])):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[m-1][n-1]
        
