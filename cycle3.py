#!/usr/bin/env python3
from itertools import cycle, islice

SEQ = ('Buzz', 'Fuzz', 'FuzzBuzz', 'Fuzz', 'Buzz', 'FuzzBuzz')


def main(n):
    for x in islice(cycle(SEQ), n):
        print(x)


if __name__ == '__main__':
    main(100)
