'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
eg.
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
eg.
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
'''

# ——————————————————————————————递归写法————————————————————————————————
# class Solution:
#     def climbStairs(self, n: int) -> int:
#
#         def f(index):
#             if index == 1:
#                 return 1
#             elif index == 2:
#                 return 2
#             else:
#                 return f(index-2) + f(index-1)
#         return f(n)

# ————————————————————————— —动态规划————————————————————————————————
# class Solution:
#     def climbStairs(self, n: int) -> int:
        # dp = [1] * (n + 2)
        # dp[0] = 0
        # for i in range(n):
        #     dp[i+2] = dp[i+1] + dp[i]
        # print(dp)
        # return dp[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            c = a+b
            a = b
            b = c
        return b

a = Solution()
b = a.climbStairs(3)
