n = int(input())
riders = []
for i in range(n):
    riders.append([input()])
    riders[i].append(sum([float(time) for time in input().split()]))

riders = sorted(riders, key=lambda x: x[1])
for i in range(len(riders)):
    print(f'{i + 1}. {riders[i][0]} ({int(riders[i][1] // 60)}:{riders[i][1] % 60:06.3f})')
