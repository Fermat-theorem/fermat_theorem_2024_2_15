# 密码锁开锁
# class Solution:
#     def openLock(self, deadends: list[str], target: str) -> int:
#         q = []
#         start = '0000'
#         turn = 0
#         q_set = set()
#         deadends = set(deadends)             # todo：原有的写法为列表，查询会比较慢，集合快很多1400ms —→ 900ms
#         if '0000' in deadends:
#             return -1
#         q.append([start, turn])
#         q_set.add(start)
#
#         def handle(choice, num):
#             for i in range(4):
#                 res1 = choice[:i] + str((int(choice[i])+1) % 10) + choice[i+1:]
#                 res2 = choice[:i] + str((int(choice[i])-1) % 10) + choice[i+1:]         # todo：字符转换的方法
#                 if res1 not in q_set:
#                     q.append([res1, num+1])
#                     q_set.add(res1)
#                 if res2 not in q_set:
#                     q.append([res2, num+1])
#                     q_set.add(res2)
#
#         while q:
#             start, turn = q.pop(0)
#             if start == target:
#                 return turn
#             if start not in deadends:
#                 handle(start, turn)
#         return -1

# ————————————————————————————————————方法二——————————————————————————————————————————
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        q = []
        turn = 0
        q_set = set()
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        q.append(['0000', turn])
        q_set.add('0000')

        def handle(lis):
            x, y = lis
            for i in range(4):
                res1 = x[:i] + str((int(x[i])+1) % 10) + x[i+1:]
                res2 = x[:i] + str((int(x[i])-1) % 10) + x[i+1:]
                if res1 not in q_set:
                    nums.append([res1, y+1])
                    q_set.add(res1)
                if res2 not in q_set:
                    nums.append([res2, y+1])
                    q_set.add(res2)

        while q:
            nums = []                      # todo：这种写法相当于把选择的后续重新更新在目标列表，不在从历史路径的列表pop了，原来的写法相当于把产生的新结果追加到列表后面
            for m in q:                    # todo：速度上会比之前那个更快
                start, turn = m
                if start == target:
                    return turn
                if start not in deadends:
                    handle(m)
            q = nums
        return -1


a = Solution()
a.openLock(["0201", "0101", "0102", "1212", "2002"], "9999")

# todo：双向BFS、BFS优化技巧
