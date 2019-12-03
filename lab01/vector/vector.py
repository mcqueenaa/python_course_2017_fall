#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt


class Vector(list):

    """
    Class Vector is n-dimensional geometry vector.
    Examples of usage:
    >>> a = Vector([1, 2, 3, 4])
    >>> b = Vector([0, 1, -1, -4])
    >>> a
    Vector([1, 2, 3, 4])
    >>> a + b
    Vector([1, 3, 2, 0])
    >>> a - b
    Vector([1, 1, 4, 8])
    >>> print(a * b)
    Vector([0, 2, -3, -16])
    >>> print(b / a)
    Vector([0.0, 0.5, -0.3333333333333333, -1.0])
    >>> a == Vector([1, 2, 3, 4])
    True
    >>> a.append(144)
    >>> print(a)
    Vector([1, 2, 3, 4, 144])
    >>> len(a)
    5
    >>> a.ndim() == 5
    True
    >>> a[1] == 2
    True
    >>> a[-1] = 5
    >>> a[-1]
    5
    >>> a.clear()
    >>> not a
    True
    >>> b.reverse()
    >>> b
    Vector([-4, -1, 1, 0])
    >>> abs(b) == sqrt(16 + 1 + 1 + 0)
    True
    >>> b.argmin()
    0
    >>> b[b.argmin()] == -4
    True
    >>> b.argmax()
    2
    >>> b[b.argmax()] == 1
    True
    >>> [i for i in b] == [-4, -1, 1, 0]
    True
    """

    def __init__(self, v):
        self.v = v
        self.counter = 0
        if not isinstance(v, list):
            raise ValueError('v must be list type')

    def __iter__(self):
        return iter(self.v)

    def __str__(self):
        return 'Vector(%s)' % str(self.v)

    __repr__ = __str__

    def __add__(self, other):
        arr = []
        for (i, j) in zip(self.v, other.v):
            arr.append(i + j)
        return Vector(arr)

    def __sub__(self, other):
        arr = []
        for (i, j) in zip(self.v, other.v):
            arr.append(i - j)
        return Vector(arr)

    def __mul__(self, other):
        arr = []
        for (i, j) in zip(self.v, other.v):
            arr.append(i * j)
        return Vector(arr)

    def __truediv__(self, other):
        arr = []
        for (i, j) in zip(self.v, other.v):
            arr.append(i / j)
        return Vector(arr)

    def append(self, a):
        self.v.append(a)

    def ndim(self):
        return len(self.v)

    __len__ = ndim

    def __getitem__(self, index):
        return self.v.__getitem__(index)

    def __setitem__(self, index, value):
        return self.v.__setitem__(index, value)

    def clear(self):
        return self.v.clear()

    def reverse(self):
        self.v = self.v[::-1]

    def __abs__(self):
        k = 0
        for i in self.v:
            k += i ** 2
        return sqrt(k)

    def argmin(self):
        return self.v.index(min(self.v))

    def argmax(self):
        return self.v.index(max(self.v))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
