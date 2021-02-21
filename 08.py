n_lines = int(input())

lines = [input().strip('0') for i in range(n_lines)]

for line in lines:
    started, zeros = False, 0
    for digit in line:
        if digit == '1':
            started = True
        elif started:
            zeros += 1
    print(zeros)
