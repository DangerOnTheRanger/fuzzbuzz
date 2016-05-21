#!/usr/bin/env python3
def main(x):
    from itertools import cycle, islice
    for x in islice(cycle(("Buzz", "Fuzz", "FuzzBuzz", "Fuzz", "Buzz", "FuzzBuzz")), x):print(x)
main(100)
