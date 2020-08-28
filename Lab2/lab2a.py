# Name: Nicholas Chen Han Wei
# Section: G7

# lab2a

# All statements should only be in functions. Do not include statements outside functions in this file.

# INSTRUCTIONS: 
# Refer to the code in lab2a_main.py (line 41) - perform_once() will be called one time before 
# exist() is called many times. You may modify this function if desired, or leave it as it is.
def perform_once(employee_list):
  # This function takes in employee_list and returns the same employee_list for now.
  return set(employee_list)

# INSTRUCTIONS: 
# This method is a fully functioning method that uses sequential search to search for the id in employee_list.
# This method returns True (if this ID exists), or False otherwise.
# Modify this method so that it uses a superior algorithm that performs significantly faster.
def exist(id, employee_list):
    return True if (id in employee_list) else False