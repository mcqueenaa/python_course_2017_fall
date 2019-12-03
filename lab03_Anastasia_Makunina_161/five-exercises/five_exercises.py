#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def map_(func, iterable):
    """
    The same as built-in map(), but generator
    >>> from collections import Generator
    >>> square = lambda x: x ** 2
    >>> isinstance(map_(square, range(10)), Generator)
    True
    >>> list(map_(square, range(10)))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    
    for i in iterable:
        yield func(i)


def zip_(*iterables):
    # https://docs.python.org/3/library/itertools.html#itertools.zip_longest
    """
    The same as built-in zip(), but generator
    >>> for i, j, k in zip_(range(3), range(4), range(-7, 0)):
    ...     print(i, j, k)
    0 0 -7
    1 1 -6
    2 2 -5
    """
    
    iterators = [iter(i) for i in iterables]
    number = len(iterators)
    if not number:
        return
    while True:
        values = []
        for ind, item in enumerate(iterators):
            try:
                value = next(item)
            except StopIteration:
                return
            values.append(value)
        yield tuple(values)


def dropwhile(predicate, iterable):
    """
    The same as itertools.dropwhile(), but generator
    >>> from collections import Generator
    >>> isinstance(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]), Generator)
    True
    >>> list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
    [6, 4, 1]
    """
    
    iterable = iter(iterable)
    for i in iterable:
        if not predicate(i):
            yield i
            break
    for i in iterable:
        yield i


def filterfalse(predicate, iterable):
    # https://docs.python.org/3/library/itertools.html#itertools.filterfalse
    """
    The same as itertools.filterfalse(), but generator
    >>> from collections import Generator
    >>> isinstance(filterfalse(lambda x: x % 2, range(10)), Generator)
    True
    >>> list(filterfalse(lambda x: x % 2, range(10)))
    [0, 2, 4, 6, 8]
    """
    
    if predicate is None:
        predicate = bool
    for i in iterable:
        if not predicate(i):
            yield i


def unique(iterable):
    """
    Generates unique values from iterable object
    >>> from collections import Generator
    >>> isinstance(unique(range(10)), Generator)
    True
    >>> list(unique([1, 1, 2, 2, 3, 1, 11, -1]))
    [1, 2, 3, 11, -1]
    """

    iterable = iter(iterable)
    arr = []
    for i in iterable:
        if i not in arr:
            arr.append(i)
            yield i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
