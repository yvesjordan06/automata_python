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
        self.__states = {str(x) for x in states}
        self.__initial_state = str(initial_state)
        self.__final_states = {final_states} if isinstance(
            final_states, (str, int)) else {str(x) for x in final_states}
        self.__transitions = set()
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
            if isinstance(states, list):
                for state in states:
                    if not state in self.__states:
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
            result = transition.get_from() in self.__states and transition.get_on(
            ) in self.__alphabet and transition.get_to() in self.__states
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
            if start not in self.__states:
                raise Exception(str(start) + '  not found in Automata states')
            if symbol not in self.__alphabet:
                raise Exception(str(symbol) + '  not found in Automata alphabet')
            for transition in self.__transitions:
                if str(start) == transition.get_from() and str(symbol) == transition.get_on():
                    to.append(transition.get_to())
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
            if _next in self.__final_states:
                return True
            else:
                return False
        except:
            return False or error

    def epsilon_closure(self, symbol: str) -> set:
        """
        """
        pass

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
                return  Type.NFA
            else:
                return Type.DFA
        except Exception as error:
            print('Unknown Error:', error)
"""
TODO
1- CHECK AUTOMATA TYPE (done)
2- CONVERT TO DFA
"""
