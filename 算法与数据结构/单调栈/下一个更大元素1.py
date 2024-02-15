'''
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
eg.
输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1
'''
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        q = []
        right = 0
        result = [-1] * len(nums2)
        nums1_result = [-1] * len(nums1)

        while right < len(nums2):
            while q and nums2[q[-1]] < nums2[right]:  # todo:q里面存索引，维护一个单调栈的索引，更新对应的result（result——nums2）
                b = q.pop()
                result[b] = nums2[right]
            q.append(right)
            right += 1

        for i, c in enumerate(nums1):  # todo：将nums1里面的对应的元素找到在nums2里面的位置，然后根据nums2的索引，找到result里面的值，即为下一个更大值
            index = nums2.index(c)
            nums1_result[i] = result[index]

        return nums1_result

#——————————————————————————————————————方法二————————————————————————————————————————
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         dct = {_: -1 for _ in nums1}  # todo：把nums1字典话，hash提高查询速度
#         stk = []

#         for v in nums2:
#             while stk and stk[-1] < v:
#                 _ = stk.pop()
#                 if _ in dct:   # todo：这个就是方法一的for循环做的事，只是这里变成了字典，找到下一个更大值了，看下这个是不是在nums1里面，在的话就更新了
#                     dct[_] = v
#             stk.append(v)

#         return list(dct.values())