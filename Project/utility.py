# utility.py v1.0

import csv
from itertools import chain
import time, os

# reads a CSV file and returns every line as a list
def package_reader(packages_csv):
    packages = []
    
    with open(packages_csv) as r_csvfile:
        reader = csv.DictReader(r_csvfile)
        for row in reader:
            pkg = [row['ID']]
            pkg += [eval(row[cn]) for cn in ['reward', 'weight']]
            packages.append(pkg)
    return packages

# for Q1
# checks if your answer (packageSet) has syntax errors
def get_syntax_error_msg_q1(your_packageSet):
    if type(your_packageSet) != list:
        return "Your answer is not a list. Your route must be a list of package IDs"

    if not all(type(elem)==str for elem in your_packageSet):
        return "Your answer must be a list of strings (packageIDs) only."

    # check if there are duplicate flagIDs in your_route
    if len(your_packageSet) != len(set(your_packageSet)):
        return "There are duplicate package IDs in your package selection. packageIDs in your package selection must be unique."

    return None # all ok

# for Q1
# used for computing quality score for Q1
# will return error message (string) if there is an error
# returns error_msg (or None if all ok), score (the sum of rewards), the sum of weights (for comparison with W)
def get_rS_and_wS_q1(your_packageSet, packages_dict, W):
    # check for syntax error first
    err_msg = get_syntax_error_msg_q1(your_packageSet)
    if err_msg != None:
        return err_msg, 0, 0
    # calculate the sum of rewards and weights
    rS, wS = 0, 0
    for pid in your_packageSet:
        if not pid in packages_dict:
            return "Package ID in your package selection is not valid : " + pid, 0, 0 # error
        rS += packages_dict[pid][1]
        wS += packages_dict[pid][2]
    return None, rS, wS # no error

# for Q2
# checks if your answer (packageSet) has syntax errors
def get_syntax_error_msg_q2(your_packageSet):
    if type(your_packageSet) != list:
        return "Your answer is not a list. Your route must be a list of package IDs"

    selPackages = list(chain(*your_packageSet))
    if not all(type(elem)==str for elem in selPackages):
        return "Your answer must be a list of strings (packageIDs) only."

    # check if there are duplicate flagIDs in your_route
    if len(selPackages) != len(set(selPackages)):
        return "There are duplicate package IDs in your package selection. packageIDs in your package selection must be unique."

    return None # all ok

# for Q2
# used for computing quality score for Q2
# will return error message (string) if there is an error
# returns error_msg (or None if all ok), score (the minimum among members’ sum of rewards), members' sum of weights  (for comparison with W)
def get_mS_and_wSm_q2(your_packageSet, packages_dict, W):
    # check for syntax error first
    err_msg = get_syntax_error_msg_q2(your_packageSet)
    if err_msg != None:
        return err_msg, 0, 0
        
    # calculate
    #   mS: the minimum among members’ sum of rewards
    #   wSm: members' sum of weights
    mS, wSm = 1e400, []
    for m_pkg in your_packageSet:  # edited
        rS, wS = 0, 0
        for pid in m_pkg:
            if not pid in packages_dict:
                return "Package ID in your package selection is not valid : " + pid, 0, 0 # error
            rS += packages_dict[pid][1]
            wS += packages_dict[pid][2]
        if rS < mS:
            mS = rS
        wSm.append(wS)   
    return None, mS, wSm # no error

