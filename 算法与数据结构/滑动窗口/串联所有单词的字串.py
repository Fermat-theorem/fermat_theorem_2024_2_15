# class Solution:
#     def findSubstring(self, s: str, words: list[str]) -> list[int]:      # todo：该方法超时，因为回溯找所有组合花费较多时间
#         area = len("".join(words))
#         if area > len(s):
#             return []

#         sub_str = set()
#         choice = []

#         def backtrack(choice, words):
#             if len(choice) == len(words):
#                 sub_choice = [v for c,v in choice]
#                 sub_str.add("".join(sub_choice))
#                 return
#             for i, w in enumerate(words):
#                 if (i, w) in choice:
#                     continue
#                 choice.append((i, w))
#                 backtrack(choice, words)
#                 choice.pop(-1)
#         backtrack(choice, words)
#         # print(sub_str)

#         i = 0
#         result = []
#         while i+area-1 < len(s):
#             if s[i:i+area] in sub_str:
#                 result.append(i)
#             i += 1
#         return result

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        step = len(words[0])
        area = step * len(words)
        if area > len(s):
            return []

        def check(string, words, step):                       # todo：每次遍历，把对应的字符串传进来处理
            words_list = list(words)
            for i in range(0, len(string), step):
                if string[i:i+step] not in words_list:
                    return False
                else:
                    words_list.remove(string[i:i + step])
            return True

        i = 0
        result = []
        while i+area <= len(s):
            if check(s[i:i+area], words, step):
                result.append(i)
            i += 1
        return result