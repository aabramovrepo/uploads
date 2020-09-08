from typing import List


def change_list(lst: List[int]) -> List[int]:
    print(f'change_list: {lst}')  # prints [1, 2, 3]
    return lst * 2


def run(source: List[int]) -> List[int]:
    print(f'run: source = {source}')  # prints [1, 2, 3]
    source = change_list(source)
    print(f'run: source = {source}')  # prints [1, 2, 3, 1, 2, 3]
    ret = source + [4, 5]
    print(f'run: ret = {ret}')  # prints [1, 2, 3, 1, 2, 3, 4, 5]

    return ret


def main() -> None:
    lst = [1, 2, 3]
    print(f'main: lst = {lst}')  # prints [1, 2, 3]
    ret_lst = change_list(lst)

    print(f'main: ret_lst = {ret_lst}')  # prints [1, 2, 3, 1, 2, 3]
    print(f'main: lst = {lst}')  # prints [1, 2, 3]

    print('\n\n')

    res = run(lst)

    print(f'main: res = {res}')  # prints [1, 2, 3, 1, 2, 3, 4]
    print(f'main: lst = {lst}')  # prints [1, 2, 3]


if __name__ == '__main__':
    main()
