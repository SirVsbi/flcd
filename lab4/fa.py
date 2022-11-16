from typing import AnyStr
import graphviz


class State:
    def __init__(self, value: str = ""):
        self.value: str = value
        self.transitions: dict[str, str] = dict()

    def add_transition(self, other, alphabet):
        self.transitions[other] = alphabet

    def get_transtion(self, symbol):
        return self.transitions[symbol]

    def __str__(self):
        return f"state: {self.value} \n transitions: {self.transitions}"

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, rhs):
        return self.value == rhs


class FA:
    def __init__(self, file_name):
        self.states: list[State] = list()
        self.alphabet: list[str] = list()
        self.initial_state: State = State()
        self.end_states: list[str] = list()
        self.transitions: dict[tuple[str, str], list[str]] = dict()
        self.__read_fa(file_name)

    @staticmethod
    def get_line(line: AnyStr) -> list[str]:
        return line.strip().split(' ')[2:]

    @staticmethod
    def create_state(state):
        return State(value=state)

    def __read_fa(self, filename):
        with open(filename) as file:
            self.states = list(map(State, FA.get_line(file.readline())))
            self.alphabet = FA.get_line(file.readline())
            self.initial_state = State(value=FA.get_line(file.readline())[0])
            self.end_states = FA.get_line(file.readline())
            file.readline()
            for line in file:
                source = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                route = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1].replace(" ",
                                                                                                                    "")
                destination = line.strip().split('->')[1].replace(" ", "")
                for state in self.states:
                    if state.value == source:
                        state.add_transition(route, destination)
                if (source, route) in self.transitions.keys():
                    self.transitions[(source, route)].append(destination)
                else:
                    self.transitions[(source, route)] = [destination]

    def isDFA(self) -> bool:
        for transition in self.transitions.keys():
            if len(self.transitions[transition]) > 1:
                return False
        return True

    def is_accepted(self, sequence: str) -> bool:
        if not self.isDFA():
            return False
        current_state = self.initial_state.value
        for symbol in sequence:
            if (current_state, symbol) not in self.transitions.keys():
                return False
            current_state = self.transitions[(current_state, symbol)][0]
        return current_state in self.end_states

    def __str__(self):
        string = "states: \n"
        for state in self.states:
            string += f"{state} \n"
        string += f"alphabet: {self.alphabet} \n"
        string += f"initial state: {self.initial_state.value} \n"
        string += f"end states: "
        for state in self.end_states:
            string += f"{state} "
        return string

    def diagram(self):
        dot = graphviz.Digraph('finite_state_machine', format='png')
        dot.graph_attr['rankdir'] = 'LR'
        for state in self.states:
            if state.value in self.end_states:
                dot.node(state.value, shape='doublecircle')
            else:
                dot.node(state.value, shape='circle')
        for transiton in self.transitions:
            dot.edge(transiton[0], self.transitions[transiton][0], label=transiton[1])
        dot.render(view=True)

