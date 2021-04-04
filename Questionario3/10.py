n = int(input())
lst = [[input(), input(), input(), input()] for i in range(n)]
for ver in lst:
    used = ver[0]
    brinks = False
    for timeframe in ver[1:]:
        for char in timeframe:
            if char not in used:
                brinks = True
                break
            else:
                used = used.replace(char, '', 1)
    if brinks:
        print('You died!')
    elif used == '':
        print("It's in the box!")
    else:
        new = ''
        for char in used:
            new += char if char not in new else ''
        print(f"Bora ralar: {''.join(sorted(new))}")
