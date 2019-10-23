from typing import Union


def get_with_spaces(string: str, length: int = 4) -> str:
    arr = []
    for i in range(len(string), 0, -length):
        start = i - length
        if start < 0:
            start = 0
        temp = string[start: i]
        arr.append(temp)
    arr = arr[::-1]
    return ' '.join(arr)


def get_with_leading_zeroes(string: str, length: int = 16) -> str:
    base_length = len(string)
    assert base_length <= length
    final_string = string.zfill(length)
    return final_string


def get_inverse(string: str) -> str:
    base_length = len(string)
    zeroes = string.count('0')
    ones = string.count('1')
    assert zeroes + ones == base_length

    inverse_string = string.replace('0', '_', ).replace('1', '0').replace('_', '1')
    return inverse_string


def get_in_additional_code_from_int(number: int) -> str:
    number_minus = number - 1
    number_bin = bin(number_minus)[2:]
    number_zeroes = get_with_leading_zeroes(number_bin)
    number_inverse = get_inverse(number_zeroes)
    result = number_inverse

    return result


def get_in_additional_code_from_string(string: str) -> str:
    number = int(string, base=2)
    result = get_in_additional_code_from_int(number)
    return result


def get_in_additional_code(input_union: Union[int, str]) -> str:
    if type(input_union) == int:
        return get_in_additional_code_from_int(input_union)
    else:
        return get_in_additional_code_from_string(input_union)


def main():
    # base = '011001110111'
    # print('base:       ', base)
    #
    # with_zeroes = get_with_leading_zeroes(base)
    # print('with_zeroes:', with_zeroes)
    #
    # inverse = get_inverse(with_zeroes)
    # print('inverse:    ', inverse)

    # string_input = '100010001011'
    # string_with_zeroes = get_with_leading_zeroes(string_input)
    # print('string_with_zeroes:', string_with_zeroes)
    #
    # first_code = get_in_additional_code(string_with_zeroes)
    # print('first_code:', first_code)
    #
    # second_code = get_in_additional_code(first_code)
    # print('second_code:', second_code)
    #
    # equality_condition = string_with_zeroes == second_code
    # print('equality_condition:', equality_condition)

    base_str = '1000100110001001'
    base_int = int(base_str, base=2)
    print('base_str:', base_str)
    print('base_int:', base_int)
    print()

    addition_str = get_in_additional_code(base_str)
    additional_ind = int(addition_str, base=2)
    print('addition_str:', addition_str)
    print('additional_ind:', additional_ind)


if __name__ == '__main__':
    main()
