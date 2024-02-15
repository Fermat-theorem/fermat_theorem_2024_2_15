# 斐波那契数列
# class Solution:
#     def fib(self, n: int) -> int:
#         dp = [0,1]+[1]*(n-1)
#         print(dp)
#         if n in [0,1]:
#             return n
#         for i in range(2,n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[-1]


# a = Solution()
# print(a.fib(5))

# 解法二：
# 少去全备忘录的记载，而是每次只取相邻两次的加法的结果进行存储，节省空间
# class Solution:
#     def fib(self, n: int) -> int:
#         dp = [0,1]
#         print(dp)
#         if n in [0,1]:
#             return n
#         for i in range(2,n+1):
#             dp[0], dp[1] = dp[1], dp[0]+dp[1]
#         return dp[-1] % 1000000007
