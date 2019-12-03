#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from typing import List
from numbers import Number


def regexp_0(text: str, pattern: str) -> List[slice]:
    """
    Finds the occurrence and position of the substrings within a string
    >>> regexp_0("LingvoX SpaceX SpacoX", "oX")
    [slice(5, 7, None), slice(19, 21, None)]
    """

    slices = []
    for_end = len(pattern)
    pattern = '(?=(' + pattern + '))'
    for f in re.finditer(pattern, text):
        start = f.start()
        end = f.start() + for_end
        slices.append(slice(start, end, None))
        
    return slices


def regexp_1(text: str) -> str:
    """
    Converts camel case string to snake case string
    >>> regexp_1("QObject")
    'q_object'
    >>> regexp_1("KNeighborsClassifier")
    'k_neighbors_classifier'
    """

    camel = text
    snake = ''
    for i in re.findall(r'([A-ZА-Я][a-zа-я]*)', camel):
        snake = snake + i.lower() + '_'
    if snake.endswith('_'):
        snake = snake[:len(snake) - 1]
        
    return snake


def regexp_2(text: str, length: int) -> str:
    """
    Removes words from a string of length between 1 and a given number
    >>> regexp_2("Hello Cyril Kak dela bro", 3)
    'Hello Cyril dela'
    >>> regexp_2("Hello Cyril Kak dela bro", 4)
    'Hello Cyril'
    """
    
    reg_word = re.compile(r'\w+')       
    for i in re.findall(reg_word, text):
        if len(i) <= length:
            text = re.sub(i, '', text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = text.lstrip()
    text = text.rstrip()    
    return text


def regexp_3(text: str) -> str:
    """
    Removes the parenthesis area in a string
    >>> regexp_3("Polina (Ivan)")
    'Polina'
    >>> regexp_3("Mark (Station) (LingvoX)")
    'Mark'
    """

    p_area = re.compile(r'\s?\(.*?\)')
    if re.search(p_area, text):
        text = re.sub(p_area, '', text)
    if re.search(r'\)', text):
        text = re.sub(r'\)', '', text)
    text = text.lstrip()
        
    return text


def regexp_4(num: Number) -> bool:
    """
    Returns true whenever a decimal with a precision of 2
    >>> regexp_4(1.22)
    True
    >>> regexp_4(1.2)
    True
    >>> regexp_4(11)
    True
    >>> regexp_4(11.)
    True
    >>> regexp_4(11.333)
    False
    """

    reg_true = r'\d+\.?\d{,3}'
    reg_false = r'\d+\.\d{3,}'
    s_num = str(num)
    if re.search(reg_true, s_num):
        if re.search(reg_false, s_num):
            return False
        else:
            return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
