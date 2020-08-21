# Name: Nicholas Chen Han Wei
# Section: G7

# lab1c (Euclid's algo)

# All statements should only be in functions.
def gcd_c(x, y):
    # Adapted from lab1a, I apparently wrote this instead of brute force in 1a
    # if y = 0, we got the answer. if y is not 0, we get the remainder of x / y to get the next remainder
    # we use the remainder to check if x can be equally divided. Since when x % y = 0, we can recurse this
    # equation to obtain the result.
    return x if y == 0 else gcd_c(y, x % y)
