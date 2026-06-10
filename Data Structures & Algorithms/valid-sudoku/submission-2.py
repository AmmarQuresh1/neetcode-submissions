class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows
        values = set()
        for row in board:
            for cell in row:
                length = len(values)
                values.add(cell)
                if len(values) == length and cell != ".":
                    return False
            values = set()

        # check all columns 
        values = set()
        for col in range(len(board[0])):
            for row in range(len(board)):
                cell = board[row][col]
                length = len(values)
                values.add(cell)
                if len(values) == length and cell != ".":
                    return False
            values = set()

        # check all 3x3's
        values = set()
        row, col = 0, 0
        while row * col <= 64:
            cell = board[row][col]
            length = len(values)
            values.add(cell)
            if len(values) == length and cell != ".":
                return False
            col += 1
            if col % 3 == 0:
                col -= 3
                row += 1
                if col % 9 == 0:
                    col = 0
                elif row % 3 == 0:
                    row -= 3
                    col += 3
                    values = set()

        return True
