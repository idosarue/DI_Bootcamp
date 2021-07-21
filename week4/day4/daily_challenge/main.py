

matrix = [
    ['7', 'T', 'h', 'i', 's', '$', '#', '^'],
    ['i', 's', '%', ' ', 'M', 'a', 't', 'r'],
    ['3', 'i', 'x', '#', '', '', '%', '!']
]

for line in matrix:
    for char in line:
        if char.isalpha():
            print(char, end="")
        elif not char.isalpha() and line[line.index(char) - 1].isalpha():
            print(' ', end="")
