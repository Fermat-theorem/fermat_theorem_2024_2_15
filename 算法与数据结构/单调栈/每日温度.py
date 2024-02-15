'''
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
如果气温在这之后都不会升高，请在该位置用 0 来代替。
eg.
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
eg.
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
'''
# ——————————————————————————————————方法一——————————————————————————————————
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # 用来存储索引
        n = len(temperatures)
        process_list = []
        result = [0] * n
        for i in range(n):
            while process_list and temperatures[process_list[-1]] < temperatures[i]:
                index = process_list.pop()
                result[index] = i - index
            process_list.append(i)
        return result
