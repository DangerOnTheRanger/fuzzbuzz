#!/usr/bin/env python3
from itertools import cycle, islice


def main(n):
    for x in islice(cycle(('Buzz', 'Fuzz', 'FuzzBuzz',
                           'Fuzz', 'Buzz', 'FuzzBuzz')), n):
        print(x)


if __name__ == '__main__':
    main(100)
