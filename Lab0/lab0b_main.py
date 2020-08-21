# lab0b_main.py
# Do not submit this file

# You may modify this file for testing purposes, 
# but your final lab0b.py must be able to run with the original lab0b_main.py.

from lab0b import weight_category

# run the 5 test cases for weight_category
print("True --> test case passed. False --> test case failed\n")
print("Running test cases for Q0(b):")
print("Test case 1 passed :", weight_category(71, 168) == "overweight")     # test case 1
print("Test case 2 passed :", weight_category(103, 200) == "overweight")    # test case 2
print("Test case 3 passed :", weight_category(25, 100) == "normal")         # test case 3
print("Test case 4 passed :", weight_category(65.3, 171) == "normal")       # test case 4
print("Test case 5 passed :", weight_category(63, 185.1) == "underweight")  # test case 5
print()
print("Ensure that all 4 test cases are correct before submitting your solution to the Submission Server")
