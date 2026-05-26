class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows
        values = set()
        for row in board:
            for cell in row:
                if cell in values and cell != ".":
                    return False
                values.add(cell)
                
            values = set()

        # check all columns 
        values = set()
        for col in range(len(board[0])):
            for row in range(len(board)):
                cell = board[row][col]
                if cell in values and cell != ".":
                    return False
                values.add(cell)
            values = set()

        # check all 3x3's
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                values = set()
                for i in range(3):
                    for j in range(3):
                        cell = board[box_row + i][box_col + j]
                        if cell in values and cell != ".":
                            return False
                        values.add(cell)

        return True
