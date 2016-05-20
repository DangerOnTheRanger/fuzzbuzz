def is_multiple_of(number, mul):
    """Return True if number is multiple of mul, false otherwise.
    So again we're exploiting the properties of integer division.
    For any divisor, there are at least two consecutive dividends that will return
    the exact same quotient under integer divison, and the smaller number in each
    is a multiple of the divisor. All we have to do is check that number
    is the smaller of the pair. We do that by seeing if the result changes
    if we subtract 1. If so, number is the smaller of the pair (i.e, number - 1
    is part of some other pair), so return True.
    Otherwise, we were given the larger of the pair, or alternatively,
    some completely different number, so return False.
    """
    if number / mul > (number - 1) / mul:
        return True
    else:
        return False


def multiple_of_three(number):
    return is_multiple_of(number, 3)


def multiple_of_two(number):
    return is_multiple_of(number, 2)
    
    
for x in xrange(1, 101):
    if multiple_of_three(x):
        print "FuzzBuzz"
    elif multiple_of_two(x):
        print "Fuzz"
    else:
        print "Buzz"

