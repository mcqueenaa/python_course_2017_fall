#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable


def chain(*args):
    """
    >>> list(chain([[["test"]]]))
    ['t', 'e', 's', 't']
    """

    for iterable in args:
        if isinstance(iterable, Iterable):
            for item in iterable:
                if item != iterable:
                    yield from chain(item)
                else:
                    yield item
        else:
            yield iterable


if __name__ == "__main__":
    import doctest
    doctest.testmod()
