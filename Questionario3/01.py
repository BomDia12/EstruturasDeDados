n = int(input())
grades = sorted([float(input()) for i in range(n)])

print(f'{grades[0]:.2f}')
print(f'{grades[len(grades) // 2]:.2f}') if n % 2 != 0 else print(f'{(grades[len(grades) // 2] + grades[len(grades) // 2 + 1]) / 2:.2f}')
print(f'{grades[-1]:.2f}')
