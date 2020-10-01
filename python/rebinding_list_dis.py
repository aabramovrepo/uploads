from dis import dis
from typing import List


def change_list(lst: List[int]) -> List[int]:
    return lst * 2


def run(source: List[int]) -> List[int]:
    source = change_list(source)
    ret = source + [4, 5]
    return ret


def change_list_mutability(lst: List[int]) -> None:
    lst *= 2  # no need to return it


def run_mutability(source: List[int]) -> List[int]:
    change_list_mutability(source)  # assignment not needed!!!
    ret = source + [4, 5]
    return ret


def main() -> None:
    lst = [1, 2, 3]
    print(f'main: lst = {lst}')  # prints [1, 2, 3]
    ret_lst = change_list(lst)

    dis(change_list)
    print()
    print()

    # print(f'main: ret_lst = {ret_lst}')  # prints [1, 2, 3, 1, 2, 3]
    # print(f'main: lst = {lst}')  # prints [1, 2, 3]
    # print('\n\n')

    res = run(lst)

    dis(run)

    return

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
