from collections import deque
import sys
sys.setrecursionlimit(101)
# Python allows the user to manually set the recursion limit.
# So, we exploit this by setting it to 101, which simulates the number of
# loop iterations we'd execute if we were using a loop.
# Eventually, we'll exceed this number, and Python will throw
# a RuntimeError, essentially accomplishing the same thing as
# a regular for/while loop.


sequence = deque(["Buzz", "Fuzz", "FuzzBuzz", "Fuzz", "Buzz", "FuzzBuzz"])


def next_in_sequence():
    """Print next string in FuzzBuzz sequence.
    This is identical to the deque solution in sequence.py, save for
    printing out the next string instead of returning it, and the recursion bit,
    so go see sequence.py for an explanation of what's going on here.
    """
    next = sequence.popleft()
    sequence.append(next)
    print next
    next_in_sequence()


try:
    next_in_sequence()
except RuntimeError:
    # swallow the eventual exception due to recursion taking one step too many
    pass
