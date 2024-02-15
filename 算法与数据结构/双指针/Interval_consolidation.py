'''
以数组intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间
并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
eg.
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
'''
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        start, end = intervals[0]

        for index in range(1, len(intervals)):
            i, j = intervals[index]
            if i <= end:
                end = max(end, j)
            else:
                result.append([start, end])
                start, end = i, j
        result.append([start, end])
        return result

# 方法二
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:   # todo: 方法二速度依然快，且空间少用1m，建议重新审视为什么！

#         if len(intervals) <2:
#             return intervals
#         area = sorted(intervals,key=lambda x:x[0])
#         ls = []
#         new = area[0]
#         for i in range(1,len(area)):
#             if area[i][0]>new[1]:
#                 ls.append(new)
#                 new = area[i]
#             else:
#                 new[1] = max(new[1],area[i][1])
#         ls.append(new)
#         return ls

a = Solution()
b = a.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
print(b)