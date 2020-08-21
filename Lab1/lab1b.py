# Name: Nicholas Chen Han Wei
# Section: G7

# lab1b (Dijkstra's algo)
import sys

# All statements should only be in functions.
def gcd_b(x, y):
    # For two integers x and y, if x > y then gcd(x, y) = gcd(x - y, y)
    if x > y: return gcd_b(x - y, y)
    elif x < y: return gcd_b(x, y - x)
    return x
