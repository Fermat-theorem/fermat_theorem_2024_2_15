'''
给定一个区间的集合 intervals,其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠.
eg.
输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
eg.
输入: intervals = [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
eg.
输入: intervals = [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
'''

# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         new_intervals = sorted(intervals, key=lambda x:(x[0],x[1]))         # todo:我的做法是以区间首段来区分，写法稍微会复杂点。
#                                                                                    其实这个题最关键的是尾段，所以以尾段排序反而
#                                                                                    会简单和快速一些，见下面做法
#         result = new_intervals[0]
#         count = 0
#         for i in range(1, len(new_intervals)):
#             m, n = result
#             x, y = new_intervals[i]
#             if x>=n:
#                 result = new_intervals[i]
#             elif y<=n:
#                 count += 1
#                 result = new_intervals[i]
#             else:
#                 count += 1
#         return count

class Solution:
    #再贪心贪一波
    #先按照区间end进行排序，维护一个指针遍历区间start，如果end比start小就end走起来(two pointers)
    #因此这里是数最多多少个不重叠区间(因此才是从小到大排序的)
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        end_pos = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):              # todo：尾段排序后，以区间首段来看，在前一个区间里面，就舍去，不在里面，则证明没有重叠
            if end_pos <= intervals[i][0]:
                end_pos = intervals[i][1]  #从这个局部看还能有多少个(局部再求一个最优)
                count += 1
        return len(intervals)-count