# 全排列问题
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        trace = []
        amount = len(nums)
        result = []
        def traceback(nums,trace):
            if len(trace) == amount:
                result.append(list(trace))             # todo: 这里的list，非常非常重要
                return
            for i in range(amount):
                if nums[i] in trace:                   # todo：这种写法错误，因为比如数据列表为【1，2，3，1】，本身就会有重复值，无法全排列
                    continue                           # todo：建议把路径中的格式规定为值+索引，路径满足后，转换为result，见回溯算法24点解析
                trace.append(nums[i])
                traceback(nums, trace)
                trace.remove(nums[i])
        traceback(nums, trace)
        return result
a = Solution()
b = a.permute([1, 2, 3, 1])
print(len(b))