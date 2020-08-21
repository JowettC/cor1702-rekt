# Name: Nicholas Chen Han Wei
# Section: G7

# lab1a (Brute force)

# All statements should only be in functions.
def gcd_a(x, y):
    # Let's loop from 1 to x's size + 1 instead
    i = min(x, y)
    while (x % i or y % i) != 0:  # while modulo x and i or y and i ain't 0, keep iterating
        i -= 1
    # Bad result.
    return i