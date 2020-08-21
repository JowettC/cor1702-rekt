# Name: Nicholas Chen Han Wei
# Section: G7

# lab1a (Brute force)

# All statements should only be in functions.
def gcd_a(x, y):
    if y == 0: return x # if y = 0, we got the answer.
    # if y is not 0, we get the remainder of x / y to get the next remainder
    # we use the remainder to check if x can be equally divided. Since when x % y = 0, we can recurse this
    # equation to obtain the result.
    return gcd_a(y, x % y)