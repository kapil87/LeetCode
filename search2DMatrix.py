class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def search(matrix, rows, cols, target):
            """"""
            i = 0
            j = cols-1
            while(i < rows and j >=0 ):
                if (matrix[i][j] == target):
                    print (i, j, target)
                    return True
                if (matrix[i][j] > target):
                    j -=1
                else:
                    i +=1
            return False
        
        
        rows = len(matrix)
        if rows >=1:
            cols = len(matrix[0])
            return search(matrix, rows, cols, target)
        return False
