from typing import Dict

from helper import get_with_leading_zeroes


class Summator:
    def __init__(self):
        self.__flags: Dict[str, int] = dict()
        self.__keys = ['SF', 'ZF', 'PF', 'AF', 'CF', 'OF']
        self.__refresh_flags()

    def __refresh_flags(self):
        self.__flags = {key: 0 for key in self.__keys}

    def sum_two(self, number_first_raw: str, number_second_raw: str):
        number_first, number_second = map(get_with_leading_zeroes, [number_first_raw, number_second_raw])
        assert len(number_first) == len(number_second)
        print('number_first ', number_first)
        print('number_second', number_second)

        result = ''

        div = 0
        for first_char, second_char, index in zip(number_first[::-1], number_second[::-1], range(len(number_first))):
            first_int = int(first_char)
            second_int = int(second_char)
            print(first_int, second_int)
            print('first_int:', first_int)
            print('second_int:', second_int)

            temp_sum = first_int + second_int + div
            print('temp_sum:', temp_sum)

            div, mod = divmod(temp_sum, 2)
            print(div, mod)
            print('div:', div)
            print('mod:', mod)
            result += str(mod)

            print()
        result = result[::-1]
        print('result:', result)


def main():
    number_first = '100010001011'
    number_second = '111011001110111'

    summator = Summator()
    summator.sum_two(number_first, number_second)


if __name__ == '__main__':
    main()
