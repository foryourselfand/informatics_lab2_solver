from pprint import pprint
from typing import Dict

from helper import get_in_additional_code, get_with_leading_zeroes
from input_tasks_getter import InputTasksGetter
from task_solver_B import TaskSolverB
from task_solver_X import TaskSolverX


class TaskSolverY:
    def __init__(self):
        self.Y: Dict = dict()

    def solve_task(self, x: Dict, b: Dict):
        print('Task #6')
        print(f'ОДЗ = [2^15; 2^15 - 1] = [{2 ** 15}; {2 ** 15 - 1}]')

        print('Task #7')
        for index in range(1, len(b) + 1):
            self.solve_single(x[index], b[index], index)

    def solve_single(self, x_elem: int, b_elem: str, index: int):
        x_index = f'X{index}(10)'
        b_index = f'B{index}(2)'
        y_index = f'Y{index}(10)'

        from_b_to_y = f'{b_index} -> {y_index}'

        b_with_zeroes = get_with_leading_zeroes(b_elem)

        b_first_bit = int(b_with_zeroes[0])

        elem_to_translate = b_elem
        sign = 1

        if b_first_bit == 1:
            b_additional_code = get_in_additional_code(b_elem)

            elem_to_translate = b_additional_code
            sign = -1

        translated_number = sign * int(elem_to_translate, base=2)

        equality_format = '{translated_number}(10) {equality_sign} {x_index}{equality_addition}'
        equality_sign = '='
        equality_addition = ''

        if translated_number != x_elem:
            equality_sign = '≠'
            equality_addition = f' ≠ {x_elem}(10)'

        equality_expression = equality_format.format(translated_number=translated_number,
                                                     equality_sign=equality_sign,
                                                     x_index=x_index,
                                                     equality_addition=equality_addition)

        full_line = f'{from_b_to_y} = {equality_expression}'
        print(full_line)


def main():
    input_tasks_getter = InputTasksGetter()
    # input_task = input_tasks_getter.get_input_task(3)
    input_task = (2187, 30327)

    task_solver_x = TaskSolverX()
    task_solver_x.solve_task(input_task)
    x: Dict = task_solver_x.get_x()
    print()

    task_solver_b = TaskSolverB()
    task_solver_b.solve_task(x)
    b: Dict = task_solver_b.get_b()
    print()

    task_solver_y = TaskSolverY()
    task_solver_y.solve_task(x, b)


if __name__ == '__main__':
    main()
