class Solution:
    def findLength(self, A: list[int], B: list[int]) -> int:
        def find_lenth(a_in, b_in, lenth):
            result = 0
            k = 0
            for i in range(lenth):
                if A[a_in+i] == B[b_in+i]:
                    k += 1
                    result = max(result, k)
                else:
                    k = 0
            return result

        m, n = len(A), len(B)
        ret = 0
        for i in range(m):
            lth = min(n, m-i)
            ret = max(find_lenth(i, 0, lth), ret)         # todo:这里要区分是索引还是个数，以及我传进函数的是索引，思考为什么？
        for i in range(n):
            lth = min(n - i, m)
            ret = max(find_lenth(0, i, lth), ret)
        return ret

a = Solution()
b = a.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
print(b)
