import collections


class Solution:
    def isValidSudoku(self, board: list[list[str]], type=0) -> bool:
        """Determine if a 9 x 9 Sudoku board is valid. Only the filled cells
        need to be validated according to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain
        the digits 1-9 without repetition.

                Args:
                    board (list[list[str]]): _description_

                Returns:
                    bool: _description_
        """
        valid_digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        valid_digits_static = frozenset(valid_digits)
        length = len(board)
        if type == 0:
            # neetcode
            cols = collections.defaultdict(set)
            rows = collections.defaultdict(set)
            squares = collections.defaultdict(set)  # key = (r /3, c /3)

            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        continue
                    if (
                        board[r][c] in rows[r]
                        or board[r][c] in cols[c]
                        or board[r][c] in squares[(r // 3, c // 3)]
                    ):
                        return False
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[(r // 3, c // 3)].add(board[r][c])

            return True
        else:

            def row_check():
                for r in range(length):
                    count = set()
                    for c in range(length):
                        if board[r][c] == ".":
                            continue
                        elif board[r][c] in valid_digits_static:
                            if board[r][c] not in count:
                                count.add(board[r][c])
                            else:
                                return False
                        else:
                            return False
                return True

            def col_check():
                for c in range(length):
                    count = set()
                    for r in range(length):
                        if board[r][c] == ".":
                            continue
                        elif board[r][c] in valid_digits_static:
                            if board[r][c] not in count:
                                count.add(board[r][c])
                            else:
                                return False
                        else:
                            return False
                return True

            def mini_board_check():
                for k in [0, 3, 6]:
                    count = set()
                    for r in range(3):
                        for c in range(3):
                            if board[r + k][c + k] == ".":
                                continue
                            elif board[r + k][c + k] in valid_digits_static:
                                if board[r + k][c + k] not in count:
                                    count.add(board[r + k][c + k])
                                else:
                                    return False
                            else:
                                return False
                return True

            R = row_check()
            C = col_check()
            M = mini_board_check()
            return R and C and M


if __name__ == "__main__":
    s = Solution()
    assert (
        s.isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
        is True
    )
    assert (
        s.isValidSudoku(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
        is False
    )
    assert (
        s.isValidSudoku(
            [
                [".", ".", ".", ".", "5", ".", ".", "1", "."],
                [".", "4", ".", "3", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                [".", ".", "2", ".", "7", ".", ".", ".", "."],
                [".", "1", "5", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", "2", ".", ".", "."],
                [".", "2", ".", "9", ".", ".", ".", ".", "."],
                [".", ".", "4", ".", ".", ".", ".", ".", "."],
            ]
        )
        is False
    )
