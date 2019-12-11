class State(frozenset):
    def __init__(self, state):
        """

        Returns:
            object: 
        """
        super(State, self).__init__()

    def to_string(self):
        return ''.join(self)
