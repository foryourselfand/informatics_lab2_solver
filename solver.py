from sys import argv
from typing import Dict

from input_tasks_getter import InputTasksGetter
from task_solver_B import TaskSolverB
from task_solver_X import TaskSolverX
from task_solver_Y import TaskSolverY
from task_summator import TaskSummator


def main():
    variant = 3 if len(argv) != 2 else int(argv[1])

    input_tasks_getter = InputTasksGetter()
    input_task = input_tasks_getter.get_input_task(variant)

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
    print()

    task_summator = TaskSummator()
    task_summator.solve_task(x, b)


if __name__ == '__main__':
    main()
