reservedWords = []
separators = []
operators = []


def read_file():
    with open('token.in', 'r') as f:
        f.readline()
        for i in range(11):
            separator = f.readline().strip()
            if separator == "<space>":
                separator = " "
            separators.append(separator)
        for i in range(14):
            operators.append(f.readline().strip())
        for i in range(13):
            reservedWords.append(f.readline().strip())