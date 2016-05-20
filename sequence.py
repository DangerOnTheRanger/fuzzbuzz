from collections import deque
sequence = deque(["Buzz", "Fuzz", "FuzzBuzz", "Fuzz", "Buzz", "FuzzBuzz"])


def next_in_sequence():
    """Return next string in FuzzBuzz sequence.
    The FuzzBuzz problem follows a pattern:
        * Odd
        * Even
        * Multiple of 3
        * Even
        * Odd
        * Multiple of 3
    All we have to do is keep track of where we are in the sequence.
    To accomplish this, we use a deque and a little bit of pushing and popping
    to keep from having to either pre-generate the entire sequence beforehand,
    or from having to use an iterator.
    """
    next = sequence.popleft()
    sequence.append(next)
    return next


for x in xrange(1, 101):
    print next_in_sequence()
