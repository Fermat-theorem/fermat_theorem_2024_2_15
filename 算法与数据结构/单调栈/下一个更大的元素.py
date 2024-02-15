'''
给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。
eg.
输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
eg.
输入: nums = [1,2,3,4,3]
输出: [2,3,4,-1,4]
'''
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n  # todo：全部取为-1，是因为result的赋值，是后面比前面大才赋值，是一个单调栈，其余未赋值的，就当他是-1，因为没找到，至于为什么可以这样写，见方法一解析
        index_list = []

        for i in range(n*2-1):
            while index_list and nums[index_list[-1]] < nums[i % n]:
                result[index_list[-1]] = nums[i % n]
                index_list.pop()
            index_list.append(i % n)

        return result

# todo：为什么可以用单调栈这样写，是因为只可能出现...9,8,7,6...这种单调递减形式，如果出现了...9,8,7,6...10这种情况，那么10就会变成6789共有的最先出现的大于值（栈一次弹出，result依次更新）
# todo：如果出现..9,8,..10..7,6..这种情况，那么创建单调栈的过程中，10就会变成8和9的最大值，导致8和9被pop出去并更新result（以索引方式），这是index的队列的————值就变为了..10..7..6..
# todo：如果后面碰到比10大的，继续重复上述流程。如果碰不到？没关系，这些位置不用更新，早已变成-1，证明没找到后面比他大的值

# ————————————————————————————————————————方法二————————————————————————————————————————————
# class Solution:
#     def nextGreaterElements(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         result = [-1] * n
#         index_list = []
#
#         for i in range(n*2-1):
#             while index_list and nums[index_list[-1]] < nums[i % n]:
#                 t = index_list.pop()   # todo：另一种写法，方法二对比方法一，反正你都取得索引列表的最后一个，取了以后还弹出了，那我先弹出赋值t，在放在result索引里面
#                 result[t] = nums[i % n]
#
#             index_list.append(i % n)
#         return result



