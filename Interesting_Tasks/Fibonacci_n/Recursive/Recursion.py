#!/usr/bin/env python3


def fib(n):
    if n == 1 or n == 2:
        result = 1

    else:
        result = fib(n-1) + fib(n-2)

    return result
