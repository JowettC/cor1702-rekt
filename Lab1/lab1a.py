# Name: Nicholas Chen Han Wei
# Section: G7

# lab1a (Brute force)

# All statements should only be in functions.
def gcd_a(x, y):
    t = x if x < y else y
    while t != 1:
        if x % t == 0 and y % t == 0: return t
        else: t -= 1
    return t