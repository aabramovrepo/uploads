# pylint: disable=no-value-for-parameter (E1120)
# pylint: disable=unused-argument (W0613)
from functools import wraps
from typing import Any, Callable

import click


# run a-command:
# python multi_command_example.py a-command -a ab -o b PATH

# run b-command:
# python multi_command_example.py b-command -b bc -o b PATH

# options common for both commands are defined here
def command_wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    @click.option('--main-option', '-o', default='a',
                  type=click.Choice(['a', 'b', 'c']))
    @click.argument('path', type=click.Path(exists=False))
    def wrapper(ctx: click.core.Context, **kwargs: Any) -> Any:
        # store all options in the context object
        for name, value in kwargs.items():
            ctx.obj[name] = value

        # launch the app code from here
        run(ctx)
        return func()

    return wrapper


@click.group()
@click.pass_context
def main(ctx: click.core.Context) -> None:
    print('---> main')
    # ensure that ctx.obj exists and is a dict
    ctx.ensure_object(dict)


# a-command specific options have to be defined here
@main.command('a-command')
@click.option('--a-option', '-a', default='aa',
              type=click.Choice(['aa', 'ab', 'ac']))
@click.pass_context
@command_wrapper
def command_a() -> None:
    print('---> command_a')


# b-command specific options have to be defined here
@main.command('b-command')
@click.option('--b-option', '-b', default='bb',
              type=click.Choice(['ba', 'bb', 'bc']))
@click.pass_context
@command_wrapper
def command_b() -> None:
    print('---> command_b')


# the run function can access to all set parameters over context
def run(ctx: click.core.Context) -> None:
    print('---> run')
    print(ctx.command.name)
    print(ctx.obj)


if __name__ == '__main__':
    main()
