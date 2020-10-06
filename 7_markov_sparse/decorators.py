""" Quick decorator example: timing functionality """

from time import perf_counter
import functools


# the decorator: have the function print its elapsed time and its name
def timing(func):

    @functools.wraps(func)  # force the new function to have the old name
    def func_with_timer(*args, **kwargs):
        start = perf_counter()
        output = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print("{}, time taken: {:.1e}".format(func.__name__, elapsed))
        return output

    return func_with_timer


# -------------------------------------------------
# decorator example without the decorator syntax
def myfunc(x, b=3):
    return 2*b*x


def dec1():
    """ decorator test (without @ syntax) """
    y = myfunc(2)  # no decorator
    print(y)
    print('-'*20)
    myfunc_d = timing(myfunc)  # now with decorator
    y = myfunc_d(2)
    print(y)


# -------------------------------------------------
# actual decorator example
@timing  # decorates foo with timer code
def foo(y, z, c=5):
    return y + z + c


def dec2():
    """ decorator test: decorating foo with @ syntax """
    y = foo(2, 3, c=10)
    print(y)
    print("New function name: ", foo.__name__)
