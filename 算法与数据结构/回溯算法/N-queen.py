# N皇后问题
'''
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
'''
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        board = [['.' for i in range(n)] for m in range(n)]                    # todo：列表的生成方式非常重要，建议重新审视
        row = 0

        def check(row, colum, board):
            rl, rr = row, row
            cl, cr = colum, colum
            for i in range(row):
                if board[i][colum] == 'Q':
                    return False
            while rl != 0 and cl != 0:
                rl -= 1
                cl -= 1
                if board[rl][cl] == 'Q':
                    return False
            while rr != 0 and cr != len(board) - 1:           # todo 边界条件重点关注
                rr -= 1
                cr += 1
                if board[rr][cr] == 'Q':
                    return False
            return True

        def backtrack(row, n):
            if row == n:
                result.append(["".join(i) for i in board])
                return

            for i in range(n):                          # todo 边界条件在重新审视
                if check(row, i, board):
                    board[row][i] = 'Q'
                    backtrack(row + 1, n)
                    board[row][i] = '.'

        backtrack(row, n)
        return result

a = Solution()
b = a.solveNQueens(4)
print(b)