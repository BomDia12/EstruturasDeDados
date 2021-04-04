n = int(input())
names = sorted([input() for i in range(n)], key=lambda x: len(x), reverse=True)
trashed = []
vai = True
for i in range(len(names)):
    try:
        if len(names[i]) != len(names[i + 1]) and len(names[i]) not in trashed:
            print(names[i])
            vai = False
            break
        else:
            trashed.append(len(names[i]))
    except IndexError:
        continue

if vai and len(names[-1]) in trashed:
    print('Que mala suerte!')
else:
    print(names[-1])
