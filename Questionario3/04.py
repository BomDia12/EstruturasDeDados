n = int(input())
ceps = sorted([input() for i in range(n)])
last = ''.join('a' for i in range(len(ceps[0])))
for i in range(len(ceps)):
    temp = ceps[i]
    ceps[i] = ''.join([ceps[i][j] if ceps[i][j] != last[j] else ' ' for j in range(len(ceps[i]))])
    last = temp
print(f"R$ {0.07 * sum([cep.count(' ') for cep in ceps]):.2f}")
