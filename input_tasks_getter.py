from typing import Dict, Tuple
from pprint import pprint


class InputTasksGetter:
    def __init__(self):
        self.__file_name = 'input_tasks.txt'
        self.__input_tasks: Dict[int, Tuple[int, int]] = dict()
        self.__read_input_tasks()

    def __read_input_tasks(self):
        with open(self.__file_name, 'r', encoding='utf-8') as input_file:
            for input_line in input_file.readlines():
                line = input_line.replace('\n', '')
                if line[0] == '№':
                    continue

                split_line = line.split(' ')
                for i in range(2):
                    index = i * 3
                    dict_key: int = int(split_line[index])
                    dict_value: Tuple[int, int] = tuple(map(int, split_line[index + 1: index + 3]))
                    self.__input_tasks[dict_key] = dict_value

    def get_input_task(self, variant: int = 3):
        return self.__input_tasks[variant]


def main():
    input_tasks_getter = InputTasksGetter()
    input_task = input_tasks_getter.get_input_task()
    pprint(input_task)


if __name__ == '__main__':
    main()
