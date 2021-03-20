n_lines = int(input())

in_lines = [input() for i in range(n_lines)]

for in_string in in_lines:
    out_string, current_char, repetitions = '', '', '0'
    for char in in_string:
        if char.isnumeric():
            repetitions += char
        else:
            out_string += current_char * int(repetitions)
            current_char, repetitions = char, ''
    out_string += current_char * int(repetitions)
    print(out_string)
