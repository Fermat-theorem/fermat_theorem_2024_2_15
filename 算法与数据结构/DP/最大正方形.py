'''
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
eg.
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
'''
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        max_value = 0

        def check(lf, lfup, up):
            return min(lf, lfup, up) + 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[i+1][j+1] = 0
                    continue
                else:
                    dp[i+1][j+1] = check(dp[i+1][j], dp[i][j], dp[i][j+1])
                    max_value = max(max_value, dp[i+1][j+1])
        return max_value

a = Solution()
b = a.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(b**2)
                    