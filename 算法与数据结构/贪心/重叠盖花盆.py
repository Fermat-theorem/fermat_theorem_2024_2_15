'''
花盆有坐标，同一坐标的花盆用一块模板是可以覆盖的，给你一系列输入，
'''
def func():
    # please define the python3 input here.
    # For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    M, S, N = list(map(int, input().split(" ")))
    area = set([0])
    cha_value = []

    for i in range(1, N + 1):
        area.add(int(input()))
    area = list(area)
    area.sort()
    for i in range(2, len(area)):
        cha_value.append(area[i]-area[i-1]-1)

    cha_value.sort(reverse=True)
    max_value = max(area)
    min_value = min(area[1:])

    result = max_value - min_value + 1 - sum(cha_value[:M-1])
    print(result)


if __name__ == "__main__":
    func()