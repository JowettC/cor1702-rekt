# Name: Nicholas Chen Han Wei
# Section: G7

# lab3a

# All statements should only be in functions. Do not include statements outside functions in this file.


# Takes in an integer and returns the sum of all its digits as an integer
# this function does NOT have to handle negative numbers (i.e. i will always be >=0)
# this function must be recursive (i.e. it will call itself)
# Refer to hints in the requirements doc.
def sum_of_digits(i):
  return i if i == 0 else i % 10 + sum_of_digits(i // 10)
