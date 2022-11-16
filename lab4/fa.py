from typing import AnyStr


class State:
    def __init__(self, value: str = ""):
        self.value: str = value
        self.transitions: dict[str, str] = dict()

    def __eq__(self, other):
        return self.value == other.value

    def add_transition(self, other, alphabet):
        self.transitions[other] = alphabet

    def __str__(self):
        return f"state: {self.value} \n transitions: {self.transitions}"


class FA:
    def __init__(self, file_name):
        self.states: list[State] = list()
        self.alphabet: list[str] = list()
        self.initial_state: State = State()
        self.end_states: list[State] = list()
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
            self.end_states = list(map(State, FA.get_line(file.readline())))
            file.readline()
            for line in file:
                source = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                letter = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                destination = line.strip().split('->')[1]
                for state in self.states:
                    if state.value == source:
                        state.add_transition(destination, letter)
                print(f"source: {source}, letter: {letter}, destination = {destination}")


        print(f"states: ")
        for state in self.states:
            print(state)
        print(f"alphabet: {self.alphabet}")
        print(f"initial state: {self.initial_state}")
        print(f"end states:")
        for state in self.end_states:
            print(state)

