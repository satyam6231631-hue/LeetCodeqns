class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def solve(row, col):

            if row == 9:
                return True

            if col == 9:
                return solve(row + 1, 0)

            if board[row][col] != '.':
                return solve(row, col + 1)

            box = (row // 3) * 3 + (col // 3)

            for num in '123456789':

                if num not in rows[row] and \
                   num not in cols[col] and \
                   num not in boxes[box]:

                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)

                    if solve(row, col + 1):
                        return True

                    board[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box].remove(num)

            return False

        solve(0, 0)