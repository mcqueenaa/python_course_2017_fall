#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def takes(*types):
    """
    >>> @takes(int, str, float, int)
    ... def foo(*args):
    ...     print(args)
    >>> try:
    ...     args = 1, "arg1", 2.0, 11
    ...     foo(*args)
    ... except TypeError as exc:
    ...     print(str(exc))
    (1, 'arg1', 2.0, 11)
    >>> @takes(int, float, str, int)
    ... def bar(*args):
    ...     print(args)
    >>> try:
    ...     args = 1, "arg1", "kek", 12.0
    ...     foo(*args)
    ... except TypeError as exc:
    ...     print(str(exc))
    str argument in position 2 is not float object
    """
    def decorator(func):
        
        @functools.wraps(func)
        def wrapper(*fargs):
            for i, (arg, type_) in enumerate(zip(fargs, types)):
                if not isinstance(arg, type_):
                    raise TypeError(
                        "{} argument in position {} is not {} object".format(
                            type(arg).__name__, i, type_.__name__
                        )
                    )
            return func(*fargs)
        return wrapper
    return decorator


if __name__ == "__main__":
    import doctest
    doctest.testmod()
