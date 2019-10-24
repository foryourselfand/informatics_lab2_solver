from typing import Dict, Tuple
from helper import get_with_leading_zeroes, get_inverse


class Summator:
    def __init__(self):
        self.SF = self.ZF = self.PF = self.AF = self.CF = self.OF = -1

    def __refresh_flags(self):
        self.SF = 0
        self.ZF = 1
        self.PF = 1
        self.AF = 0
        self.CF = 0
        self.OF = 0

    def get_sum(self, input_number_first: str, input_number_second: str) -> Tuple[str, str]:
        self.__refresh_flags()
        number_first_with_zeroes = get_with_leading_zeroes(input_number_first)
        number_second_with_zeroes = get_with_leading_zeroes(input_number_second)

        number_first_sign = int(number_first_with_zeroes[0])
        number_second_sign = int(number_second_with_zeroes[0])

        number_first = number_first_with_zeroes[::-1]
        number_second = number_second_with_zeroes[::-1]

        result = ''

        rank_out = 0
        rank_previous = 0
        for first_char, second_char, index in zip(number_first, number_second, range(len(number_first))):
            first_int = int(first_char)
            second_int = int(second_char)

            temp_sum = first_int + second_int + rank_previous

            rank_next, to_result = divmod(temp_sum, 2)
            result += str(to_result)

            rank_previous = rank_next

            if self.ZF == 1 and to_result == 1:
                self.ZF = 0

            if index < 8:
                self.PF = (self.PF + to_result) % 2

            if index == 3:
                if rank_next == 1:
                    self.AF = 1

            if index == 15:
                self.SF = to_result
                rank_out = rank_next
                if rank_next == 1:
                    self.CF = 1

                if number_first_sign == number_second_sign and self.SF != number_first_sign:
                    self.OF = 1

        full_result = result[::-1]

        return full_result, str(rank_out)

    def __str__(self):
        flags = []
        for key, value in self.__dict__.items():
            flags.append(f'{key} = {value}')
        result = '\t'.join(flags)
        return result


def main():
    summator = Summator()

    numbers = '1010101000111100', '0110101001100100'
    result, rank_out = summator.get_sum(*numbers)
    print('result:', result)
    print('rank_out:', rank_out)

    print(summator)


if __name__ == '__main__':
    main()
