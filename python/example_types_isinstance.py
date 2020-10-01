class CustomClass:

    def __init__(self, param_a: bool, param_b: float) -> None:
        self.param_a = param_a
        self.param_b = param_b

    @property
    def param_a(self) -> bool:
        return self._param_a

    @param_a.setter
    def param_a(self, value: bool) -> None:
        if isinstance(value, bool):
            self._param_a = bool(value)
        else:
            raise TypeError(f'value hast to be of {bool.__name__} type, '
                            f'the given value is of {type(value)}')

    @property
    def param_b(self) -> float:
        return self._param_b

    @param_b.setter
    def param_b(self, value: float) -> None:
        if isinstance(value, float):
            self._param_b = float(value)
        else:
            raise TypeError(f'value hast to be of {float.__name__} type, '
                            f'the given value is of {type(value)}')


def main() -> None:
    # correct object initialization
    obj = CustomClass(True, 3.14)
    print(f'param_a = {obj.param_a}, param_b = {obj.param_b}')

    # messing up the parameter order
    #
    # isinstance catches this early at runtime
    # obj = CustomClass(3.14, True)
    # print(f'param_a = {obj.param_a}, param_b = {obj.param_b}')

    # obj = CustomClass(True, False)
    # print(f'param_a = {obj.param_a}, param_b = {obj.param_b}')

    # passing parameters by their names is not needed, however, could be still
    # beneficial, e.g. when having multiple parameters of the same type
    # one after another - better readability


if __name__ == '__main__':
    main()
