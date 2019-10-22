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


def main():
    base = '011001110111'
    print('base:', base)

    with_zeroes = get_with_leading_zeroes(base)
    print('with_zeroes:', with_zeroes)

    inverse = get_inverse(with_zeroes)
    print('inverse:    ', inverse)


if __name__ == '__main__':
    main()
