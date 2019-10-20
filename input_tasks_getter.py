from typing import Dict, Tuple
from pprint import pprint


class InputTasksGetter:
    def __init__(self):
        self.file_name = 'input_tasks.txt'

    def get_input_tasks(self):
        input_tasks: Dict[int, Tuple[int, int]] = dict()
        with open(self.file_name, 'r', encoding='utf-8') as input_file:
            for input_line in input_file.readlines():
                line = input_line.replace('\n', '')
                if line[0] == '№':
                    continue

                split_line = line.split(' ')
                for i in range(2):
                    index = i * 3
                    dict_key: int = int(split_line[index])
                    dict_value: Tuple[int, int] = tuple(map(int, split_line[index + 1: index + 3]))
                    input_tasks[dict_key] = dict_value
        return input_tasks


def main():
    input_tasks_getter = InputTasksGetter()
    input_tasks = input_tasks_getter.get_input_tasks()
    pprint(input_tasks)
    print(input_tasks[3])


if __name__ == '__main__':
    main()
