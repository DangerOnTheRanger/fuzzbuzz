#!/usr/bin/env python3
def main(x):
    from itertools import cycle, repeat
    for x,y in zip(repeat(x, x),cycle(("Buzz", "Fuzz", "FuzzBuzz", "Fuzz", "Buzz", "FuzzBuzz"))):print(y)
main(100)
