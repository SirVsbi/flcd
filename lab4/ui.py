from lab4.fa import FA


class UI:

    def __init__(self):
        self.automata = FA("fa.in")

    def readAutomata(self):
        self.automata = FA("fa.in")

    def print_all(self):
        print(self.automata)

    def print_states(self):
        for state in self.automata.states:
            print(state)

    def print_alphabet(self):
        print(self.automata.alphabet)

    def print_transitions(self):
        print(self.automata.transitions)

    def print_initial_state(self):
        print(self.automata.initial_state)

    def print_end_states(self):
        print(self.automata.end_states)

    def check_if_deterministic(self):
        print("it's deterministic" if self.automata.isDFA() else "it's not deterministic")

    def check_sequence(self):
        sequence = input()
        print("Sequence accepted" if self.automata.is_accepted(sequence) else "sequnce is not accepted")

    def show_diagram(self):
        self.automata.diagram()

    def print_menu(self):
        print("0. Exit")
        print("1. Read finite automata from file")
        print("2. Print everything")
        print("3. Print states")
        print("4. Print alphabet")
        print("5. Print transitions")
        print("6. Print initial states")
        print("7. Print end states")
        print("8. Check if the finite automata is deterministic")
        print("9. Check if sequence is accepted")
        print("10. Show diagram")

    def run(self):
        commands = {
            '1': self.readAutomata,
            '2': self.print_all,
            '3': self.print_states,
            '4': self.print_alphabet,
            '5': self.print_transitions,
            '6': self.print_initial_state,
            '7': self.print_end_states,
            '8': self.check_if_deterministic,
            '9': self.check_sequence,
            '10': self.show_diagram
        }
        exit_flag = False
        while not exit_flag:
            self.print_menu()
            command = input()
            if command in commands.keys():
                commands[command]()
            elif command == "0":
                exit_flag = True
            else:
                continue
