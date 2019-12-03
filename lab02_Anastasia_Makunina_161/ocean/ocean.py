#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from copy import deepcopy


class Ocean:

    def __init__(self, init_state):
        self.init_state = init_state

    def __str__(self):
        output = ''
        for i in range(len(self.init_state)):
            j = ' '.join([str(h) for h in self.init_state[i]])
            if i != len(self.init_state) - 1:
                output = output + j + '\n'
            else:
                output = output + j
        return output

    def gen_next_quantum(self):
        next_state = deepcopy(self.init_state)
        for row in range(len(self.init_state)):
            for col in range(len(self.init_state[row])):
                s = 0
                f = 0
                if self.init_state[row][col] != 1:
                    if col - 1 != -1:
                        try:
                            if self.init_state[row][col - 1] == 2:
                                f += 1
                            elif self.init_state[row][col - 1] == 3:
                                s += 1
                        except IndexError:
                            pass

                        try:
                            if self.init_state[row + 1][col - 1] == 2:
                                f += 1
                            elif self.init_state[row + 1][col - 1] == 3:
                                s += 1
                        except IndexError:
                            pass

                    if row - 1 != -1:
                        try:
                            if self.init_state[row - 1][col] == 2:
                                f += 1
                            elif self.init_state[row - 1][col] == 3:
                                s += 1
                        except IndexError:
                            pass

                        try:
                            if self.init_state[row - 1][col + 1] == 2:
                                f += 1
                            elif self.init_state[row - 1][col + 1] == 3:
                                s += 1
                        except IndexError:
                            pass

                    if (col - 1 != -1) and (row - 1 != -1):
                        try:
                            if self.init_state[row - 1][col - 1] == 2:
                                f += 1
                            elif self.init_state[row - 1][col - 1] == 3:
                                s += 1
                        except IndexError:
                            pass

                    try:
                        if self.init_state[row + 1][col] == 2:
                            f += 1
                        elif self.init_state[row + 1][col] == 3:
                            s += 1
                    except IndexError:
                        pass

                    try:
                        if self.init_state[row][col + 1] == 2:
                            f += 1
                        elif self.init_state[row][col + 1] == 3:
                            s += 1
                    except IndexError:
                        pass

                    try:
                        if self.init_state[row + 1][col + 1] == 2:
                            f += 1
                        elif self.init_state[row + 1][col + 1] == 3:
                            s += 1
                    except IndexError:
                        pass

                    if self.init_state[row][col] == 2:
                        if (f >= 4) or (f <= 1):
                            next_state[row][col] = 0

                    elif self.init_state[row][col] == 0:
                        if s == 3:
                            next_state[row][col] = 3
                        if f == 3:
                            next_state[row][col] = 2

                    elif self.init_state[row][col] == 3:
                        if (s >= 4) or (s <= 1):
                            next_state[row][col] = 0

        self.init_state = deepcopy(next_state)
        return Ocean(init_state=self.init_state)


if __name__ == '__main__':
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = [int(i) for i in sys.stdin.readline().split()]
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean)
