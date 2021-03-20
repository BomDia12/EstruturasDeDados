string = input()

times = string.count('*')

string = string.replace('*', '')

print(string[:times])
