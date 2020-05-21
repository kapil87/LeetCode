class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.board = [[None for _ in range(0, n) ] for _ in range(0, n)]
        self.playerSymbols = {
            1: 'X',
            2: '0'
        }

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        def _isValidMove(row, col):
            return self.board[row][col] == None
        
        def _whoIsWinner(_player):
            def _check_rows(_player):
                for row in self.board:
                    if row.count('None') > 0:
                        return False
                    elif all([ele == self.playerSymbols[_player] for ele in row]):                   return True
                return False
            def _check_cols(_player):
                for c in range(0, self.n):
                    col = []
                    for r in range(0, self.n):
                        col.append(self.board[r][c])
                    if col.count('None') > 0:
                        return False
                    elif all([ele == self.playerSymbols[_player] for ele in col]):
                        return True
                return False
                    
            def _check_diagonals(_player):
                left_to_right_diagonal = []
                for r in range(0, self.n):
                    for c in range(0, self.n):
                        if r == c:
                            left_to_right_diagonal.append(self.board[r][c])
                right_to_left_diagonal = []
                for r in range(0, self.n):
                    for c in range(0, self.n):
                        if r == c:
                            reverse_col = copy.deepcopy(self.board[r])
                            reverse_col = reverse_col[::-1]
                            right_to_left_diagonal.append(reverse_col[c])
            
                if left_to_right_diagonal.count('None') > 0 or right_to_left_diagonal.count('None') > 0:
                    return False
                return all([ele == self.playerSymbols[_player] for ele in left_to_right_diagonal]) or all([ele == self.playerSymbols[_player] for ele in right_to_left_diagonal])
                
                
            if _check_rows(_player) or _check_cols(_player) or _check_diagonals(_player):
                return _player
            return 0
        
        if _isValidMove(row, col):
            self.board[row][col] = self.playerSymbols[player]

        return _whoIsWinner(player)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
