def partial(to_check, opposite):
    double_start = 0
    single_start = 0
    for i in range(len(equation)):
        if equation[i:i + 2] == to_check * 2:
            double_start += 1
        elif equation[i] == to_check and equation[i - 1] != to_check:
            single_start += 1
        elif double_start > 0 and (equation[i:i + 2] == opposite * 2):
            break
        elif single_start > 0 and equation[i] == opposite:
            single_start -= 1
        elif double_start > 0 and (equation[i] == opposite):
            double_start -= 1
    if double_start > 0:
        return True
    else:
        return False


equations = [input() for i in range(int(input()))]

for equation in equations:
    parenthesis = partial('(', ')')
    brackets = partial('[', ']')
    curly_brackets = partial('{', '}')
    if parenthesis or brackets or curly_brackets:
        print('A expressão possui duplicata.')
    else:
        print('A expressão não possui duplicata.')
