class Solution(object):
    def generate(self, num_rows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #This solution is copy of leetcode solution.
        triangle = []
        
        for row_num in range(num_rows):
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1
            
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            
            triangle.append(row)
        return triangle
