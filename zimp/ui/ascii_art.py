import sys
from zimp.ui.clihelpers import Colors, color


sep = "\\"
if sys.path[0].__contains__("/"):
    sep = "/"
file = "../" * len(sys.path[0].split("zimp" + sep)[1].split(sep))
file += "../data/basic_font"

values = {}
i = 0
j = 0
k = 0
c = ''
for line in open(file):
    if i % 7 == 0:
        c = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'\
            [j]
        values[c] = ['', '', '', '', '', '', '']
        j += 1
        k = 0
    values[c][k] = line[3:-1] + (" " * (9 - (len(line) - 4)))
    i += 1
    k += 1


def fancy_text(text, colorv=Colors.Black, backgroundv=None):
    for c in text:
        if c not in values and not c == '\n':
            raise Exception("Unknown character")

    ret = []

    for line in text.split('\n'):
        lines = ['', '', '', '', '', '', '']
        for c in line:
            max_length = 0
            for i in range(0, 7):
                lines[i] += values[c][i]

                if len(lines[i]) > max_length:
                    max_length = len(lines[i])

            for i in range(0, 7):
                if len(lines[i]) < max_length:
                    lines[i] += ' ' * (max_length - len(lines[i]))

        max_length = max([len(l) for l in lines])
        for i in range(0, 7):
            if len(lines[i]) < max_length:
                lines[i] += ' ' * (max_length - len(lines[i]))

        ret.append('\n'.join(lines))

    output = '\n'.join(ret)

    output2 = ''
    for c in output:
        if c == '\n':
            output2 += c
        elif not backgroundv is None and c == ' ':
            output2 += color(backgroundv, '.', backgroundv)
        else:
            output2 += color(colorv, c)

    return output2
