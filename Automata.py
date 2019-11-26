from Alphabet import Alphabet
from Transition import Transition


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
            elif isinstance(transition, (tuple)):
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
        try:
            if start not in self.__states:
                raise Exception(str(start) + '  not found in Automata states')
            if symbol not in self.__alphabet:
                raise Exception(str(symbol) + '  not found in Automata alphabet')
            for transition in self.__transitions:
                if str(start) == transition.get_from() and str(symbol) == transition.get_on():
                    return transition.get_to()
            raise Exception('Transition from: ' + start + ' on: ' + symbol + ' does not exist in Automata')
        except Exception as error:
            print('Transition Read Error:', error)
            raise Exception
    def knows_word(self, word):
        next = self.__initial_state
        try:
            for symbol in str(word):
                next = self.read(next, symbol)
            if next in self.__final_states:
                return True
            else:
                return False
        except Exception as error:
           return False
            


a = Alphabet(1, 2, [1, 2, 3], {0, 1, 2, 3, 'a'})
automata = Automata(a, ('a', 'b', 'c'), 'a', 'c', [('a', 1, 'c')])
automata.add_transition(('f', 8, '6'))
pass
