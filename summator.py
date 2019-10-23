from typing import Dict
from helper import get_with_leading_zeroes, get_inverse


class Summator:
    def __init__(self):
        self.__flags: Dict[str, int] = dict()
        self.__keys = ['SF', 'ZF', 'PF', 'AF', 'CF', 'OF']

    def __refresh_flags(self):
        self.__flags = {key: 0 for key in self.__keys}

    def get_sum(self, input_number_first: str, input_number_second: str) -> str:
        self.__refresh_flags()
        number_first_with_zeroes = get_with_leading_zeroes(input_number_first)
        number_second_with_zeroes = get_with_leading_zeroes(input_number_second)

        number_first = number_first_with_zeroes[::-1]
        number_second = number_second_with_zeroes[::-1]

        result = ''

        previous_rank = 0
        for first_char, second_char, index in zip(number_first, number_second, range(len(number_first))):
            first_int = int(first_char)
            second_int = int(second_char)
            # print('first_int:', first_int)
            # print('second_int:', second_int)

            temp_sum = first_int + second_int + previous_rank
            # print('temp_sum:', temp_sum)

            to_next_rank, to_result = divmod(temp_sum, 2)
            # print('to_next_rank:', to_next_rank)
            # print('to_result:', to_result)
            result += str(to_result)

            previous_rank = to_next_rank
            # print()
        final_result = result[::-1]
        # print('final_result:', final_result)

        return final_result

    # @staticmethod
    # def get_in_additional_code_from_string(string: str) -> str:
    #     string_with_leading_zeroes = get_with_leading_zeroes(string)
    #     string_inverse = get_inverse(string_with_leading_zeroes)
    #
    #     one_with_leading_zeroes = get_with_leading_zeroes('1')
    #
    #     result = Summator.get_sum(string_inverse, one_with_leading_zeroes)
    #
    #     return result


def main():
    summator = Summator()

    first_numbers = '0000100010001011', '0111011001110111'
    first_result_fact = '0111111100000010'
    first_result_temp = summator.get_sum(*first_numbers)
    print('first_result_temp:', first_result_temp)
    print(first_result_fact == first_result_temp)

    second_numbers = '0000100010001011', '1000100110001001'
    second_result_fact = '1001001000010100'
    second_result_temp = summator.get_sum(*second_numbers)
    print('second_result_temp:', second_result_temp)
    print(second_result_fact == second_result_temp)


if __name__ == '__main__':
    main()
