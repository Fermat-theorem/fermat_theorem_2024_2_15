# ————————————————————————————二分法———————————————————————————— #
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        len_nums = len(nums)
        if len_nums == 1 and nums[0] == target:
            return [0, 0]
        if len_nums == 1 and nums[0] != target:
            return [-1, -1]
        value_left = 0
        value_right = len_nums-1
        value_mid = (len_nums-1)//2

        while value_left <= value_right:
            if nums[value_mid] == target:
                value_index = value_mid
                break
            if nums[value_mid] > target:
                value_right = value_mid-1
                value_mid = (value_left + value_right)//2
            if nums[value_mid] < target:
                value_left = value_mid + 1
                value_mid = (value_left + value_right)//2
        else:
            return [-1, -1]

        i, j = value_index, value_index
        while i >= 0 and nums[i] == target:
            i -= 1
        while j <= len_nums-1 and nums[j] == target:
            j += 1
        return [i+1, j-1]
A = Solution()
A.searchRange([1,4], 4)
