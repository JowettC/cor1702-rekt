# Name: Nicholas Chen Han Wei
# Section: G7

# lab1d (Binary/Stein's algo)

# All statements should only be in functions.
def gcd_d(x, y):
    k = 0

    while x % 2 == 0 and y % 2 == 0:  # while x and y are both even
        x /= 2
        y /= 2
        k += 1

    while x != y:
        if x % 2 == 0:
            x /= 2  # if x is even then x /= 2
        elif y % 2 == 0:
            y /= 2  # if y is even then y /= 2
        elif x > y:
            x = (x - y) / 2 # if x > y then x = (x - y) / 2
        else:
            y = (y - x) / 2 # else y = (y - x) / 2

    return x * 2 ** k
