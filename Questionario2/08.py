main = []
time = 0
while True:
    command = input().split()
    if command[0] == 'i':
        if command[2] == '0' or int(command[2]) > len(main):
            main.append([int(command[1]), time])
        else:
            main.append([int(command[1]), time, len(main) - int(command[2])])
    elif command[0] == 'r':
        for i in range(len(main)):
            if main[i][0] == int(command[1]):
                main.pop(i)
                for j in range(len(main)):
                    if len(main[j]) > 2:
                        if main[j][2] == i:
                            main[j].pop(2)
                        elif main[j][2] > i:
                            main[j][2] -= 1
                break
    else:
        break
    time += 1

if main:
    [print('[{0}]'.format(','.join(map(str, node))), end=' ') for node in main]
else:
    print('-1')
