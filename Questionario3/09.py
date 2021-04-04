n, k = map(int, input().split())
lst = [int(input()) for i in range(n)]
lst = [[item, item % k if item >= 0 else -(abs(item) % k)] for item in lst]
lst = [[item[0], item[1], 1 if item[0] % 2 == 0 else 0] for item in lst]
lst = [[item[0], item[1], item[2], item[0] if item[2] else -item[0]] for item in lst]
lst = sorted(lst, key=lambda x: (x[1], x[2], x[3]), reverse=True)
print(lst)
print(' '.join([str(item[0]) for item in lst]))
