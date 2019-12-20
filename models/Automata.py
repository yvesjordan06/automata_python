import time

from PyQt5.QtCore import pyqtSignal, QObject
from graphviz import Digraph

from models.Alphabet import Alphabet
from models.State import State
from models.Transition import Transition


class Type:
    DFA = 'Definite Finite State Automata'
    NFA = 'Non-Definite Finite State Automata'
    eNFA = f'Epsilon {NFA}'


def convert_set_of_state_to_state(set_states: set):
    state_list = list()
    for state in set_states:
        for character in state:
            state_list.append(character)
    return State(state_list)


class Automata(QObject):
    updated = pyqtSignal()
    statecount = 0

    def __init__(self, alphabet=None, states=None, initial_state=None, final_states=None,
                 transitions=None, **kwargs):
        super().__init__()
        kwargs.setdefault('name', 'Automata')
        self.name = kwargs['name']
        self.__alphabet = Alphabet('')
        self.__states = set()
        self.__initial_state = None
        self.__final_states = set()
        self.__transitions = set()

        if alphabet:
            self.__alphabet = alphabet if isinstance(
                alphabet, Alphabet) else Alphabet(alphabet)
            for x in states:
                if isinstance(x, (str, int)):
                    self.__states.add(State({str(x)}))
                elif isinstance(x, (set, list, tuple, frozenset, State)):
                    self.__states.add(State({''.join(x)}))
        if initial_state:
            if isinstance(initial_state, (str, int)):
                self.__initial_state = State({str(initial_state)})
            else:
                self.__initial_state = State({''.join(initial_state)})
        if final_states:
            if isinstance(final_states, (str, int)):
                self.__final_states.add(State({str(final_states)}))
            else:
                for state in final_states:
                    if isinstance(state, (str, int)):
                        self.__final_states.add(State({str(state)}))
                    else:
                        self.__final_states.add(State({''.join(state)}))
        if transitions:
            if isinstance(transitions, list):
                for trans in transitions:
                    self.add_transition(trans)
            else:
                self.add_transition(transitions)

    def link_close(self):
        if len(self.__initial_state) == 1:
            start = State({''.join(self.__initial_state) + '0'})
            end = State({'f' + ''.join(list(self.__final_states)[-1])})
            actual_start = self.__initial_state.copy()
            actual_end = list(self.__final_states)[-1].copy()
            self.__states.add(start)
            self.__states.add(end)
            self.__initial_state = start
            self.__final_states = {end}
            firstTrans = Transition(start, '', actual_start)
            linkTrans = Transition(start, '', end)
            loopTrans = Transition(actual_end, '', actual_start)
            endTrans = Transition(actual_end, '', end)
            self.add_transition(firstTrans)
            self.add_transition(loopTrans)
            self.add_transition(endTrans)
            self.add_transition(linkTrans)

        else:
            print('Impossible sur l\'automate')
        return self

    def iter(self, value: str):
        self.__alphabet.add_symbol(str(value))
        if self.__initial_state is None or len(self.__final_states) == 0:
            self.__initial_state = State({f'i{self.statecount}'})
            self.__final_states = [State({f'f{self.statecount}'})]
            self.__states.add(State({f'i{self.statecount}'}))
            self.__states.add(State({f'f{self.statecount}'}))
            trans = Transition(self.__initial_state, str(value), list(self.__final_states)[-1])
            self.add_transition(trans)
            Automata.statecount += 1

        else:
            s = State({f'S{self.statecount}'})
            final = list(self.__final_states)[-1]
            self.__states.add(s)
            trans = Transition(final, str(value), s)
            self.__final_states = [s]
            self.add_transition(trans)
        return self

    def iter_with_automata(self, value):
        value_final = value.get_final_states()[-1]
        value_initial = value.get_initial_state()
        actual_final = list(self.__final_states)[-1]
        self.__final_states = [value_final]
        self.__states.update(value.get_states())
        self.__alphabet.update(value.get_alphabet())
        self.__transitions.update(value.get_transitions())
        print(value.get_states())
        print(self.__states)
        trans = Transition(actual_final, '', value_initial)
        self.add_transition(trans)
        return self

    def union_with_automata(self, value):
        value_final = value.get_final_states()[-1]
        value_initial = value.get_initial_state()
        actual_final = list(self.__final_states)[-1]
        self.__states.update(value.get_states())
        self.__transitions.update(value.get_transitions())
        self.__alphabet.update(value.get_alphabet())
        print(value.get_states())
        print(self.__states)
        start = Transition(self.get_initial_state(), '', value_initial)
        end = Transition(value_final, '', actual_final)
        self.add_transition(start)
        self.add_transition(end)
        return self

    def union(self, value: str):
        self.__alphabet.add_symbol(str(value))

        if self.__initial_state is None or len(self.__final_states) == 0:
            self.__initial_state = State({f'i{self.statecount}'})
            self.__final_states = [State({f'f{self.statecount}'})]
            self.__states.add(State({f'i{self.statecount}'}))
            self.__states.add(State({f'f{self.statecount}'}))
            trans = Transition(self.__initial_state, str(value), list(self.__final_states)[-1])
            self.add_transition(trans)
            Automata.statecount += 1
        else:
            initial = self.__initial_state
            final = list(self.__final_states)[-1]
            trans = Transition(initial, str(value), final)
            self.add_transition(trans)
        return self

    def get_alphabet(self):
        return self.__alphabet

    def add_symbol(self, symbol):
        if self.__alphabet:
            self.__alphabet.add_symbol(symbol)
        else:
            self.__alphabet = Alphabet(symbol)
        self.updated.emit()

    def get_states(self):
        return self.__states

    def get_states_string(self):
        string = set()
        for state in self.__states:
            string.add(''.join(state))
        return string

    def get_initial_state(self):
        return self.__initial_state

    def get_final_states(self):
        return self.__final_states

    def get_initial_state_string(self):
        return ''.join(self.__initial_state) if self.__initial_state else None

    def get_final_states_string(self):
        string = set()
        for state in self.__final_states:
            string.add(''.join(state))
        return string

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
                self.updated.emit()
            elif isinstance(transition, tuple):
                _from = str(list(transition)[0])
                _on = str(list(transition)[1])
                _to = str(list(transition)[2])
                new_trans = Transition(_from, _on, _to)
                self.__validate_transition(new_trans)
                self.__transitions.add(new_trans)
                self.updated.emit()
            else:
                raise Exception(
                    'Cannot read transition expected format \n Expected Format (from, on, to)')
        except Exception as error:
            print('Transition Error:', error)

    def delete_transition(self, transition: Transition):
        if not isinstance(transition, Transition):
            raise TypeError(f'type Transition expected but got {type(transition)}')
        try:
            self.__transitions.remove(transition)
        except KeyError:
            raise KeyError(f'Transition {str(transition)} not found')

    def add_state(self, state):
        local_state = set()
        if isinstance(state, (State, set, frozenset, list, tuple)):
            local_state = State(state)
        else:
            local_state = State({str(state)})
        self.__states.add(local_state)
        self.updated.emit()

    def remove_state(self, state):
        local_state = set()
        if isinstance(state, (State, set, frozenset, list, tuple)):
            local_state = State(state)
        else:
            local_state = State({str(state)})
        try:
            self.__states.remove(local_state)
            self.updated.emit()
        except KeyError:
            raise KeyError(f'State {local_state} not found')

    def set_initial_state(self, state):
        local_state = set()
        if isinstance(state, (State, set, frozenset, list, tuple)):
            local_state = State(state)
        else:
            local_state = State({str(state)})
        if local_state not in self.__states:
            raise ValueError(f'Cannot set state {local_state} as initial state: State not found in Automata states')
        self.__initial_state = local_state
        self.updated.emit()

    def add_final_state(self, state):
        local_state = set()
        if isinstance(state, (State, set, frozenset, list, tuple)):
            local_state = State(state)
        else:
            local_state = State({str(state)})
        if local_state not in self.__states:
            raise ValueError(f'Cannot set state {local_state} as final state: State not found in Automata states')
        self.__final_states.add(local_state)
        self.updated.emit()

    def remove_final_state(self, state):
        local_state = set()
        if isinstance(state, (State, set, frozenset, list, tuple)):
            local_state = State(state)
        else:
            local_state = State({str(state)})
        try:
            self.__final_states.remove(local_state)
            self.updated.emit()
        except KeyError:
            raise KeyError(f'State {local_state} not found')

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

    def read(self, _start, symbol):
        to = list()
        start = State(_start) if isinstance(_start, (State, tuple, set)) else State({str(_start)})
        try:
            if isinstance(start, (set, State)) and len(start) > 1:
                for i in start:
                    for transition in self.__transitions:
                        if {i} == transition.get_from() and str(symbol) == transition.get_on():
                            to.append(transition.get_to())
                return to
            if start not in self.__states:
                raise Exception(str(start) + '  not found in Automata states')
            if symbol not in self.__alphabet and symbol != '':
                raise Exception(str(symbol) + '  not found in Automata alphabet')
            for transition in self.__transitions:
                if start == transition.get_from() and str(symbol) == transition.get_on():
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
            state = State(str(_state))
        else:
            state = State(_state)
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
                    closure.append(State(read))
            verified_closure.append(State(iter_state))
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
        new_final_states = set()
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
                    _actual_state = State({''.join(final) for final in actual_state})
                    states.append(_actual_state)
                    actual_transition = Transition(state, symbol, _actual_state)
                    transitions.add(actual_transition)
                verified_state.add(State(state))

                for x_state in verified_state:
                    for f_state in self.__final_states:
                        if f_state.intersection(x_state):
                            new_final_states.add(x_state)

        return Automata(self.__alphabet, verified_state, self.__initial_state, new_final_states, list(transitions))

    def minimize(self):
        if self.check_type() != Type.DFA:
            return self.convert_to_dfa().minimize()
        state_pairs = list()
        marked_pairs = list()
        temp_state = self.__states.copy()
        for state in self.__states:
            temp_state.remove(state)
            for x_state in temp_state:
                pair = {state, x_state}
                state_pairs.append(frozenset(pair))

        # Scanning pairs and marking

        for pair in state_pairs:
            if len(pair.intersection(self.__final_states)) == 1:
                marked_pairs.append(pair)
        a_state_has_been_marked = True
        while a_state_has_been_marked:
            a_state_has_been_marked = False
            for pair in state_pairs:
                if pair not in marked_pairs:
                    local_pair = list(pair)
                    for symbol in self.__alphabet.get_alphabet():
                        result_pair = set()
                        a = self.read(local_pair[0], symbol)
                        b = self.read(local_pair[-1], symbol)
                        for i in a:
                            result_pair.add(i)
                        for i in b:
                            result_pair.add(i)
                        if result_pair in marked_pairs:
                            marked_pairs.append(pair)
                            a_state_has_been_marked = True
        # Generating new set of states
        unmarked_pair = set(state_pairs).difference(set(marked_pairs))
        used_state = set()
        new_states = set()
        for state in self.__states:
            act_state = {state}
            if state in used_state:
                continue
            for pair in unmarked_pair:
                if act_state.intersection(pair):
                    used_state.update({x for x in pair})
                    act_state.update({x for x in pair})
            new_states.add(convert_set_of_state_to_state(act_state))

        # Generation new set of transitions
        read_trans = list()
        new_transitions = set()
        new_initial_state = set()
        new_final_states = set()
        for state in new_states:
            if state.intersection(self.__initial_state):
                new_initial_state = state
            for f_state in self.__final_states:
                if f_state.intersection(state):
                    new_final_states.add(state)

        for transition in self.__transitions:
            _from = transition.get_from()
            _to = transition.get_to()
            _on = transition.get_on()
            if (_from, _on) in read_trans:
                continue
            for state in new_states:
                if state.intersection(_from):
                    result = self.read(_from, _on)
                    read_trans.append((_from, _on))
                    for x_state in result:
                        for i in new_states:
                            if i.intersection(x_state):
                                trans = Transition(state, _on, i)
                                new_transitions.add(trans)

        return Automata(self.__alphabet, new_states, new_initial_state, new_final_states, list(new_transitions))

    def view(self, **kwargs):
        kwargs.setdefault('filename', f'../diagrams/automate{time.time()}')
        kwargs.setdefault('format', f'png')

        f = Digraph('Test', filename=kwargs['filename'], format=kwargs['format'])
        f.attr(label=f'Type: \n {self.check_type()}')
        f.attr(rankdir='LR', size='15,5')
        f.attr('node', shape='none', height='0', width='0')
        f.node('')
        f.attr('node', shape='doublecircle')
        for x in self.__final_states:
            f.node(x.to_string())
        f.attr('node', shape='circle')
        f.edge('', self.__initial_state.to_string())
        for t in self.__transitions:
            f.edge(t.get_from().to_string(), t.get_to().to_string(), label=t.get_on())
        return f.view()

    def temp_view(self):
        return self.view(filename='../diagrams/temp', format='png')

    def save_view(self, filename, _format):
        return self.view(filename=filename, format=_format)


