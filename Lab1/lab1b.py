# Name: Nicholas Chen Han Wei
# Section: G7

# lab1b (Dijkstra's algo)
import sys

# All statements should only be in functions.
def gcd_b(x, y):
    # TODO: Optimise, find the best method
    # while x != y: # while both babies are not equal
    #     if x > y: return gcd_b(x - y, y)
    #     elif x < y: return gcd_b(x, y - x)
    # return x
    sys.setrecursionlimit(5000)
    # # For two integers x and y, if x > y then gcd(x, y) = gcd(x - y, y)
    if x > y: return gcd_b(x - y, y)
    elif x < y: return gcd_b(x, y - x)
    else: return x