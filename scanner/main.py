import re

from lab4.fa import FA
from languageSymbols import read_file, reservedWords, separators, operators
from pif import PIF
from scanner import Scanner
from symbol_table import SymbolTable


class Main:

    def __init__(self):
        self.st = SymbolTable(17)
        self.pif = PIF()
        self.scanner = Scanner()

    def run(self):
        read_file()
        file_name = "p3.txt"
        exception_message = ""

        fa_identifier: FA = FA('fa-identifier.in')
        fa_constant: FA = FA('fa-constant.in')

        with open(file_name, 'r') as file:
            lineCounter = 0
            for line in file:
                lineCounter += 1
                tokens = self.scanner.tokenize(line.strip())
                extra = ''
                for i in range(len(tokens)):
                    if tokens[i] in reservedWords + separators + operators:
                        if tokens[i] == ' ':  # ignore adding spaces to the pif
                            continue
                        self.pif.add(tokens[i], (-1, -1))
                    elif tokens[i] in self.scanner.cases and i < len(tokens) - 1:
                        if re.match("[1-9]", tokens[i + 1]):
                            self.pif.add(tokens[i][:-1], (-1, -1))
                            extra = tokens[i][-1]
                            continue
                        else:
                            exception_message += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                                lineCounter) + "\n"
                    elif fa_identifier.is_accepted(tokens[i]):
                        id = self.st.add(tokens[i])
                        self.pif.add("id", id)
                    elif fa_constant.is_accepted(tokens[i]):
                        const = self.st.add(extra + tokens[i])
                        extra = ''
                        self.pif.add("const", const)
                    else:
                        exception_message += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            lineCounter) + "\n"

        with open('st.out', 'w') as writer:
            writer.write(str(self.st))

        with open('pif.out', 'w') as writer:
            writer.write(str(self.pif))

        if exception_message == '':
            print("Lexically correct")
        else:
            print(exception_message)


main = Main()
main.run()