"""
TODO
1- CHECK AUTOMATA TYPE (done)
2- CONVERT TO DFA
"""

example = Automata(['a', 'b'], ['q0', 'q1', 'q2', 'q3', 'q4', 'q5'], 'q0', ['q5'],
                   [
                       ('q0', 'a', 'q1'),
                       ('q0', 'b', 'q3'),
                       ('q1', 'a', 'q1'),
                       ('q1', 'b', 'q2'),
                       ('q2', 'a', 'q2'),
                       ('q2', 'b', 'q5'),
                       ('q3', 'a', 'q3'),
                       ('q3', 'b', 'q4'),
                       ('q4', 'a', 'q4'),
                       ('q4', 'b', 'q5'),
                       ('q5', 'a', 'q5'),
                       ('q5', 'b', 'q5')
                   ]
                   )
if __name__ == '__main__':
    automata = Automata(['1', '0'], ['a', 'b'], 'a', ['b'],
                        [('a', '0', 'a'), ('a', '1', 'b'), ('b', '1', 'b'), ('b', '0', 'a')])
    automata = Automata(['1', '0'], ['a', 'b'], 'a', ['b'],
                        [('a', '0', 'a'), ('a', '1', 'a'), ('a', '1', 'b'), ('b', '1', 'b'), ('b', '0', 'a')])
    automata2 = automata.convert_to_dfa()

    automata3 = Automata(['1', '0'], ['A', 'B', 'C', 'D', 'E', 'F'], 'A', ['C', 'D', 'E'],
                         [
                             ('A', 0, 'B'),
                             ('A', 1, 'C'),
                             ('B', 0, 'A'),
                             ('B', 1, 'D'),
                             ('C', 0, 'E'),
                             ('C', 1, 'F'),
                             ('D', 0, 'E'),
                             ('D', 1, 'F'),
                             ('E', 0, 'E'),
                             ('E', 1, 'F'),
                             ('F', 0, 'F'),
                             ('F', 1, 'F'),
                         ]
                         )
    b = automata.convert_to_dfa()

    automata4 = Automata(['0', '1'], ['q0', 'q1', 'q2', 'q3', 'q4'], 'q0', ['q4'],
                         [
                             ('q0', '0', 'q1'),
                             ('q0', '1', 'q3'),
                             ('q1', '0', 'q2'),
                             ('q1', '1', 'q4'),
                             ('q2', '0', 'q1'),
                             ('q2', '1', 'q4'),
                             ('q3', '0', 'q2'),
                             ('q3', '1', 'q4'),
                             ('q4', '0', 'q4'),
                             ('q4', '1', 'q4')
                         ]
                         )
    automata5 = Automata(['0', '1'], ['q0', 'q1', 'q2', 'q3', 'q4', 'q5'], 'q0', ['q3', 'q4'],
                         [
                             ('q0', '0', 'q1'),
                             ('q0', '1', 'q2'),
                             ('q1', '0', 'q2'),
                             ('q1', '1', 'q3'),
                             ('q2', '0', 'q2'),
                             ('q2', '1', 'q4'),
                             ('q3', '0', 'q3'),
                             ('q3', '1', 'q3'),
                             ('q4', '0', 'q4'),
                             ('q4', '1', 'q4'),
                             ('q5', '0', 'q5'),
                             ('q5', '1', 'q4')
                         ]
                         )
    automata6 = Automata(['a', 'b'], ['1', '2', '3', '4'], '1', ['4'],
                         [
                             ('1', 'a', '3'),
                             ('1', 'a', '2'),
                             ('2', 'a', '4'),
                             ('3', 'a', '3'),
                             ('3', 'b', '4'),
                             ('4', 'b', '2'),
                         ]
                         )

    automata7 = Automata(['0', '1'], ['q0', 'q1', 'q2', 'q3', 'q4'], 'q0', ['q4'],
                         [
                             ('q0', '0', 'q1'),
                             ('q0', '0', 'q0'),
                             ('q0', '1', 'q0'),
                             ('q1', '0', 'q2'),
                             ('q1', '1', 'q2'),
                             ('q2', '0', 'q3'),
                             ('q2', '1', 'q3'),
                             ('q3', '0', 'q4'),
                             ('q3', '1', 'q4'),
                         ]
                         )

    automata8 = Automata(['a', 'b'], ['q0', 'q1', 'q2', 'q3', 'q4', 'q5'], 'q0', ['q5'],
                         [
                             ('q0', 'a', 'q1'),
                             ('q0', 'b', 'q3'),
                             ('q1', 'a', 'q1'),
                             ('q1', 'b', 'q2'),
                             ('q2', 'a', 'q2'),
                             ('q2', 'b', 'q5'),
                             ('q3', 'a', 'q3'),
                             ('q3', 'b', 'q4'),
                             ('q4', 'a', 'q4'),
                             ('q4', 'b', 'q5'),
                             ('q5', 'a', 'q5'),
                             ('q5', 'b', 'q5')
                         ]
                         )
    # automata8.view()
    # automata8.minimize().view()
    four_min = automata4.minimize()
