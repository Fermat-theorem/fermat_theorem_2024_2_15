'''
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
换句话说，s1 的排列之一是 s2 的 子串 。
eg.
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
eg.
输入：s1= "ab" s2 = "eidboaoo"
输出：false
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:   # todo:核心就是s1可以打乱顺序（任意排列），所以滑动区间or双指针只需要考虑s2里面的子串，通过比字母老匹配
        dic1 = {}
        dic2 = {}
        lenth1 = len(s1)
        if len(s1) > len(s2):
            return False
        for i in range(lenth1):
            dic1[s1[i]] = dic1.get(s1[i], 0) + 1
            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
        if dic1 == dic2:
            return True
        for end in range(lenth1, len(s2)):
            dic2[s2[end-lenth1]] = dic2.get(s2[end-lenth1], 0) - 1
            dic2[s2[end]] = dic2.get(s2[end], 0) + 1
            if dic2[s2[end-lenth1]] == 0:
                del dic2[s2[end-lenth1]]
            if dic1 == dic2:
                return True
        else:
            return False

a = Solution()
b = a.checkInclusion(s1="ab", s2="eidbaooo")
print(b)
