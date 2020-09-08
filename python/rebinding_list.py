from typing import List


def change_list(lst: List[int]) -> List[int]:
    print(f'change_list: lst = {lst}')  # prints [1, 2, 3]
    return lst * 2


def run(source: List[int]) -> List[int]:
    print(f'run: source = {source}')  # prints [1, 2, 3]
    source = change_list(source)
    print(f'run: source = {source}')  # prints [1, 2, 3, 1, 2, 3]
    ret = source + [4, 5]
    print(f'run: ret = {ret}')  # prints [1, 2, 3, 1, 2, 3, 4, 5]

    return ret


def change_list_mutability(lst: List[int]) -> List[int]:
    print(f'change_list_mutability: lst = {lst}')  # prints [1, 2, 3]
    lst *= 2
    return lst


def run_mutability(source: List[int]) -> List[int]:
    print(f'run_mutability: source = {source}')  # prints [1, 2, 3]
    change_list_mutability(source)  # assignment not needed!!!
    print(f'run_mutability: source = {source}')  # [1, 2, 3, 1, 2, 3]
    ret = source + [4, 5]
    print(f'run_mutability: ret = {ret}')  # prints [1, 2, 3, 1, 2, 3, 4, 5]

    return ret


def main() -> None:
    lst = [1, 2, 3]
    print(f'main: lst = {lst}')  # prints [1, 2, 3]
    ret_lst = change_list(lst)

    print(f'main: ret_lst = {ret_lst}')  # prints [1, 2, 3, 1, 2, 3]
    print(f'main: lst = {lst}')  # prints [1, 2, 3]

    print('\n\n')

    res = run(lst)

    print(f'main: res = {res}')  # prints [1, 2, 3, 1, 2, 3, 4, 5]
    print(f'main: lst = {lst}')  # prints [1, 2, 3]

    print('\n\n')

    # here we will make use of mutability
    # WARNING: Python libs (e.g. OpenCV) use rebinding
    # and do not mutate input parameters!
    res = run_mutability(lst)

    print(f'main: res = {res}')  # prints [1, 2, 3, 1, 2, 3, 4, 5]
    print(f'main: lst = {lst}')  # prints [1, 2, 3, 1, 2, 3]


if __name__ == '__main__':
    main()
