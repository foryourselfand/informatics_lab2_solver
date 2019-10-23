from typing import Dict, List
from summator import Summator
from input_tasks_getter import InputTasksGetter
from task_solver_B import TaskSolverB
from task_solver_X import TaskSolverX
from helper import get_with_leading_zeroes, get_with_spaces, get_in_additional_code
from task_solver_Y import TaskSolverY


class TaskSummator:
    def __init__(self):
        self.summator: Summator = Summator()
        self.expressions: List[str] = ['1 2', '2 3', '2 7', '7 8', '8 9', '1 8', '11 3']

    def solve_task(self, x: Dict, b: Dict):
        print('Task #8')
        for index, expression_raw in enumerate(self.expressions, 1):
            self.solve_single(index, expression_raw, x, b)

    def solve_single(self, index, expression_raw: str, x: Dict, b: Dict):
        expression_split = expression_raw.split(' ')
        expression_with_b = ['B' + temp_expression for temp_expression in expression_split]
        expression_with_x = ['X' + temp_expression for temp_expression in expression_split]
        print(f'Expression #{index}')

        expression_indexes = map(int, expression_split)
        first_index, second_index = list(expression_indexes)
        first_number, second_number = b[first_index], b[second_index]
        first_number_zeroes, second_number_zeroes = list(map(get_with_leading_zeroes, [first_number, second_number]))
        first_number_spaces, second_number_spaces = list(
            map(get_with_spaces, [first_number_zeroes, second_number_zeroes]))
        first_number_x, second_number_x = x[first_index], x[second_index]
        result_x = first_number_x + second_number_x

        result_bin, rank_out = self.summator.get_sum(first_number_zeroes, second_number_zeroes)
        result_bin_spaces = get_with_spaces(result_bin)

        into_rank = '' if rank_out == '0' else '(1)'

        flags: Dict = self.summator.__dict__

        result_to_translate = result_bin
        result_sign = 1
        if flags['SF'] == 1:
            result_additional = get_in_additional_code(result_bin)
            result_to_translate = result_additional
            result_sign = -1

        result_dec = result_sign * int(result_to_translate, base=2)
        result_dec_str = f' = {result_dec}(10)'

        equality_sign = '='
        if result_dec != result_x:
            equality_sign = '≠'

        # -----------

        temp_format = '{:>7} {:>22} {:>13} {:1} {:>8} {:>10}'

        first_line = temp_format.format(f'{expression_with_b[0]}(2)', f'{first_number_spaces}(2)', '', '',
                                        f'{expression_with_x[0]}(10)', f'{first_number_x}(10)')
        second_line = temp_format.format(f'+ {expression_with_b[1]}(2)', f'{second_number_spaces}(2)', '', '',
                                         f'+ {expression_with_x[1]}(10)', f'{second_number_x}(10)')
        third_line = temp_format.format('------', '----------------------', '', '',
                                        '', '----------')
        forth_line = temp_format.format(into_rank, f'{result_bin_spaces}(2)', result_dec_str, equality_sign, '',
                                        f'{result_x}(10)')

        print(first_line)
        print(second_line)
        print(third_line)
        print(forth_line)
        print()

        # -----------
        flags_list = []
        for key, value in flags.items():
            flags_list.append(f'{key} = {value}')
        flags_str = '\t\t'.join(flags_list)
        print(flags_str)

        print()
        print()


def main():
    input_tasks_getter = InputTasksGetter()
    input_task = input_tasks_getter.get_input_task(17)
    # input_task = (2187, 30327)

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
