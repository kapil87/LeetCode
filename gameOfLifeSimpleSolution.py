class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def getNeighbors (borad, row, col):
            """Get neighbors for a row,col """
            top, bottom, left, right = 0, 0, 0, 0
            top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0 
            rows = len(board)
            colums = len(board[row])
            
            #Top cell
            if row-1 >= 0:
                top = board[row-1][col]
                #print 'top', top
            #Top Left cell
            if row-1 >= 0 and col-1 >= 0:
                top_left = board[row-1][col-1]
                #print 'top_left', top_left
            #Top Right cell
            if row-1 >= 0 and col+1 < colums:
                top_right = board[row-1][col+1]
                #print 'top_right', top_right
            #Left cell
            if col-1 >= 0:
                left = board[row][col-1]
                #print 'left', left
            #Right cell
            if col+1 < colums:
                right = board[row][col+1]
                #print 'right', right
            #Bottom cell
            if row+1 < rows:
                bottom = board[row+1][col]
                #print 'bottom', bottom
            #Bottom Left cell
            if row +1 < rows and col-1 >=0:
                bottom_left = board[row+1][col-1]
                #print 'bottom_left', bottom_left
            #Bottom Right cell
            if row+1 < rows and col+1 < colums:
                bottom_right = board[row+1][col+1]
                #print 'bottom_right',bottom_right
            
            neighbors = top+bottom+left+right+top_left+top_right+bottom_left+bottom_right
            return neighbors
        
        updated_board = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                neighbors = getNeighbors(board, row, col)
                #print 'neighbors for [%s, %s] are [%s]'%(row, col, neighbors)
                if neighbors < 2:
                    updated_board[row][col] = 0
                if board[row][col] == 1 and (neighbors == 2 or neighbors == 3):
                    updated_board[row][col] = 1
                if neighbors > 3:
                    updated_board[row][col] = 0
                if board[row][col] == 0 and neighbors ==3:
                    updated_board[row][col] = 1

            #print updated_board
        
        for row in range(len(updated_board)):
            for col in range(len(board[row])):
                board[row][col] = updated_board[row][col]
                
        
                    
