from unittest import TestCase
from makamte import AFD


class TestAFD(TestCase):
    def setUp(self):
        self.automate = AFD(['1', '0'], ['a', 'b'], 'a', ['b'],
                            [('a', '0', 'a'), ('a', '1', 'b'), ('b', '1', 'b'), ('b', '0', 'a')])

    def test_ajouter_symboles(self):
        self.automate.ajouter_symboles(self.automate.alphabet, 'c')
        self.assertTrue(self.automate.alphabet.__contains__('c'))

    def test_reconnaitre_mot(self):
        self.assertFalse(self.automate.reconnaitre_mot('00000'))

    def test_reconnaitre_mot2(self):
        self.assertTrue(self.automate.reconnaitre_mot('1'))

    def test_reconnaitre_mot3(self):
        self.assertTrue(self.automate.reconnaitre_mot('111111'))

    def test_reconnaitre_mot4(self):
        self.assertFalse(self.automate.reconnaitre_mot('000001q'))
