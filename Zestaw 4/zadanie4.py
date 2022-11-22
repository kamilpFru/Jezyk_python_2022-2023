from functools import singledispatch, singledispatchmethod

@singledispatch
def fun(arg):
    print('default fun', arg)

@fun.register
def _(arg: int):
    print('arg is an int', arg)

@fun.register
def _(arg: float):
    print('arg is a float', arg)


@fun.register
def _(arg: list):
    print('arg is a list', arg)

fun('hi')
fun(2)
fun(['a', 'b', 'c'])

class Sum:

    @singledispatchmethod
    @classmethod
    def sum(cls, x, y):
        print(f'default sum function: {x} + {y}')

    @sum.register(int)
    @classmethod
    def _(cls, x: int, y: int):
        print(f'sum of integers: {x} + {y} =', x + y)

    @sum.register(float)
    @classmethod
    def _(cls, x, y):
        print(f'sum of floats: {x} + {y} =', x + y)
    
s = Sum()
s.sum(1, 2)
s.sum(2.1, 4.5)
s.sum('arg', True)
