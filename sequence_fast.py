from collections import deque
sequence = deque(["Buzz", "Fuzz", "FuzzBuzz", "Fuzz", "Buzz", "FuzzBuzz"])


# Binding oft-used functions to local scope results in a speed increase
# due to decreased variable lookup time
popleft = sequence.popleft
append = sequence.append


for x in xrange(1, 101):
    # Moving the function's code to the loop body removes the function call,
    # which actually increases performance slightly
    next_string = popleft()
    append(next_string)
    print next_string
