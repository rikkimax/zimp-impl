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
        c = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:'\
            [j]
        values[c] = ['', '', '', '', '', '', '']
        j += 1
        k = 0
    values[c][k] = line[3:-1] + (" " * (9 - (len(line) - 4)))
    i += 1
    k += 1


def fancy_text(text, colorv=Colors.Black, backgroundv=None):
    for c in text:
        if c not in values and not (c == '\n' or c == '\t'):
            print(c)
            raise Exception("Unknown character")

    ret = []

    for line in text.split('\n'):
        lines = ['', '', '', '', '', '', '']
        for c in line:
            if c == '\t':
                for i in range(0, 7):
                    lines[i] = '    ' * 4
            else:
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


# -- Claire's code --
def print_welcome():
    print("\tWelcome to the wonderful world of Zombie in my Pocket.")
    print("\tHere you will find a house with rotating rooms, bats with")
    print("\tdiarrhea, and a graveyard at the end of the garden.")
    print("\tOh, and zombies, lots of zombies.")
    print("\tBut don't worry, there are a few items scattered around")
    print("\tthe house that can help you.  You may even get to wield")
    print("\ta chansaw, zombies hate chainsaws.")
    print("\tThe object of the game is to find the zombie totem hidden")
    print("\tin the evil temple and bury it in the graveyard before ")
    print("\tthe clock strikes midnight.  Not dying is also helpful.")
    # -- Richard edit --
    # print("\tEnter 's' to start, 'q' to quit.")
    # -- Richard edit --
    print("\tHurry, time is running out...")


def print_bat():
    print("\t   /\                 /\ ")
    print("\t  / \''._   (\_/)   _.'/ \ ")
    print("\t /_.''._'--('.')--'_.''._\ ")
    print("\t | \_ / `;=/   \=;` \ _/ |")
    print("\t  \/ `\__|`\___/`|__/` \/")
    print("\t   `      \(/|\)/")
    print("\t           ' ` '")
    # -- Claire's code --
