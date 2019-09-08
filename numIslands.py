class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j):
            """This will set all the 1's in horizontal or vertial direction to 0 which are neighbors"""
            if (i <0 or i >= len(grid) or j <0 or j >= len(grid[i]) or grid[i][j] == '0'):
                return 0
            
            grid[i][j] = '0'
            dfs(grid, i-1, j)
            dfs(grid, i+1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)
            return 1
        
        if grid == None or len(grid) == 0:
            return 0
        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islands += dfs(grid, i, j)
        
        return islands
        
