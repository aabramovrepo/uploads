class CustomClass:

    def __init__(self, param_a: bool, param_b: float) -> None:
        self.param_a = param_a
        self.param_b = param_b

    @property
    def param_a(self) -> bool:
        return self._param_a

    @param_a.setter
    def param_a(self, value: bool) -> None:
        self._param_a = bool(value)

    @property
    def param_b(self) -> float:
        return self._param_b

    @param_b.setter
    def param_b(self, value: float) -> None:
        self._param_b = float(value)


def main() -> None:
    # correct object initialization
    obj = CustomClass(True, 3.14)
    print(f'param_a = {obj.param_a}, param_b = {obj.param_b}')

    # messing up the parameter order causes issues that cannot be caught early
    # at runtime, use mypy to detect such problems
    #
    # float is casted to bool: 0.0 - False, everything else - True
    # bool is casted to float: True - 1.0, False - 0.0
    obj = CustomClass(3.14, True)
    print(f'param_a = {obj.param_a}, param_b = {obj.param_b}')

    obj = CustomClass(0.0, False)
    print(f'param_a = {obj.param_a}, param_b = {obj.param_b}')

    # workaround - pass parameters by their names
    obj = CustomClass(param_b=3.14, param_a=True)
    print(f'param_a = {obj.param_a}, param_b = {obj.param_b}')

    obj = CustomClass(param_a=False, param_b=0.11)
    print(f'param_a = {obj.param_a}, param_b = {obj.param_b}')


if __name__ == '__main__':
    main()
