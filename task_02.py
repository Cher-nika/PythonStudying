"""
Your task:
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Checks if the input sequence is a Fibonacci sequence"""
    if len(data) == 0:
        return False

    if len(data) == 1:
        if data[0] == 0:
            return True
        else:
            return False

    if len(data) == 2:
        if data[0] == 0 and data[1] == 1:
            return True
        else:
            return False

    else:

        is_fib = True

        for index_i, item in enumerate(data):
            if data[index_i] == data[-2]:
                return is_fib

            if data[index_i]+data[index_i+1] == data[index_i+2]:
                continue
            else:
                is_fib = False
