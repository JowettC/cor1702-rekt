# lab1_main.py
# Do not submit this file

# You may modify this file for testing purposes, 
# but your final lab1a/b/c/d.py must be able to run with the original lab1a_main.py.

from lab1a import *
from lab1b import *
from lab1c import *
from lab1d import *

# run the 6 test cases for gcd_a
print("True --> test case passed. False --> test case failed\n")
print("Running test cases for Q1(a) - Brute force:")
print("Test case 1 passed :", gcd_a(5352, 6690) == 1338)        # test case 1. 1338
print("Test case 2 passed :", gcd_a(7800111, 393945) == 78789)  # test case 2. 78789
print("Test case 3 passed :", gcd_a(75116, 6752) == 844)        # test case 3. 844
print("Test case 4 passed :", gcd_a(7999992, 1999998) == 1999998)# test case 4. 1999998
print("Test case 5 passed :", gcd_a(2, 6) == 2)                 # test case 5. 2
print("Test case 6 passed :", gcd_a(1000, 1) == 1)              # test case 6. 1
print()

# run the 6 test cases for gcd_b
print("Running test cases for Q1(b) - Dijkstra's algo:")
print("Test case 1 passed :", gcd_b(5352, 6690) == 1338)        # test case 1. 1338
print("Test case 2 passed :", gcd_b(7800111, 393945) == 78789)  # test case 2. 78789
print("Test case 3 passed :", gcd_b(75116, 6752) == 844)        # test case 3. 844
print("Test case 4 passed :", gcd_b(7999992, 1999998) == 1999998)# test case 4. 1999998
print("Test case 5 passed :", gcd_b(2, 6) == 2)                 # test case 5. 2
print("Test case 6 passed :", gcd_b(1000, 1) == 1)              # test case 6. 1
print()

# run the 6 test cases for gcd_c
print("Running test cases for Q1(c) - Euclid's algo:")
print("Test case 1 passed :", gcd_c(5352, 6690) == 1338)        # test case 1. 1338
print("Test case 2 passed :", gcd_c(7800111, 393945) == 78789)  # test case 2. 78789
print("Test case 3 passed :", gcd_c(75116, 6752) == 844)        # test case 3. 844
print("Test case 4 passed :", gcd_c(7999992, 1999998) == 1999998)# test case 4. 1999998
print("Test case 5 passed :", gcd_c(2, 6) == 2)                 # test case 5. 2
print("Test case 6 passed :", gcd_c(1000, 1) == 1)              # test case 6. 1
print()

# run the 6 test cases for gcd_d
print("Running test cases for Q1(d) - Binary/Stein's algo:")
print("Test case 1 passed :", gcd_d(5352, 6690) == 1338)        # test case 1. 1338
print("Test case 2 passed :", gcd_d(7800111, 393945) == 78789)  # test case 2. 78789
print("Test case 3 passed :", gcd_d(75116, 6752) == 844)        # test case 3. 844
print("Test case 4 passed :", gcd_d(7999992, 1999998) == 1999998)# test case 4. 1999998
print("Test case 5 passed :", gcd_d(2, 6) == 2)                 # test case 5. 2
print("Test case 6 passed :", gcd_d(1000, 1) == 1)              # test case 6. 1
print()

