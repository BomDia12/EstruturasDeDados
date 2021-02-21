def analisa(n1, n2):
    lst = [n1, n2]
    lst.sort()
    print(f'{lst[0]}\n{lst[1]}\niguais') if n1 == n2 else print(f'{lst[1]}\n{lst[0]}\ndiferentes')
