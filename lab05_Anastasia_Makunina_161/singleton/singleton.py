#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def singleton(cls):
    """
    >>> @singleton
    ... class A:
    ...     pass
    >>> id(A()) == id(A()) == id(A())
    True
    """
    instances = {}

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal instances
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


if __name__ == "__main__":
    import doctest
    doctest.testmod()
