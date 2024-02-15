class Solution:
    def get_min_step(self, steps):
        count = 0
        steps = [0] + steps
        for i in range(1, len(steps)):           # todo:最主要要抽象出合适的表达式，抽象出为什么count要新增，这一点比较重要
            if steps[i] > steps[i-1]:
                count += steps[i] - steps[i-1]
        return count

if __name__ == "__main__":
    count = input().strip()
    steps = list(map(int, input().strip().split()))
    function = Solution()
    results = function.get_min_step(steps)
    print(results)