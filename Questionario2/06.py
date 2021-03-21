lst = []
while True:
    op = input().split()
    if op[0] == 'I':
        lst.insert(0, int(op[1]))
    elif op[0] == 'F':
        lst.append(int(op[1]))
    elif op[0] == 'P':
        print(lst.pop())
    elif op[0] == 'D':
        print(lst.pop(0))
    elif op[0] == 'V':
        print(lst.count(int(op[1])))
        lst = [i for i in lst if i != int(op[1])]
    elif op[0] == 'E':
        print(lst.pop(int(op[1]) - 1))
    elif op[0] == 'T':
        for i in range(len(lst)):
            if int(op[1]) == lst[i]:
                lst.pop(i)
                lst.insert(i, int(op[2]))
                break
    elif op[0] == 'C':
        print(lst.count(int(op[1])))
    elif op[0] == 'X':
        print()
        break

for i in lst:
    print(i)
