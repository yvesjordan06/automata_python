class Alphabet:
    def __init__(self, *args):
        self.__alphabet = set()
        for arg in args:
            if isinstance(arg, (list, set)):
                self.__alphabet = self.__alphabet.union({str(x) for x in arg})
            else:
                self.__alphabet = self.__alphabet.union({str(arg)})

    def add_symbol(self, symbol):
        if not isinstance(symbol, (str, int)):
            raise TypeError(f'type str expected got {type(symbol)}')
        self.__alphabet.add(str(symbol))

    def update(self, s):
        if not isinstance(s, Alphabet):
            raise TypeError('Alphabet expected')
        self.__alphabet.update(s.get_alphabet())

    def remove_symbol(self, symbol):
        if not isinstance(symbol, (str, int)):
            raise TypeError(f'type str expected got {type(symbol)}')
        try:
            self.__alphabet.remove(str(symbol))
        except KeyError:
            raise KeyError(f'{symbol} not found in alphabet')

    def __str__(self):
        """Retourne un representation de l'alphabet en chaine de character
                        Utilisation
                        a = Alphabet(['1','2'])
            >print(a)
            {'1', '2'}
        """
        return str(self.__alphabet)

    def __len__(self):
        # Retourne la longeur de l'alphabet
        return len(self.__alphabet)

    def __contains__(self, symbol):
        """Verifie si un symbole est inclu dans l'alphabet
                Utilisation
                a = Alphabet(['1','2'])
                >'x' in a
                False
        """
        return str(symbol) in self.__alphabet

    def get_alphabet(self):
        # Retourne l'aphabet
        return self.__alphabet

    def set_alphabet(self, alphabet):
        # Definie les element de l'aphabet
        self.__alphabet = alphabet

    def has_word(self, word):
        """Verifie si un un mot appertient a l'alphabet
                Utilisation
                a = Alphabet(['a','c'])
                >a.has_word('aba)
                False
        """
        try:
            iterator = iter(str(word))
            for symbol in iterator:
                if symbol not in self:
                    raise Exception(symbol + " is not in alphabet")
        except Exception as error:
            print('Alphabet Error:', error)
            return False
        else:
            return True

    def word_list(self, len):
        """Retourne une liste de mot de longeur 'len' passé en parametre
                Utilisation
                a = Alphabet(['a','c'])
                >a.word_list('2)
                ['aa','ac','ca','cc']
        """
        if len == 0:
            return set()
        elif len == 1:
            return self.__alphabet
        else:
            return {symbol + word for symbol in self.__alphabet for word in self.word_list(len - 1)}
