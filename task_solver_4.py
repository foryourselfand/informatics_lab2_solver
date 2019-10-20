from typing import Dict, Tuple, List

from input_tasks_getter import InputTasksGetter
from task_solver_3 import TaskSolverThird
from helper import get_with_spaces


class TaskSolverForth:
    def __init__(self):
        self.B: Dict = dict()

    def solve_task(self, x: Dict):
        print('Task #4')
        for i in range(1, 7):
            self.solve_single(x, i)

    def solve_single(self, x: Dict, index):
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


def main():
    input_tasks_getter = InputTasksGetter()
    input_tasks = input_tasks_getter.get_input_tasks()

    task_solver_third = TaskSolverThird()
    task_solver_third.solve_task(input_tasks[3])
    x: Dict = task_solver_third.get_x()

    task_solver_forth = TaskSolverForth()
    task_solver_forth.solve_task(x)


if __name__ == '__main__':
    main()
