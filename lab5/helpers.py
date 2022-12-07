from typing import List

from lab5.grammar import Grammar
from lab5.production import Production


def read_grammar(filename) -> Grammar:
    with open(filename, "r") as file:
        non_terminals = parse_line(file.readline())
        terminals = parse_line(file.readline())
        starting_symbol = file.readline().strip().split('=')[1].strip()[0]
        productions = parse_productions(parse_line(''.join([line for line in file])))
        return Grammar(non_terminals, terminals, productions, starting_symbol)


def parse_line(line: str):
    return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]


def parse_productions(productions_text):
    # print(productions_text)
    productions_list = productions_text[0].split("\n")
    productions: List[Production] = list()
    for line in productions_list:
        lhs, rhs = line.split("->")
        rhs.strip()
        rhs = rhs.split("|")

        print(rhs)
        lhs.strip().replace("\n", "")
        productions.append(Production(lhs, rhs))
    return productions
