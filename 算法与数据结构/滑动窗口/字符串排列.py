"""
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
换句话说，s1 的排列之一是 s2 的 子串 。
eg.
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
eg.
输入：s1= "ab" s2 = "eidboaoo"
输出：false
"""

# ——————————————————————————————————方法一——————————————————————————————————————
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        needs = {}
        window = {}
        for i in s1:
            needs[i] = needs.get(i, 0) + 1
        while right < len(s2):
            j = s2[right]
            if j in needs:
                if window.get(j, 0) < needs[j]:  # todo：这里需要用到get函数，不然汇会报错，因为needs里有的，window不一定有
                    window[j] = window.get(j, 0) + 1
                    right += 1
                else:  # todo：else分支的含义是，如果我找到了重复的字母，left就移动，比如....a.....a....，我要去掉前面多的a，left就一直移动
                    window[s2[left]] -= 1
                    left += 1
            else:
                window = {}
                right += 1
                left = right
            if window == needs:  # todo:这个只能放在单次循环末尾，如果放前面，可能导致right+1后，跳出循环，此时还没进行比较（即要选中最后一个数）
                return True
        return False


# —————————————————————————————————————————方法二——————————————————————————————————————————————————

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        思路：怎么判断s2的字串和s1的排列之一相等，假如排序的话，遍历s2的同时，每次都排序，总的时间复杂度太高了。
        因此，我们采用一个有序字典来比较，由于只包含小写字母，我们采用数组来模拟有序字典，
        这样判断s2的子串和s1的排列之一相等就很容易了。总的时间复杂度为O(n),n为s2的长度。
        空间复杂度为:O(26)*2 == O(1)
        """
        m1 = len(s1)
        m2 = len(s2)
        if m1 > m2:
            return False
        dic1 = [0]*26
        dic2 = [0]*26
        for i in range(m1):
            dic1[ord(s1[i])-ord('a')] += 1
            dic2[ord(s2[i])-ord('a')] += 1
        if dic1 == dic2:
            return True

        for i in range(m1, m2):  # todo：核心在这里，全排列的字符串，长度一定想等！所以我从更长的m2往下走的时候，头要去，尾要加，操作一次比较一次
            dic2[ord(s2[i-m1])-ord('a')] -= 1
            dic2[ord(s2[i])-ord('a')] += 1
            if dic1 == dic2:
                return True
        return False

a = Solution()
b = a.checkInclusion("adc", "dcda")
print(b)


