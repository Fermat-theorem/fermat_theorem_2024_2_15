'''
DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
例如，"ACGAATTCCG" 是一个 DNA序列 。
在研究 DNA 时，识别 DNA 中的重复序列非常有用。
给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。
eg.
输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]
eg.
输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]
'''


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        i = 0
        result_dict = {}
        while i + 10 - 1 < len(s):
            area = s[i:i + 10]
            result_dict[area] = result_dict.get(area, 0) + 1
            i += 1

        result = [key for key in result_dict if result_dict[key] != 1]
        return result

# ————————————————方法二————————————————————

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:       # todo 结合方法实现，用一个集合存储字典内重复出现的字符串，然后返回
        i = 0
        result_dict = {}
        result = set()
        while i+10-1 < len(s):
            area = s[i:i+10]
            result_dict[area] = result_dict.get(area, 0) + 1
            if result_dict[area] != 1:
                result.add(area)
            i += 1

        # result = [key for key in result_dict if result_dict[key] != 1]
        return list(result)