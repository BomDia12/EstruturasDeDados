import re


start = [int(item) for item in re.split(' |:', input())]
end = [int(item) for item in re.split(' |:', input())]
result = [end[i] - start[i] for i in range(len(start))]

valid = True

for i in range(3, -1, -1):
    if result[i] < 0:
        if i > 1:
            result[i - 1] -= 1
            result[i] += 60
        elif i == 1:
            result[i - 1] -= 1
            result[i] += 24
        else:
            valid = False

if valid:
    print(f'{result[0]} dia(s)\n{result[1]} hora(s)\n{result[2]} minuto(s)\n{result[3]} segundo(s)')
else:
    print('Data inválida!')
