n = int(input())
pretendentes = [input().split() for i in range(n)]
pretendentes = [[pretendentes[i][0], pretendentes[i][1], pretendentes[i][2],
                 abs(int(pretendentes[i][2]) - 180), abs(int(pretendentes[i][3]) - 75) if int(pretendentes[i][3]) <= 75
                 else int(pretendentes[i][3])] for i in range(n)]
pretendentes = sorted(pretendentes, key=lambda x: (x[3], x[4], x[1], x[0]))
print(pretendentes)
[print(f'{pretendente[1]}, {pretendente[0]}') for pretendente in pretendentes]
