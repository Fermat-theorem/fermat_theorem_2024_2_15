"""
给定两个字符串 和 ，找到 中所有 的 异位词 的子串，返回这些子串 的起始索引。不考虑答案输出的顺序。spsp
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
eg.
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        from collections import defaultdict

        result = []
        lengh = len(p)
        valid, left, right = 0, 0, 0
        needs, window = defaultdict(int), defaultdict(int)
        for i in p:
            needs[i] += 1
        while right < len(s):
            j = s[right]
            right += 1
            if j in needs:
                window[j] += 1
                if window[j] == needs[j]:
                    valid += 1

            while right-left >= lengh:
                if valid == len(needs):
                    result.append(left)
                m = s[left]
                left += 1
                if m in window:  # todo: 这个分支有个隐含的错误，就是left的移动带来了多个重复字母的去除，可能导致valid的计数，多次减少，、、
                    window[m] -= 1  # todo: 比如...a....a.....a.....left...，left走过重复字母，后面的window[a]都更小，导致valid不对
                    if window[m] < needs[m]:
                        valid -= 1
        return result


# 改进以后的做法：
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        from collections import defaultdict
        result = []
        lengh = len(p)
        valid, left, right = 0, 0, 0
        needs, window = defaultdict(int), defaultdict(int)
        for i in p:
            needs[i] += 1
        while right < len(s):
            j = s[right]
            right += 1
            if j in needs:
                window[j] += 1
                if window[j] == needs[j]:
                    valid += 1

            while right-left >= lengh:
                if valid == len(needs):
                    result.append(left)
                m = s[left]
                left += 1
                if m in window:
                    if window[m] == needs[m]:
                        valid -= 1
                    window[m] -= 1
        return result
