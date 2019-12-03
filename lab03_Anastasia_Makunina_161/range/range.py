#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Sequence
from collections import Iterator


class RangeIterator(Iterator):

    def __init__(self, rangeobj):
        self.rangeobj = rangeobj
        self.index = 0

    def __next__(self):
        try:
            item = self.rangeobj[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return item

    def __iter__(self):
        return self


class Range(Sequence):

    def __init__(self, *args):
        self.args = args
        if len(args) == 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        elif len(args) == 2:
            start = args[0]
            stop = args[1]
            step = 1
        elif len(args) == 1:
            start = 0
            stop = args[0]
            step = 1
        elif len(args) > 3:
            raise TypeError('range expected at most 3 arguments, got '
                            + str(len(args)))
        else:
            raise TypeError('range expected 1 arguments, got 0')

        if isinstance(start, float): 
            raise \
                TypeError("'float' object cannot be interpreted as an integer")

        if isinstance(start, str):
            raise TypeError("'str' object cannot be interpreted as an integer")

        if isinstance(stop, float):
            raise \
                TypeError("'float' object cannot be interpreted as an integer")

        if isinstance(stop, str):
            raise TypeError("'str' object cannot be interpreted as an integer")

        if isinstance(step, float):
            raise \
                TypeError("'float' object cannot be interpreted as an integer")

        if isinstance(step, str):
            raise TypeError("'str' object cannot be interpreted as an integer")

        if step == 0:
            raise ValueError('range() arg 3 must not be zero')

        self.start = start
        self.stop = stop
        self.step = step
        self.arr = [i for i in range(start, stop, step)]

    def __eq__(self, other):
        return self.arr == other

    def __iter__(self):
        return RangeIterator(self)

    def __repr__(self):
        return str(range(self.start, self.stop, self.step))

    def __getitem__(self, key):
        if key > len(self.arr):
            raise IndexError('range object index out of range')
        return self.arr[key]

    def __len__(self):
        return len(self.arr)

    def __contains__(self, value):
        return value in self.arr


if __name__ == "__main__":
    import doctest
    doctest.testmod()
