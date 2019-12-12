from PyQt5.QtWidgets import QAction


class HAction(QAction):
    def __init__(self, name: str, **arg):
        arg.setdefault('icon', '')
        if arg['icon']:
            super().__init__(arg['icon'], name)
        else:
            super().__init__(name)

        arg.setdefault('status_tip', name)
        arg.setdefault('shortcut', '')

        arg.setdefault('slot', [])

        self.setStatusTip(arg['status_tip'])
        self.setShortcut(arg['shortcut'])

        if arg['slot']:
            slot = arg['slot']

            if callable(slot):
                func = slot
                arg = []
            else:
                if not isinstance(slot, list):
                    raise TypeError(f'slot : Expected list but recieved {type(slot)}')
                if len(slot) > 1:
                    func = slot[0]
                    if len(slot) == 1:
                        arg = []
                    elif isinstance(slot[1], (str, int)):
                        arg = [slot[1]]
                    elif not isinstance(slot[1], (list, tuple)):
                        raise TypeError(f'slot[1]: Expected list or tuple or string but recieved {type(slot[1])}')
                    else:
                        arg = slot[1]

            self.triggered.connect(lambda: func(*arg))
