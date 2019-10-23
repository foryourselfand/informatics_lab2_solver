from typing import Dict, List
from summator import Summator
from input_tasks_getter import InputTasksGetter
from task_solver_B import TaskSolverB
from task_solver_X import TaskSolverX
from task_solver_Y import TaskSolverY


class TaskSummator:
    def __init__(self):
        self.summator: Summator = Summator()
        self.expressions: List[str] = ['1 2', '2 3', '2 7', '7 8', '8 9', '1 8', '11 3']

    def solve_task(self, b: Dict):
        for index, expression_raw in enumerate(self.expressions, 1):
            self.solve_single(index, expression_raw, b)

    def solve_single(self, index, expression_raw: str, b: Dict):
        expression_split = expression_raw.split(' ')
        expression_with_b = ['B' + temp_expression for temp_expression in expression_split]
        expression_full = ' + '.join(expression_with_b)
        print(f'Expression #{index}: {expression_full}')

        expression_indexes = map(int, expression_split)
        first_index, second_index = list(expression_indexes)
        first_number, second_number = b[first_index], b[second_index]

        result_bin, rank_out = self.summator.get_sum(first_number, second_number)
        print('result_bin:', result_bin)
        print('rank_out:', rank_out)
        print(self.summator)

        print()


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

    task_summator = TaskSummator()
    task_summator.solve_task(b)


if __name__ == '__main__':
    main()
