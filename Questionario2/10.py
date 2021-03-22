def partial(to_check, opposite):
    double_start = 0
    for i in range(len(equation)):
        if equation[i:i + 2] == to_check * 2:
            double_start += 1
        elif double_start > 0 and (equation[i] == ')'):
            double_start -= 1


amount = int(input())
equations = [input() for i in range(amount)]

for equation in equations:
    if True > 0:
        print('A expressão possui duplicata.')
    else:
        print('A expressão não possui duplicata.')
