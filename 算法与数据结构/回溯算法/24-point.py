class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        permutations = self.permuteUnique(cards)
        for permutation in permutations:
            if self.compute(permutation):
                print(permutation)
                return True
        return False

    # 唯一排序
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        permutations = []
        nums.sort()
        tmp = []
        visited = [False] * len(nums)
        self.backtracking(nums, tmp, visited, permutations)
        return permutations

    # 回溯
    def backtracking(self, nums: list[int], tmp: list[float], visited: list[bool], perm: list[int]) -> None:

        if len(nums) == len(tmp):
            perm.append(tmp[:])
            return
        for i in range(len(nums)):
            # 已经判断过就跳过
            if visited[i]:
                continue
            #   如果当前的和上一个相同，就跳过，同时要求没有被使用过
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            visited[i] = True
            tmp.append(nums[i])
            self.backtracking(nums, tmp, visited, perm)
            visited[i] = False
            tmp.pop()

    def compute(self, nums: list[float]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24) <= 0.00001
        # 生成 0-3 的 数字,并进行遍历
        for i in range(len(nums) - 1):  # 计算+-*/对应的结果
            # tmp 追加 第一位数字和第二位数字的加减乘除
            tmp = []
            tmp.append(nums[i] + nums[i + 1])
            tmp.append(nums[i] - nums[i + 1])
            tmp.append(nums[i] * nums[i + 1])
            if nums[i + 1] != 0:
                tmp.append(nums[i] / nums[i + 1])
            # 获取 前两位的加减乘除
            for num in tmp:
                # 把输入的数组扔进一个新的数组
                new_list = nums[:]
                # 把当前位 赋值成 前两位的结果
                new_list[i] = num
                #  弹出当前位的下一位,如 i= 0 ,弹出 new_list[1],不断迭代。直至数组剩下最后一位,计算误差
                new_list.pop(i + 1)
                if self.compute(new_list):
                    print(tmp)
                    return True
        return False
# 自己的写法


# cards = [1,3,4,6]
# cards = [str(num) for num in cards]
# choice = []
# result = []
# def track(cards, choice):
#     if len(choice) == 4:
#         result.append(list(choice))
#         return
#     for num in cards:
#         if num in choice:           # todo：这种写法为什么不行？因为比如数据列表为【1，2，3，1】，本身就会有重复值，所以全排列判断到第二个1，将永远无法满足
#             continue
#         choice.append(num)
#         track(cards, choice)
#         choice.remove(num)
#
# track(cards, choice)
# print(result)


# class Solution:
#     def judgePoint24(self, cards: list[int]) -> bool:
#
#         import math
#         cards = [str(num) for num in cards]
#         print(cards)
#         choice = []
#         result = []
#         operate = ['+', '-', '*', '/']
#
#         def track(cards, choice):
#             if len(choice) == 4:
#                 print(choice)
#                 result.append([c[1] for c in choice])
#                 return
#             for index,num in enumerate(cards):
#                 if (index, num) in choice:
#                     continue
#                 choice.append((index, num))
#                 track(cards, choice)
#                 choice.remove((index, num))
#
#         track(cards, choice)
#         print(result)
#
#         def check1(x1, x2, x3, x4, i, j, k):
#             value1 = '(' + x1 + i + x2 + ')' + j + x3 + k + x4
#             value2 = '('+ x1 + i + x2 + j + x3 + ')' + k + x4
#             value3 = x1 + i +'('+  x2 + j + x3 + ')' + k + x4
#             value4 = '(' + x1 + i + x2 + ')' + j + '(' + x3 + k + x4 + ')'
#             value5 = x1 + i + x2 + j + x3 + k + x4
#             value6 = x1 + i + '(' + x2 + j + '(' + x3 + k + x4 + ')' + ')'
#
#
#             values = [value1,value2,value3,value4,value5,value6]
#             for mm in values:
#                 try:
#                     if math.isclose(eval(mm),24):
#                         return True
#                 except:
#                     continue
#             else:
#                 return False
#
#         count = 0
#         for c in result:
#             a, b, c, d = c
#             for i in operate:
#                 for j in operate:
#                     for k in operate:
#                         count += 1
#                         if check1(a, b, c, d, i, j, k):
#                             print(count)
#                             return True
#         else:
#             print(count)
#             return False

a = Solution()
b = a.judgePoint24([8, 4, 1, 7])
print(b)
