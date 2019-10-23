from typing import Tuple, Dict, Union, List
from pprint import pprint

from input_tasks_getter import InputTasksGetter


class TaskSolverX:
    def __init__(self):
        self.X: Dict[Union[str, int], Union[str, int]] = {1: 'A',
                                                          2: 'C',
                                                          3: 'A + C',
                                                          4: 'A + C + C',
                                                          5: 'C - A',
                                                          6: '65536 - X4'}
        self.signs = ['+', '-']

    def solve_task(self, input_task: Tuple[int, int]):
        self.X['A'], self.X['C'] = input_task
        self.solve_first_six()
        self.solve_last_six()
        # pprint(self.X)

    def get_x(self) -> Dict[Union[str, int], Union[str, int]]:
        return self.X

    def solve_first_six(self):
        for i in range(1, 7):
            self.make_full_expression_first_six(i)

    def solve_last_six(self):
        for i in range(7, 13):
            self.make_full_expression_last_six(i)

    def make_full_expression_first_six(self, index: int):
        expressions: List[str] = list()

        x_index = f'X{index}'
        expressions.append(x_index)

        raw_expression = self.X[index]
        expressions.append(raw_expression)

        proceed_expression = raw_expression
        for old_elem in ['A', 'C', 'X4']:
            if old_elem[0] == 'X':
                new_elem = self.X[int(old_elem[1:])]
            else:
                new_elem = self.X[old_elem]
            proceed_expression = proceed_expression.replace(old_elem, str(new_elem))
        expressions.append(proceed_expression)

        eval_flag = False
        for sign in self.signs:
            if sign in raw_expression:
                eval_flag = True
                break

        if eval_flag:
            eval_expression = str(eval(proceed_expression))
            expressions.append(eval_expression)
            self.X[index] = int(eval_expression)
        else:
            self.X[index] = int(proceed_expression)

        full_line = ' = '.join(expressions)
        print(full_line)

    def make_full_expression_last_six(self, index: int):
        expressions: List[str] = list()
        big_index = index

        str_big_index = f'X{big_index}'
        expressions.append(str_big_index)

        small_index = big_index - 6
        str_small_index = f'-X{small_index}'
        expressions.append(str_small_index)

        new_elem = -self.X[small_index]
        expressions.append(str(new_elem))
        self.X[big_index] = int(new_elem)

        full_line = ' = '.join(expressions)
        print(full_line)


def main():
    input_tasks_getter = InputTasksGetter()
    input_task = input_tasks_getter.get_input_task()
    # input_task = (2187, 30327)

    task_solver_x = TaskSolverX()
    task_solver_x.solve_task(input_task)


if __name__ == '__main__':
    main()
