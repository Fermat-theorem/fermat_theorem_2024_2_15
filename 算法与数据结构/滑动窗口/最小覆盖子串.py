'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：
对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
eg.
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'
eg.
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
'''
# ——————————————————————————————————方法一————————————————————————————————————————#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_dic = {}
        window_dic = {}
        left, right = 0, 0
        min_value = ''
        for alp in t:
            need_dic[alp] = need_dic.get(alp, 0) + 1

        def check(dic1, dic2):     # todo：这个方法使用函数判断，速度上会稍逊方法二
            for key in dic2:
                if key not in dic1 or dic1[key] < dic2[key]:
                    break
            else:
                return True
            return False

        while right < len(s):
            c = s[right]
            if c in need_dic:
                window_dic[c] = window_dic.get(c, 0) + 1
                while check(window_dic, need_dic):
                    if min_value:
                        min_value = min(min_value, s[left:right+1], key=len)
                    else:
                        min_value = s[left:right+1]
                    d = s[left]
                    if d in need_dic:
                        window_dic[d] = window_dic.get(d) - 1
                    left += 1
                right += 1
            else:
                right += 1

        return min_value

# ————————————————————————————————————方法二——————————————————————————————————#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        window, need = defaultdict(int), defaultdict(int)
        for c in t:
            need[c] += 1

        slow, fast = 0, 0
        valid = 0
        start, length = 0, float('inf')
        while fast < len(s):
            c = s[fast]

            # 窗口内更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:  # todo：只判断相同键的值是否相等，多了少了都不会+1，important！
                    valid += 1
            # 缩小窗口
            while valid == len(need):  # 是len(need)不是len(t)，因为t中可能会有重复元素
                if fast - slow + 1 < length:   # todo：变量值保存开始索引和长度，不断比较两个指针的长度，我的方法就慢在这里，你都双指针了，还有必要搞那个min函数吗？
                    start = slow  # todo：是为了最后返回数组，这个相当于数组的起点，然后有了数组长度，则可以返回最后真实的最小长度的子串
                    length = fast - slow + 1
                d = s[slow]
                slow += 1
                if d in need:
                    if window[d] == need[d]:  # todo：只判断相同键的值是否还是大于，一旦等于了，你左移left指针，那么valid就必须要-1了，大于的话就证明还可以减少
                        valid -= 1
                    window[d] -= 1
            fast += 1

        return '' if length == float('inf') else s[start: start + length]


a = Solution()
b = a.minWindow("ADOBECODEBANC", "ABC")
print(b)



