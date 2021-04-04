import math


n = int(input())
houses = [[int(oi) for oi in input().split()] for i in range(n)]
houses = sorted([[math.ceil(house[1] / house[0]) if house[0] != 0 else 0, house[0]] for house in houses], key=lambda x: x[1])
houses = sorted(houses, key=lambda x: x[0], reverse=True)
[print(f'{house[0]} / {house[1]}') for house in houses]
