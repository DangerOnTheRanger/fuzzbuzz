def is_multiple_of(number, mul):
    """Return True if number is multiple of mul, false otherwise.
    Okay, so here's how this works: Normally, Python - and most
    other programming languages - chops off the decimal part of the quotient
    if both terms are integers, i.e, integer division is performed. However,
    if one of the terms is a float, then the decimal part will be kept.
    Any number plus a decimal part is going to be greater than simply the number itself,
    so we compare the two. If number is in fact a multple of mul, then there will be
    no decimal part, and both sides of the expression will be equal."""
    if float(number) / mul == number / mul:
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

