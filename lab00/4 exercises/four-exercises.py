# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def divisible(begin, end):
    """
    :param begin: int, positive integer
    :param end: int, positive integer
    :return: str, string of space separated integers
    Examples of usage:
    >>> divisible(1, 10)
    '7'
    >>> divisible(1, 17)
    '7 14'
    >>> len(divisible(100, 1000))
    407
    >>> divisible(29, 60)
    '42 49 56'
    >>> len(divisible(300, 3000).split())
    309
    >>> ns = [int(n) for n in divisible(300, 10000).split()]
    >>> seven_mask = [not bool(n % 7) for n in ns]
    >>> all(seven_mask)
    True
    >>> any(seven_mask)
    True
    >>> five_mask = [not bool(n % 5) for n in ns]
    >>> all(five_mask)
    False
    >>> any(five_mask)
    False
    >>> divisible(2, 5)
    ''
    >>> 1329 not in ns
    True
    """

    res = ''
    for i in range(begin, end + 1):
        if (i % 7 == 0) and (i % 5 != 0):
            res = res + str(i) + ' '
    res = res[0:len(res) - 1]

    return res


def register_count(string):
    """
    :param string: str, input string
    :return: dict, dict of lower and upper letter counts
    >>> register_count("Mama") == {'UPPER': 1, 'LOWER': 3}
    True
    >>> register_count("Your Name") == {'UPPER': 2, 'LOWER': 6}
    True
    >>> register_count("LingvoX!!!") == {'UPPER': 2, 'LOWER': 5}
    True
    >>> register_count("Trud, mir, mai! Zvahka!") == {'UPPER': 2, 'LOWER': 14}
    True
    >>> register_count("Coi ZIV!,,,,,") == {'UPPER': 4, 'LOWER': 2}
    True
    """

    d = {'UPPER': 0, 'LOWER': 0}
    letters = list(string)
    for i in letters:
        if i.islower():
            d['LOWER'] = d['LOWER'] + 1
        elif i.isupper():
            d['UPPER'] = d['UPPER'] + 1

    return d


def pairwise_diff(first, second):
    """
    :param first: str, first input string
    :param second: str, second input string
    :return: float, percentage of different letters
    >>> pairwise_diff('ABSD', 'ABCD')
    0.25
    >>> pairwise_diff('aBSD', 'ABCD')
    0.5
    >>> pairwise_diff('LingvX', 'SpaceX')
    0.83
    >>> pairwise_diff('LingvoX', 'SpaceX')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> pairwise_diff('abc', 'ab')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> first = 'Salaman..'; second = 'Salaman.!'
    >>> round(1. / len(first), 2) == pairwise_diff(first, second)
    True
    >>> pairwise_diff(first + second, first + first)
    0.06
    >>> pairwise_diff(first * 3, second * 2 + first)
    0.07
    """

    k = 0
    assert len(first) == len(second)
    first_list = list(first)
    second_list = list(second)
    for (i, j) in zip(first_list, second_list):
        if i != j:
            k += 1
    out = round(k / len(first), 2)

    return out


def run_robot():
    """
    Uses input() inside.
    :return: int, rounded euclidean distance from origin
    """

    import math
    import re

    height = 0
    width = 0
    move = ' '
    re_move = r'(UP|DOWN|RIGHT|LEFT) (\d+)'
    moves = []
    while move != '':
        move = \
            input('Напишите, в каком направлении \
    и сколько шагов должен сделать робот в формате \
    "UP x; DOWN z; RIGHT y; LEFT h", где x, z, y, h - целые числа: '
                  )
        moves.append(move)
    for m in moves:
        if re.search(re_move, m):
            if re.search(re_move, m).group(1) == 'UP':
                height = height + int(re.search(re_move, m).group(2))
            elif re.search(re_move, m).group(1) == 'DOWN':
                height = height - int(re.search(re_move, m).group(2))
            elif re.search(re_move, m).group(1) == 'RIGHT':
                width = width + int(re.search(re_move, m).group(2))
            elif re.search(re_move, m).group(1) == 'LEFT':
                width = width - int(re.search(re_move, m).group(2))
    s = round(math.sqrt(height ** 2 + width ** 2))

    return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
