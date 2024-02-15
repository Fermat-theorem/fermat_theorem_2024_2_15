'''
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。
eg.
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

# ——————————————————————————————写法一（超时）————————————————————————————————
# class Solution:
#     def combine(self, n: int, k: int) -> list[list[int]]:
#         nums = [i for i in range(1,n+1)]
#         result = []
#         choice = []
#         visit = []
#         def track(choice, nums):                                    # todo:该写法超时，请思考——没有利用有序数组的条件，做了重复判断
#             if len(choice) == k and set(choice) not in visit:       # 超时原因2，会进行组合的判断，[2,1] 和 [1,2]是一个组合，需要进行判断和记录
#                 visit.append(set(choice))
#                 result.append(list(choice))
#                 return
#             for c in nums:                        # 超时原因1，每次都会遍历nums，看选的数在不在choice里面
#                 if c in choice:
#                     continue
#                 choice.append(c)
#                 track(choice, nums)
#                 choice.remove(c)
#
#         track(choice, nums)
#         return result


# ——————————————————————————————————————写法二————————————————————————————————————————
# class Solution:
#     def combine(self, n: int, k: int) -> list[list[int]]:    # todo:这种写法更快，可以通过leecode，为什么？请思考
#         nums = [i for i in range(1, n+1)]                    # 这种写法，取消了上面写法的nums遍历，以索引为切入维度，取过的索引，后面没有再遍历
#         result = []                                          # 相当于剪枝，[4,3,2],取完后，一定不会再遍历前面的数，下一个一定是1，速度更快
#         choice = []
#
#         def track(choice, start):
#             i = k - len(choice)
#             if len(choice) == k:
#                 result.append(list(choice))
#                 return
#             for j in range(start, i-2, -1):           # todo：为什么这里是i-2，请重点思考！！
#                 choice.append(nums[j])                # i是个数，还需要多少个数，eg.i=3，则需要3个数，索引就要到i-1（2），range取数特点
#                 track(choice, j-1)                    # 反过来又要求能取到索引为i-1（2）时，就必须设置为i-2（1）
#                 choice.remove(nums[j])
#
#         track(choice, n-1)
#         return result

# ————————————————————————————写法三——————————————————————————————

# 正向索引写法
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:    # todo:这种写法更快，可以通过leecode，为什么？请思考
        nums = [i for i in range(1, n+1)]                    # 这种写法，取消了上面写法的nums遍历，以索引为切入维度，取过的索引，后面没有再遍历
        result = []                                          # 相当于剪枝，[4,3,2],取完后，一定不会再遍历前面的数，下一个一定是1，速度更快
        choice = []

        def track(choice, start):
            i = k - len(choice)
            if len(choice) == k:
                result.append(list(choice))
                return
            for j in range(start, n-i+1):           # todo：为什么这里是n-i+1，请重点思考！同写法二原因，边界条件
                choice.append(nums[j])
                track(choice, j+1)
                choice.remove(nums[j])

        track(choice, 0)
        return result

a = Solution()
b = a.combine(5, 3)
print(b)
