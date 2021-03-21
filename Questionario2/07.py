shopping_list = {}

while True:
    enter = input()
    if enter == 'fim':
        break
    else:
        item, value = enter.split()
        if item == '-':
            shopping_list.pop(value)
        else:
            shopping_list[item] = float(value)

temp = [f'{item}: R$ {shopping_list[item]:.2f}' for item in shopping_list]
temp.reverse()
[print(i) for i in temp]
print('----------------------')
print(f'{len(shopping_list)} item(ns): R$ {sum([shopping_list[item] for item in shopping_list]):.2f}')
