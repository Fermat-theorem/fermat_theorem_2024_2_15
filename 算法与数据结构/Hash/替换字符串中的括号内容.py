'''
给你一个字符串 s ，它包含一些括号对，每个括号中包含一个 非空 的键。
比方说，字符串 "(name)is(age)yearsold" 中，有 两个 括号对，分别包含键 "name" 和 "age" 。
你知道许多键对应的值，这些关系由二维字符串数组 knowledge 表示，其中 knowledge[i] = [keyi, valuei] ，表示键 keyi 对应的值为 valuei 。
你需要替换 所有 的括号对。当你替换一个括号对，且它包含的键为 keyi 时，你需要：
将 keyi 和括号用对应的值 valuei 替换。
如果从 knowledge 中无法得知某个键对应的值，你需要将 keyi 和括号用问号 "?" 替换（不需要引号）。
knowledge 中每个键最多只会出现一次。s 中不会有嵌套的括号。
请你返回替换 所有 括号对后的结果字符串。
eg.
输入：s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
输出："bobistwoyearsold"
解释：
键 "name" 对应的值为 "bob" ，所以将 "(name)" 替换为 "bob" 。
键 "age" 对应的值为 "two" ，所以将 "(age)" 替换为 "two" 。
eg.
输入：s = "hi(name)", knowledge = [["a","b"]]
输出："hi?"
解释：由于不知道键 "name" 对应的值，所以用 "?" 替换 "(name)" 。
'''
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dic_know = {}
        result = []
        word = []
        for i in knowledge:
            dic_know[i[0]] = i[1]
        flag = 0
        for alp in s:
            if alp == '(':
                flag = 1
                continue
            elif alp == ')':
                flag = 0
                result.append(dic_know.get(''.join(word), '?'))
                word = []
                continue
            if flag:
                word.append(alp)
            else:
                result.append(alp)
        return ''.join(result)

# ——————————————————————————————————————方法二————————————————————————————————————————
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans = []
        knows = {k: v for k, v in knowledge}      # todo:列表拆包
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i + 1)            # todo:用字符串的find函数，找到右边的界限，再把左右界限中的键取出来匹配，在把i放到j的位置，双指针
                ans.append(knows.get(s[i + 1:j], '?'))
                i = j
            else:
                ans.append(s[i])
            i += 1

        return ''.join(ans)



a = Solution()
b = a.evaluate(s="(name)is(age)yearsold", knowledge=[["name","bob"],["age","two"]])
print(b)