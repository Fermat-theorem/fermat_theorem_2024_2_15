'''
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。
eg.
输入：nums = [1,1,1], k = 2
输出：2
eg.
输入：nums = [1,2,3], k = 3
输出：2
'''


# class Solution:
#     def maxScore(self, cardPoints: list[int], k: int) -> int:                 # todo:这个写法超出时间，因为每次都要计算区间内的sum
#         len_nums = len(cardPoints)
#         area = len_nums - k
#         print(area)
#         total_sum = sum(cardPoints)
#         print(total_sum)
#         if area == 0:
#             return total_sum
#         max_result = 0
#
#         i = 0
#         while (i + area - 1) != len_nums:
#             max_result = max(max_result, total_sum - sum(cardPoints[i:i + area]))
#             i += 1
#
#         return max_result

# ——————————————————————方法二——————————————————————————#

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        len_nums = len(cardPoints)
        area = len_nums - k
        if area == 0:
            return sum(cardPoints)
        i = 0
        cur_sum = sum(cardPoints[:i]) + sum(cardPoints[i+area:])
        max_result = cur_sum
        while (i + area) < len_nums:                                    # todo: 为什么不是i+area-1，请思考
            cur_sum = cur_sum + cardPoints[i] - cardPoints[i + area]    # todo: 为什么这里是i///i+area，请思考
            max_result = max(cur_sum, max_result)
            i += 1

        return max_result
a = Solution()
b = a.maxScore([1,79,80,1,1,1,200,1], 3)
print(b)