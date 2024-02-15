'''
给你一个下标从 0 开始且长度为 n 的整数数组 differences ，它表示一个长度为 n + 1 的 隐藏 数组 相邻 元素之间的 差值 。更正式的表述为：我们将隐藏数组记作 hidden ，那么 differences[i] = hidden[i + 1] - hidden[i] 。
同时给你两个整数 lower 和 upper ，它们表示隐藏数组中所有数字的值都在 闭 区间 [lower, upper] 之间。
比方说，differences = [1, -3, 4] ，lower = 1 ，upper = 6 ，那么隐藏数组是一个长度为 4 且所有值都在 1 和 6 （包含两者）之间的数组。
[3, 4, 1, 5] 和 [4, 5, 2, 6] 都是符合要求的隐藏数组。
[5, 6, 3, 7] 不符合要求，因为它包含大于 6 的元素。
[1, 2, 3, 4] 不符合要求，因为相邻元素的差值不符合给定数据。
请你返回符合要求的隐藏数组的数目。如果没有符合要求的隐藏数组，请返回0
eg.
输入：differences = [1,-3,4], lower = 1, upper = 6
输出：2
解释：符合要求的隐藏数组为：
- [3, 4, 1, 5]
- [4, 5, 2, 6]
所以返回2。
'''

class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        max_value = 0
        min_value = 0
        a = 0
        for i in differences:
            a += i
            if i >= 0:
                max_value = max(max_value, a)
            else:
                min_value = min(min_value, a)

        if max_value-min_value > upper-lower:
            return 0
        else:
            return (upper-lower) - (max_value-min_value) + 1