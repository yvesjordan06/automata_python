from models.Automata import Automata
from models.State import State


class UnionExpression:
    def __int__(self, *args):
        self.values = [*args]


class ConcatExpression:
    def __int__(self, *args):
        self.values = [*args]


class StarExpression:
    def __int__(self, *args):
        self.values = [*args]


class IterExpression:
    def __int__(self, *args):
        self.values = [*args]


class RegularExpression:
    mutual_operators = ['|', '.', '(', ')']
    uni_operators = ['*', '+']

    def __init__(self, expression: str):
        self.expression = self.normalize(expression)

    def normalize(self, expression: str):
        exp = list(expression)
        result = list()
        try:
            for i in range(len(exp)):
                result.append(exp[i])
                if exp[i] not in self.mutual_operators and exp[i + 1] not in [*self.mutual_operators, *self.uni_operators]:
                    result.append('.')
        except IndexError:
            print(result)
            # return ''.join(result)
        finally:
            return ''.join(result)

    def toNFA(self):
        state = 0
        result: Automata = Automata()
        paranthesis = 0
        current_express = None
        current_operator = None
        op_list = []
        sub_operations = list()

        for symbol in self.expression:
            if symbol == '(':
                paranthesis += 1
            elif symbol == ')':
                paranthesis -= 1
            elif symbol in self.mutual_operators:
                if symbol == '*':
                    result.link_close()
                if symbol == '+':
                    op_list.append(symbol)
            else:
                if len(op_list) == 0:
                    result.iter(symbol)
                else:
                    op = op_list.pop()
                    if op == '+':
                        result.union(symbol)

        return result.view()

    def Solve(self):
        index = 0
        parentheses = 0
        currentexp = ''
        solvedtemp = None
        if len(self.expression) == 1:
            return Automata().iter(self.expression)
        else:
            for i in range(len(self.expression)):
                value = self.expression[i]
                if parentheses > 0:
                    if value == ')':
                        parentheses -= 1
                        solvedtemp = RegularExpression(currentexp).Solve()
                        currentexp = ''
                        continue
                    elif value == '(':
                        if len(currentexp) > 0:
                            parentheses += 1
                        continue
                    else:
                        currentexp = currentexp + value
                        continue

                if value in [*self.mutual_operators, *self.uni_operators]:
                    if value == '.':
                        res = solvedtemp or Automata().iter(self.expression[:i])
                        return res.iter_with_automata(RegularExpression(self.expression[i + 1:]).Solve())
                    if value == '|':
                        solvedtemp = solvedtemp or Automata().iter(self.expression[:i])
                        return solvedtemp.union_with_automata(RegularExpression(self.expression[i + 1:]).Solve())
                    if value == '(':
                        parentheses += 1
                    if value == ')':
                        return RegularExpression(self.expression[:i]).Solve()
                    if value == '*':
                        solvedtemp = solvedtemp or RegularExpression(self.expression[:i]).Solve()
                        solvedtemp = solvedtemp.link_close()
                        #return  solvedtemp

            if solvedtemp is not None:
                return solvedtemp


if __name__ == '__main__':
    print('running ...')
    a = RegularExpression('(ab)|((ac)|b)')
    b = a.Solve()
