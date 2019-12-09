from unittest import TestCase

from models.Automata import Automata, Type


class TestAutomata(TestCase):
    def setUp(self) -> None:
        self.automata = Automata(['1', '0'], ['a', 'b'], 'a', ['b'],
                                 [('a', '0', 'a'), ('a', '1', 'b'), ('b', '1', 'b'), ('b', '0', 'a')])

    def test_has_states(self):
        self.assertTrue(self.automata.has_states('a'))
        self.assertTrue(self.automata.has_states(['a']))
        self.assertTrue(self.automata.has_states(['a', 'b']))
        self.assertFalse(self.automata.has_states('c'))
        self.assertFalse(self.automata.has_states(['a', 'c']))

    def test_add_transition(self):
        self.fail()

    def test_read(self):
        self.fail()

    def test_knows_word(self):
        self.fail()

    def test_check_type(self):
        self.assertEqual(Type.DFA, self.automata.check_type())
        self.automata.add_transition(('a', '0', 'b'))
        self.assertEqual(Type.NFA, self.automata.check_type())
        self.automata.add_transition(('a', '', 'b'))
        self.assertEqual(Type.eNFA, self.automata.check_type())
