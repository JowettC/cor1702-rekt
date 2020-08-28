# Name: Nicholas Chen Han Wei
# Section: G7

# lab2b
# import numpy as np
from collections import defaultdict

# All statements should only be in functions. Do not include statements outside functions in this file.

# INSTRUCTIONS: 
# Refer to the code in lab2b_main.py - perform_once will be called one time before 
# exist is called many times. You may modify perform_once if desired, or keep it as it is.
def perform_once(employee_with_birthyear_list):
  birthyear_employees = defaultdict(list)
  # Write any code here if desired. Any code you do here will replace the original employee_list
  # while len(employee_with_birthyear_list) > 0:
  #   # If the birthyear key already exists in the dictionary
  #   if employee_with_birthyear_list[0][1] in birthyear_employees:
  #         birthyear_employees[employee_with_birthyear_list[0][1]].append(employee_with_birthyear_list[0][0])
  #   else:
  #     # Else we don't have a year, create it
  #     birthyear_employees[employee_with_birthyear_list[0][1]] = []
  #     birthyear_employees[employee_with_birthyear_list[0][1]].append(employee_with_birthyear_list[0][0])
  #
  #   # Pop
  #   del employee_with_birthyear_list[0]
  for k in employee_with_birthyear_list:
    # print(k[1], "for employee", k[0])
    birthyear_employees[k[1]].append(k[0])

  return birthyear_employees

  
# INSTRUCTIONS: 
# Write a function called get_IDs_with_birthyear that takes in a year (as an integer) and an array (employee_with_birthyear_list)
# It then returns an array of employee IDs (integers) that have matching birthyears.
# If there is no match, this function returns an empty array (i.e. []).
def get_IDs_with_birthyear(year, employee_with_birthyear_list):
  # print(employee_with_birthyear_list[year])
  # for now, this function always returns an empty list
  # return np.where(employee_with_birthyear_list[1] == year)
  return employee_with_birthyear_list[year] if year in employee_with_birthyear_list else []