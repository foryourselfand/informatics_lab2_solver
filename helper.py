def get_with_spaces(string, length: int = 4):
    arr = []
    for i in range(len(string), 0, -length):
        start = i - length
        if start < 0:
            start = 0
        temp = string[start: i]
        arr.append(temp)
    arr = arr[::-1]
    return ' '.join(arr)


def main():
    print(get_with_spaces('111011001110111'))
    print('12'.zfill(5))


if __name__ == '__main__':
    main()
