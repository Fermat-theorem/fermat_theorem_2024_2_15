class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        nums_len = len(nums)
        result_dict = {0: 1}                  # todo
        result_sum = 0
        if nums_len == 1 and nums[0] == k:
            return 1
        for i in range(nums_len):
            result_sum += nums[i]

            count += result_dict.get(result_sum - k, 0)                  # todo
            result_dict[result_sum] = result_dict.get(result_sum, 0) + 1

        return count

a = Solution()
b = a.subarraySum([1,1,1],2)
print(b)
