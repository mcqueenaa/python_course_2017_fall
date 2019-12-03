#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def minimum(*args, **kwargs):
    """
    The same as built-in min (exclude default parameter).
    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    >>> minimum(1, 2, 3) == min(1, 2, 3)
    True
    >>> minimum([1, 2, 3]) == min([1, 2, 3])
    True
    """

    if len(args) == 1:
        m = None
        for i in args[0]:
            if m is None:
                m = i
            else:
                if i < m:
                    m = i
    else:
        m = None
        for i in args:
            if m is None:
                m = i
            else:
                if i < m:
                    m = i
    if kwargs:
        m = None
        if 'key' in kwargs.keys():
            k = None
            for i in args[0]:
                if k is None:
                    k = kwargs['key'](i)
                    m = i
                else:
                    if kwargs['key'](i) < k:
                        k = kwargs['key'](i)
                        m = i
        else:
            for i in kwargs:
                if m is None:
                    m = i
                else:
                    if i < m:
                        m = i
    
    return m


def maximum(*args, **kwargs):
    """
    The same as built-in max (exclude default parameter).
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    >>> maximum(1, 2, 3) == max(1, 2, 3)
    True
    >>> maximum([1, 2, 3]) == max([1, 2, 3])
    True
    """

    if len(args) == 1:
        m = None
        for i in args[0]:
            if m is None:
                m = i
            else:
                if i > m:
                    m = i
    else:
        m = None
        for i in args:
            if m is None:
                m = i
            else:
                if i > m:
                    m = i
    if kwargs:
        m = None
        if 'key' in kwargs.keys():
            k = None
            for i in args[0]:
                if k is None:
                    k = kwargs['key'](i)
                    m = i
                else:
                    if kwargs['key'](i) > k:
                        k = kwargs['key'](i)
                        m = i
        else:
            for i in kwargs:
                if m is None:
                    m = i
                else:
                    if i > m:
                        m = i
                        
    return m


if __name__ == "__main__":
    import doctest
    doctest.testmod()
