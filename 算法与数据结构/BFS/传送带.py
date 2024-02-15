'''
欢迎各位勇者来到力扣城，本次试炼主题为「信物传送」。
本次试炼场地设有若干传送带，matrix[i][j] 表示第 i 行 j 列的传送带运作方向，"^","v","<",">" 这四种符号分别表示 上、下、左、右 四个方向。
信物会随传送带的方向移动。勇者每一次施法操作，可临时变更一处传送带的方向，在物品经过后传送带恢复原方向。
'''

class Solution:
    def conveyorBelt(self, matrix: list[str], start: list[int], end: list[int]) -> int:
        m, n, q = len(matrix), len(matrix[0]), [start]
        res = [[float('inf') for _ in range(n)] for _ in range(m)]
        res[start[0]][start[1]] = 0

        while q:
            nxt = []
            for i, j in q:
                if i - 1 >= 0 and (v := res[i][j] + (0 if matrix[i][j] == '^' else 1)) < res[i - 1][j]:
                    res[i - 1][j] = v
                    nxt.append([i - 1, j])
                if i + 1 < m and (v := res[i][j] + (0 if matrix[i][j] == 'v' else 1)) < res[i + 1][j]:
                    res[i + 1][j] = v
                    nxt.append([i + 1, j])
                if j - 1 >= 0 and (v := res[i][j] + (0 if matrix[i][j] == '<' else 1)) < res[i][j - 1]:
                    res[i][j - 1] = v
                    nxt.append([i, j - 1])
                if j + 1 < n and (v := res[i][j] + (0 if matrix[i][j] == '>' else 1)) < res[i][j + 1]:
                    res[i][j + 1] = v
                    nxt.append([i, j + 1])
            q = nxt

        return res[end[0]][end[1]]

