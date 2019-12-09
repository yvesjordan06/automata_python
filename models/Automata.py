from models.Alphabet import Alphabet
from models.Transition import Transition


class Type:
    DFA = 'Definite Finite State Automata'
    NFA = 'Non-Definite Finite State Automata'
    eNFA = f'Epsilon {NFA}'


class Automata:
    def __init__(self, alphabet, states, initial_state, final_states, transitions):
        self.__alphabet = alphabet if isinstance(
            alphabet, Alphabet) else Alphabet(alphabet)
        self.__states = set()
        for x in states:
            if isinstance(x, (str, int)):
                self.__states.add(frozenset(str(x)))
            elif isinstance(x, (set, list, tuple, frozenset)):
                self.__states.add(frozenset(x))

        if isinstance(initial_state, (str, int)):
            self.__initial_state = set(str(initial_state))
        else:
            self.__initial_state = set(initial_state)
        self.__final_states = {str(final_states)} if isinstance(
            final_states, (str, int)) else {str(x) for x in final_states}
        self.__transitions = set()
        print(transitions)
        if isinstance(transitions, list):
            for trans in transitions:
                self.add_transition(trans)
        else:
            self.add_transition(transitions)

    def get_alphabet(self):
        return self.__alphabet

    def get_states(self):
        return self.__states

    def get_initial_state(self):
        return self.__initial_state

    def get_final_states(self):
        return self.__final_states

    def get_transitions(self):
        return self.__transitions

    def show_transitions(self):
        return [x.get_transition() for x in self.__transitions]

    def has_states(self, states):
        try:
            states = list(states) if isinstance(states, (str, int)) else states
            if isinstance(states, (list, tuple, set)):
                for state in states:
                    if set(state) not in self.__states:
                        raise Exception(
                            str(state) + ' is not a state in the Automata')
        except Exception as error:
            print('Automata Error:', error)
            return False
        else:
            return True

    def add_transition(self, transition):
        # Add Transition Method
        try:
            if isinstance(transition, Transition):
                self.__validate_transition(transition)
                self.__transitions.add(transition)
            elif isinstance(transition, tuple):
                _from = str(list(transition)[0])
                _on = str(list(transition)[1])
                _to = str(list(transition)[2])
                new_trans = Transition(_from, _on, _to)
                self.__validate_transition(new_trans)
                self.__transitions.add(new_trans)
            else:
                raise Exception(
                    'Cannot read transition expected format \n Expected Format (from, on, to)')
        except Exception as error:
            print('Transition Error:', error)

    def __validate_transition(self, transition):
        try:
            result = transition.get_from() in self.__states \
                     and (
                             transition.get_on() in self.__alphabet
                             or not transition.get_on()
                     ) \
                     and transition.get_to() in self.__states
            if not result:
                raise Exception(str(transition) +
                                ' Transition not valid in Automata')
        except Exception as error:
            raise error
        else:
            return True

    def read(self, start, symbol):
        to = list()
        try:
            if isinstance(start, set) and len(start) > 1:
                for i in start:
                    for transition in self.__transitions:
                        if {i} == transition.get_from() and str(symbol) == transition.get_on():
                            to.append(frozenset(transition.get_to()))
                return to
            if set(start) not in self.__states:
                raise Exception(str(start) + '  not found in Automata states')
            if symbol not in self.__alphabet and symbol != '':
                raise Exception(str(symbol) + '  not found in Automata alphabet')
            for transition in self.__transitions:
                if start == transition.get_from() and str(symbol) == transition.get_on():
                    to.append(frozenset(transition.get_to()))
        except Exception as error:
            print('Transition Read Error:', error)
            raise Exception
        else:
            return to

    def knows_word(self, word):
        _next = self.__initial_state
        try:
            for symbol in str(word):
                _next = self.read(_next, symbol)
            if set(_next).intersection(self.__final_states):
                return True
            else:
                return False
        except:
            return False

    def epsilon_closure(self, _state) -> set:
        state = set()
        closure = list()
        verified_closure = list()
        if isinstance(state, (str, int)):
            state = {str(_state)}
        else:
            state = set(_state)
        closure.append(state)
        for iter_state in closure:
            if iter_state in verified_closure:
                continue
            else:
                read = list()
                try:
                    _read = self.read(iter_state, '')
                    read = set()

                    for x in _read:
                        read.update(x)
                except Exception as error:
                    print("line 153", error)
                if read:
                    closure.append(set(read))
            verified_closure.append(frozenset(iter_state))
        return set(verified_closure)

    def check_type(self) -> str:
        epsilon = False
        non_deterministic = False
        try:
            for transition in self.__transitions:
                if len(self.read(transition.get_from(), transition.get_on())) > 1:
                    non_deterministic = True
                if not transition.get_on():
                    epsilon = True
                    non_deterministic = True
                if epsilon and non_deterministic:
                    return Type.eNFA
            if non_deterministic:
                return Type.NFA
            else:
                return Type.DFA
        except Exception as error:
            print('Unknown Error:', error)

    def convert_to_dfa(self):
        automata_type = self.check_type()
        states = [self.__initial_state]
        transitions = set()
        verified_state = set()
        print(automata_type)
        if automata_type == Type.DFA:
            return self
        elif automata_type == Type.NFA:
            for state in states:
                if state in verified_state:
                    continue
                for symbol in self.__alphabet.get_alphabet():
                    try:
                        actual_state = self.read(state, symbol)
                    except:
                        actual_state = set()
                    _actual_state = {''.join(final) for final in actual_state}
                    states.append(_actual_state)
                    actual_transition = Transition(state, symbol, _actual_state)
                    transitions.add(actual_transition)
                verified_state.add(frozenset(state))
        return Automata(self.__alphabet, verified_state, self.__initial_state, self.__final_states, list(transitions))


"""
TODO
1- CHECK AUTOMATA TYPE (done)
2- CONVERT TO DFA
"""

if __name__ == '__main__':
    automata = Automata(['1', '0'], ['a', 'b'], 'a', ['b'],
                        [('a', '0', 'a'), ('a', '1', 'b'), ('b', '1', 'b'), ('b', '0', 'a')])
    automata = Automata(['1', '0'], ['a', 'b'], 'a', ['b'],
                        [('a', '0', 'a'), ('a', '1', 'a'), ('a', '1', 'b'), ('b', '1', 'b'), ('b', '0', 'a')])
    automata2 = automata.convert_to_dfa()

    automata
