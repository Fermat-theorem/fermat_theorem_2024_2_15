'''
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
如果不存在满足条件的子数组，则返回 0
eg.
输入：nums = [8,2,4,7], limit = 4
输出：2
eg.
输入：nums = [10,1,2,4,7,2], limit = 5
输出：4
'''

from collections import deque


# ————————————————    方法一：暴力解  ————————————————————————
# class Solution:
#     def longestSubarray(self, nums: list[int], limit: int) -> int:
#         result = 0
#         for start in range(len(nums)):
#             end = start
#             max_value = max(nums[start:end + 1])
#             min_value = max(nums[start:end + 1])
#             while abs(max_value - min_value) <= limit and end < len(nums):
#                 result = max(end - start + 1, result)
#                 end += 1
#                 max_value = max(max_value, nums[:end + 1][-1])  # todo：这里为什么不直接nums[end]?因为第19行要求是end能够走到
#                 min_value = min(min_value, nums[:end + 1][-1])  # todo：最后一行，但是如果end能够取到最后的索引，则end+=1超边界
#         return result


# —————————————————————— 方法二：单调栈 ——————————————————————————
# class Solution:
#     def longestSubarray(self, nums: list[int], limit: int) -> int:
#         n = len(nums)
#         queMax, queMin = deque(), deque()
#         left = right = ret = 0
#
#         while right < n:
#             '''
#             我们仅需要统计当前窗口内的最大值与最小值(**重点理解**)，因此我们也可以分别使用两个单调队列解决本题。在实际代码中，我们使用一个单调递增的队列 queMin维护最小值
#             一个单调递减的队列 queMax维护最大值。这样我们只需要计算两个队列的队首的差值，即可知道当前窗口是否满足条件。
#             # 注意，我们维护的只是这个区间内的最大和最小值，如果有相同的，也需要放进双端队列进行维护
#             eg.
#             [1,2,3,10,10,10,3,2,1]
#             3个10均需要放进双端队列中，这样当第1个10需要移除时，队列中还有2个10，最大值还是可以选中，这也是47//49行不涉及相等符号的情况
#             '''
#             while queMax and queMax[-1] < nums[right]:
#                 queMax.pop()
#             while queMin and queMin[-1] > nums[right]:
#                 queMin.pop()
#             queMax.append(nums[right])
#             queMin.append(nums[right])
#
#             while queMax and queMin and queMax[0] - queMin[0] > limit:
#                 if nums[left] == queMin[0]:
#                     queMin.popleft()
#                 if nums[left] == queMax[0]:
#                     queMax.popleft()
#                 left += 1                       # 如果是nums的left，在双端队列的开头，则移除进行比较，反正left+=1了
#                                                 # 如果不在，也没关系，我只是比较nums某一区间的最大最小，反正我left移动了，直到nums
#                                                 # 的这个区间，的最大最小值的差值，小于我的limit todo：重点是要区分移除的，和我要比较的，是两个队列nums//s
                                                  # 并且，在left指针之前的值，都已经被pop出去了，整个队列里面只有[left,right+1]里面的值
#             ret = max(ret, right - left + 1)
#             right += 1
#         return ret
#
#
# # ————————————————————————————————————方法三：有序数据结构加滑动区间————————————————————————————————————————————————
# class Solution:
#     def longestSubarray(self, nums: list[int], limit: int) -> int:
#         from sortedcontainers import SortedList  # todo: 为了方便统计当前窗口内的最大值与最小值，我们可以使用平衡树
#                                                  # todo：sortedcontainers这个是第三方库，这个库的底层实现并不是平衡树，但各种操作的时间复杂度仍然很优秀
#                                                  # todo: 尝试使用堆结构看能否实现该功能，答案是不能，见方法五，堆排序并不是严格单调，只是完全二叉树
#                                                  # todo: 堆其实也可以实现，参考我的方法6，2023.4.27还是不行，见方法六分析
#         s = SortedList()
#         left, right = 0, 0
#         res = 0
#         while right < len(nums):
#             s.add(nums[right])
#             print(s)
#             while s[-1] - s[0] > limit:
#                 s.remove(nums[left])             # todo:用pop为什么不行？非常经典，因为你新添加的数，不一定就是最大的在右边，有可能是在排序后的最左边
#                 # todo:但是我们要踢出来的，是原数组的最左边的数，所以是nums的left索引的数，不是s的,所以不能s.pop(0)
#                 # todo:接上，考虑极端情况 nums:mid,mid,mid,max,min   s:min,mid,mid,mid,max   应该弹出的是mid，最后nums剩max,min。s剩min，max
#                 left += 1
#             res = max(res, right - left + 1)
#             right += 1
#         return res


# ———————————————————————————————方法四 二分排序算法实现 ————————————————————————————————————
# class Solution:
#     def longestSubarray(self, nums: list[int], limit: int) -> int:
#
#         import bisect
#         s = []
#         left, right = 0, 0
#         res = 0
#         while right < len(nums):
#             bisect.insort(s, nums[right])       # todo: 用二分插入，58/61，如果用s.append()+ s.sort()，为56/61，暴力解为55/61
#             while s[-1] - s[0] > limit:
#                 s.remove(nums[left])
#                 left += 1
#             res = max(res, right - left + 1)
#             right += 1
#         return res

# ———————————————————————————————方法五 小顶堆之为什么不可以实现 ———————————————————————————————————— todo:为什么不能实现
# class Solution:
#     def longestSubarray(self, nums: list[int], limit: int) -> int:
#
#         import heapq
#         s = []
#         left, right = 0, 0
#         res = 0
#         while right < len(nums):
#             heapq.heappush(s, nums[right])
#             while s[-1] - s[0] > limit:
#                 heapq.heappop(s)
#                 left += 1
#             res = max(res, right - left + 1)
#             right += 1
#         return res


# ————————————————————————————————————————方法六————————————————————————————————————————————
# class Solution:
#     def longestSubarray(self, nums: list[int], limit: int) -> int:
#         import heapq
#
#         s = []
#         left, right = 0, 0
#         res = 0
#         heapq.heapify(s)
#         while right < len(nums):
#             heapq.heappush(s, (nums[right], right))
#             while s[-1][0] - s[0][0] > limit:
#                 if nums[left] != s[0][0]:
#                     left += 1
#                 else:
#                     heapq.heappop(s)
#                     left += 1
#             while s[0][1] < left        # todo：堆维护的是一个连续的字串，pop出的可能是连续字串的任何一个，（前5个数可能是[3，1，4，5，2]，pop出的3）导致结构破坏
#                                         # todo：方法三的s.remove()，就是用sortedlist逐项把nums[left]移除，但是堆的pop只能弹出堆顶元素，哪怕排序也不行(nums[right], right)
#             res = max(res, right - left + 1)
#             right += 1
#         return res

# a = Solution()
# b = a.longestSubarray([4,2,2,2,4,4,2,2], 0)
# print(b)

import heapq

a = [7,5,4,3,2,6,1,]   # todo:因为小顶堆实现的是完全二叉树，根节点最小，不代表严格有序，参考这段程序的输出
heapq.heapify(a)
print(a)

