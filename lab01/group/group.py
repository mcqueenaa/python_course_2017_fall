#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, date


class Person:

    """
    >>> p = Person('Ivan', 'Ivanov', 'male', date(1989, 4, 26))
    >>> print(p)
    Ivan Ivanov, male, 29 years
    >>> p.full_ages()
    29
    >>> Person('Ivan', 'Ivanov', 'man', "1989.4.26")
    Traceback (most recent call last):
        ...
    ValueError: bday must be date type
    """

    def __init__(
            self,
            name,
            surname,
            sex,
            bday,
            ):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.bday = bday
        if not isinstance(bday, date):
            raise ValueError('bday must be date type')
        today = datetime.today()
        l_bday = str(self.bday).split('-')
        l_today = str(today).split('-')
        self.age = int(l_today[0]) - int(l_bday[0])

    def __str__(self):
        output = self.name + ' ' + self.surname + ', ' + self.sex \
            + ', ' + str(self.age) + ' years'

        return output

    def full_ages(self):
        today = datetime.today()
        l_bday = str(self.bday).split('-')
        l_today = str(today).replace('-', ' ').split()
        if int(l_today[1]) == int(l_bday[1]):
            if int(l_today[2]) >= int(l_bday[2]):
                full_age = int(l_today[0]) - int(l_bday[0])
            else:
                full_age = int(l_today[0]) - (int(l_bday[0]) + 1)
        elif int(l_today[1]) > int(l_bday[1]):
            full_age = int(l_today[0]) - int(l_bday[0])
        else:
            full_age = int(l_today[0]) - (int(l_bday[0]) + 1)

        return full_age


class Student(Person):

    """
    >>> s = Student('Ivan', 'Ivanov', 'male', date(1989, 4, 26), 161, 9)
    >>> print(s)
    Ivan Ivanov, male, 29 years, 161 group, 9 skill
    """

    def __init__(
            self,
            name,
            surname,
            sex,
            bday,
            group,
            skill,
            ):
        super().__init__(name, surname, sex, bday)
        self.group = group
        self.skill = skill

    def __str__(self):
        output = self.name + ' ' + self.surname + ', ' + self.sex \
            + ', ' + str(self.age) + ' years, ' + str(self.group) \
            + ' group, ' + str(self.skill) + ' skill'

        return output


class Group:

    """
    Encapsulates list of students
    """

    def __init__(self, group):
        self.group = group

    def sort_by_age(self, reverse=False):
        raise NotImplementedError

    def sort_by_skill(self, reverse=False):
        raise NotImplementedError

    def sort_by_age_and_skill(self, reverse=False):
        raise NotImplementedError


if __name__ == '__main__':
    import doctest
    doctest.testmod()
