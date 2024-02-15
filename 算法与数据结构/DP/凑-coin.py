'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。
eg.
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
'''
# 暴力解法，迭代法
# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:
#         def dp(n):
#             if n == 0:
#                 return 0
#             if n < 0:
#                 return -1
#             res = float("INF")                            # todo：为什么取这个值？请结合代码逻辑复习
#             for coin in coins:
#                 subcoin = dp(n - coin)
#                 if subcoin == -1:
#                     continue
#                 res = min(res, 1 + subcoin)
#             return res if res != float("INF") else -1
#         return dp(amount)

# 解法二：备忘录+递归
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        note = {}
        def dp(n):
            if n in note:                        # todo：每进入新的一层函数，都会判断之前是否到过这一层，df(n)的意思是，剩n块钱金额时，最少需要多少个硬币
                return note[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float("INF")
            for coin in coins:
                subcoin = dp(n - coin)   # 自顶向下，从金额amount开始
                if subcoin == -1:
                    continue
                res = min(res, 1 + subcoin)
            note[n] = res if res != float("INF") else -1        # todo:在这一层，将df(n)产生的最小值记录在字典内，后面碰到可直接调用
            return note[n]
        return dp(amount)

# 解法三：动态规划
class Solution:
    def coinChange(self, coins: list[int], amount: int):
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i-coin<0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])
        print(dp)
        return dp[-1] if dp[-1] != amount+1 else -1
a = Solution()
b = a.coinChange([1, 2], 2)
print(b)