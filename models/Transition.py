from models.State import State


class Transition:
    def __init__(self, _from, _on, _to=None):
        self.__from = State({str(_from)}) if isinstance(_from, (str, int)) else State({''.join(_from)})
        if _to is None:
            self.__to = None
        elif isinstance(_to, (str, int)):
            self.__to = State({str(_to)})
        else:
            self.__to = State({''.join(_to)})
        self.__on = str(_on)

    def __repr__(self):
        return 'Transtion (' + str(self) + ')'

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def get_from(self) -> State:
        return self.__from

    def get_to(self) -> State:
        return self.__to

    def get_on(self) -> str:
        return self.__on

    def get_transition(self):
        return {'from': self.__from, 'on': self.__on, 'to': self.__to}

    def __str__(self):
        return "from: " + ''.join(self.__from) + " , " + "on: " + self.__on + " , " + "to: " + ''.join(self.__to)

