from pprint import pprint
from typing import Dict, Tuple, List

from input_tasks_getter import InputTasksGetter
from task_solver_X import TaskSolverX
from helper import get_with_spaces, get_inverse, get_with_leading_zeroes


class TaskSolverB:
    def __init__(self):
        self.B: Dict = dict()

    def solve_task(self, x: Dict):
        for i in range(1, 7):
            self.solve_first_six(x, i)
        for i in range(7, 13):
            self.solve_last_six(x, i)

    def get_b(self):
        return self.B

    def solve_first_six(self, x: Dict, index):
        b_index = f'B{index}(2)'
        x_index = f'X{index}(10)'

        x_elem = x[index]
        x_elem_str = f'{x_elem}(10)'

        b_elem = bin(x_elem)[2:]
        self.B[index] = b_elem
        b_elem_spaces = get_with_spaces(b_elem)
        b_elem_str = f'{b_elem_spaces}(2)'

        expressions = [b_index, x_index, x_elem_str, b_elem_str]
        full_line = ' = '.join(expressions)
        print(full_line)

    def solve_last_six(self, x: Dict, index):
        small_index = index - 6
        b_index_big = f'B{index}(2)'
        b_index_small = f'-B{small_index}(2)'

        temp_number = x[small_index] - 1
        elem_base = bin(temp_number)[2:]

        elem_zeroes = get_with_leading_zeroes(elem_base)

        elem_inverse = get_inverse(elem_zeroes)
        self.B[index] = elem_inverse
        elem_spaces = get_with_spaces(elem_inverse)
        elem_final = f'{elem_spaces}(2)'

        expressions = [b_index_big, b_index_small, elem_final]
        full_line = ' = '.join(expressions)
        print(full_line)


def main():
    input_tasks_getter = InputTasksGetter()
    input_task = input_tasks_getter.get_input_task(7)
    # input_task = (2187, 30327)

    task_solver_x = TaskSolverX()
    task_solver_x.solve_task(input_task)
    x: Dict = task_solver_x.get_x()
    print()

    solver_forth_b = TaskSolverB()
    solver_forth_b.solve_task(x)
    b: Dict = solver_forth_b.get_b()
    pprint(b)


if __name__ == '__main__':
    main()
