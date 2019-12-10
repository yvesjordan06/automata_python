def find_index_of_4(number, start=0):
    try:
        return number.index('4', start)
    except ValueError  as error:
        return -1


def case_finder(_number):
    s_number = [n for n in str(_number)]
    number = int(_number)
    length = len(s_number) - 1
    index = find_index_of_4(s_number)
    reducer = 0
    while index >= 0:
        power = length - index
        reducer += 10 ** power
        index = find_index_of_4(s_number, index + 1)
    return str(number - reducer) + ' ' + str(reducer)


cases = int(input('Number of cases: '))
cases_list = list()
for case in range(cases):
    cases_list.append(int(input('Case ' + str(case + 1) + ':')))
i = 1
for case in cases_list:
    print('Case #' + str(i) + ':' + ' ' + case_finder(case))
    i += 1


# Problem 2 Lydia Maze

class Mase:
    def __init__(self, size):
        self.__size = size

    def validate_path(self, _path):
        path = [str(x) for x in _path]
        n_south = path.count('S')
        n_east = path.count('E')
        if n_south > self.__size or n_east > self.__size:
            raise Exception('Invalid path')
        return path

    def find_move_against(self, _path):
        try:
            path = self.validate_path(_path)
        except Exception as error:
            print('Path Error:', error)
        else:
            my_path = list()
            move_not_done = ''
            for i in path:
                if i == move_not_done:
                    move_not_done = ''
                else:
                    if i == 'E':
                        my_path.append('S')
                        my_path.append('E')
                        move_not_done = 'S' if move_not_done == '' else move_not_done
                    else:
                        my_path.append('E')
                        my_path.append('S')
                        move_not_done = 'E' if move_not_done == '' else move_not_done
            return my_path;


# case = input('Enter number of test case :')
""" for i in range(int(case)):
    _case = input('Enter case '+ str(i) +' :')
    print(case_finder(_case)) """
