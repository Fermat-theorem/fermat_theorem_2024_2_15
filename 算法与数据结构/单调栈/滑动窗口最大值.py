# area = 3.1415925
# s = area
# ss = area**2
# print(r"梵蒂冈的经纬度坐标精度：{{{1:.4f}, {0:.10f}}}".format(s, ss))  # todo:format方法，需要显示大括号时，需要“转译”，加符号“{”,所以前面是三个大括号，最外层是转译时
# print(r"这是一个format方法的示例{1:.2f}，{0:.5f}".format(s, ss))

'''
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值
eg.
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
eg.
输入：nums = [1], k = 1
输出：[1]
'''
# todo: 该方法超时 37/51
# class Solution:
#     def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#         import bisect
#         right = k - 1
#         left = 0
#         que_max = nums[:right+1]
#         que_max.sort()
#         result = [que_max[-1]]
#         while right < len(nums):
#             right += 1
#             bisect.insort(que_max, nums[right])
#             que_max.remove(nums[left])
#             result.append(que_max[-1])
#             left += 1
#         return result

# class Solution:
#     def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#         from collections import deque
#         que_max = deque()
#
#         left, right = 0, 0
#         result = []
#
#         while right < len(nums):
#             '''
#             # 注意，我们维护的只是这个区间内的最大和最小值，如果有相同的，也需要放进双端队列进行维护
#             eg.[1,2,3,10,10,10,3,2,1]
#             3个10均需要放进双端队列中，这样当第1个10需要移除时，队列中还有2个10，最大值还是可以选中，这也是57行只是<的情况，而不是<=
#             '''
#             while que_max and que_max[-1] < nums[right]:    # todo：重点理解为什么是<,而不是<=,这样就可以不用pop，而把后续的相等的最大值放入队列（59行）
#                 que_max.pop()
#             que_max.append(nums[right])
#
#             if right-left+1 == k:
#                 result.append(que_max[0])
#
#             if right-left+1 > k:
#                 if nums[left] == que_max[0]:
#                     que_max.popleft()
#                 result.append(que_max[0])
#                 left += 1
#
#             right += 1
#
#         return result

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        import heapq
        n = len(nums)
        # 注意 Python 默认的优先队列是小顶堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:    # todo：确保了最大值的index一直在[i-k+1, i],不在的话，就会被pop出去。这里也可以写成while q[0][1] < i-k+1,要区分索引差与切片长度的关系
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans



a = Solution()
b = a.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5)
print(b)







            





