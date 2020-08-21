# lab0a_main.py
# Do not submit this file

# You may modify this file for testing purposes, 
# but your final lab0a.py must be able to run with the original lab0a_main.py.

from lab0a import admit

# run the 4 test cases for admit
print("True --> test case passed. False --> test case failed\n")
print("Running test cases for Q0(a):")
print("Test case 1 passed :", admit("M",22) == False) # test case 1
print("Test case 2 passed :", admit("M",23) == True)  # test case 2
print("Test case 3 passed :", admit("F",17) == False) # test case 3
print("Test case 4 passed :", admit("F",18) == True)  # test case 4
print()
print("Ensure that all 4 test cases are correct before submitting your solution to the Submission Server")
