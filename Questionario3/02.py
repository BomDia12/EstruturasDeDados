n = int(input())
clothes = sorted(input().split())
counter = 0
for i in range(n):
    try:
        counter += 1 if clothes[i] == clothes[i + 1] else 0
    except IndexError:
        continue

print(counter)
