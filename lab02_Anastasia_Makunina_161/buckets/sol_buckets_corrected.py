#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import copy


class Buckets:

    def __init__(self, length, default):
        self.default = copy(default)
        self.buckets = [copy(default)] * length

    def __str__(self):
        return str(self.buckets)

    def add(self, index, element):
        self.buckets[index] = copy(self.buckets[index])
        self.buckets[index].append(element)

    def find(self, index, element):
        return element in self.buckets[index]

    def clear(self, index):
        self.buckets[index] = self.default


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    default = [1, 2, [3]]
