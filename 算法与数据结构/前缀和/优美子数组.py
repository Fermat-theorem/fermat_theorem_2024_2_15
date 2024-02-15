'''
给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
请返回这个数组中 「优美子数组」 的数目。
eg.
输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
eg.
输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
'''
# class Solution:
#     def numberOfSubarrays(self, nums: list[int], k: int) -> int:
#         result_list = [-1]                  # todo:这里虚构了一个奇数在-1索引位置
#         for i, v in enumerate(nums):
#             if v % 2 != 0:
#                 result_list.append(i)
#         result_list.append(len(nums))
#         print(result_list)                  # todo:这里虚构了一个奇数在len(nums)索引位置
#
#         le = len(result_list)
#         if le < k:
#             return 0
#         elif le == k:
#             return 1
#         else:
#             i = 1
#             count = 0
#             while i + k < le:
#                 a = result_list[i] - result_list[i-1] - 1
#                 b = result_list[i+k] - result_list[i+k-1] - 1
#                 if a == -1:                 # todo:21行到24行其实可以省略，思考为什么
#                     a = 0
#                 if b == -1:
#                     b = 0
#                 count += (a+b)+a*b+1
#                 i += 1
#             return count

# ————————————————————————————————方法二————————————————————————————————#

# class Solution:
#     def numberOfSubarrays(self, nums: list[int], k: int) -> int:    # 官方解法，最快最省空间
#         cnt = [0] * (len(nums) + 1)
#         cnt[0] = 1
#         odd, ans = 0, 0
#         for num in nums:
#             if num % 2 == 1:
#                 odd += 1
#             if odd >= k:
#                 ans += cnt[odd - k]
#             cnt[odd] += 1
#         print(cnt)
#         return ans

# ——————————————————————————————方法三——————————————————————————————————#
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        result_dic = {0: 1}
        result = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                count += 1
            result_dic[count] = result_dic.get(count, 0) + 1
            if count >= k:
                result += result_dic.get(count-k, 0)

        return result


a = Solution()
b = a.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)
print(b)
