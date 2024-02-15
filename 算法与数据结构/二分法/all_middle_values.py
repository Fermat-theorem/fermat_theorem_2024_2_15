'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
eg.
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
'''
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        len_nums = len(nums)
        value_left = 0
        value_right = len_nums-1
        value_mid = len_nums//2

        while value_left <= value_right:
            if nums[value_mid] == target:
                value_index = value_mid
                break
            if nums[value_mid] > target:
                value_right = value_mid-1
                value_mid = (value_left + value_right)//2
            if nums[value_mid] < target:
                value_left = value_mid+1
                value_mid = (value_left + value_right)//2
        else:
            return [-1, -1]

        i, j = value_index, value_index
        while i >= 0 and nums[i] == target:    # todo:这里边界条件的范围一定要清楚，并且明白为什么放在前面！
            i -= 1                             # todo：因为python判断条件先判断and前面的，如果放后面，nums[i]放前面，可能出现索引超标的情况
        while j <= len_nums-1 and nums[j] == target:
            j += 1
        return [i+1, j-1]

a = Solution()
b = a.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
print(b)
