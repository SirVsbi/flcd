# TODO: LL(1)
from typing import List

from lab5.production import Production


class Grammar:
    def __init__(self, non_terminals: List[str], terminals: List[str], productions: List[Production],
                 starting_symbol: str):
        self.__non_terminals = non_terminals
        self.__terminals = terminals
        self.__productions = productions
        self.__starting_symbol = starting_symbol
        self.__first = set()

    def __str__(self):
        return f"""
            Grammar: 
            Non-terminals: {self.__non_terminals}, 
            Terminals: {self.__terminals},
            Productions: {list(map(str, self.__productions))}, 
            Starting symbol: {self.__starting_symbol}
        """.replace("            ", "")

    def traverse(self):
        ...

    def generate_first(self):
        for non_terminal in self.__non_terminals:
            self.__first.add(non_terminal)
        isDone = False
        for production in self.__productions:
            for rule in production.rhs:
                partialSet = self.__first[production.lhs]
                partialSet = partialSet.union(partialSet)

