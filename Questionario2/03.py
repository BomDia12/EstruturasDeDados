import math as m

size, period = map(int, input().split())
lst = [int(i) for i in input().split()]

for i in range(period, len(lst) + 1, 1):
    print(m.floor(sum(lst[i - period:i]) / period))
