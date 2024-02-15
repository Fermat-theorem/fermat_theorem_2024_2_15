'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
eg.
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for c in range(m+1)]
        dp[0][1] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[j][i] = dp[j][i-1] + dp[j-1][i]
        return dp

# ————————————————方法二（优化空间复杂度）——————————————————  # todo:理解为何使用以为数组也可以达到目标？
                                                          # todo:因为每一次dp[j][i] = dp[j][i-1] + dp[j-1][i],我如果直接使用上面那一行，就可以不要dp[j-1][i]了
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]




a = Solution()
b = a.uniquePaths(3,7)
for i in range(4):
    print(b[i])