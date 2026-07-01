class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # isValid = True

        # check whether each row is valid or not
        for row in board:
            rowSet = set()
            for num in row:
                if num in rowSet and num != '.': 
                    # isValid = False
                    return False
                rowSet.add(num)
        
        # check each col
        for i in range(len(board)):
            colSet = set()
            for j in range(len(board)):
                if board[j][i] != '.' and board[j][i] in colSet:
                    # isValid = False
                    return False
                colSet.add(board[j][i])
        
        # check each 3 X 3 matrix
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subMatrixSet = set()
                for x in range(i,i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] != '.' and board[x][y] in subMatrixSet:
                            # isValid = False
                            return False
                        subMatrixSet.add(board[x][y])
        return True