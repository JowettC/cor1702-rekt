# q1_main.py v1.0
# do not submit this file. You may modify this file, but your final solution in q1.py should run with this original main file
# use this to check that your q1.py works before submitting to red.
# edit line 11 to use a different CSV file as input. The W value is extracted from the name of the CSV file (e.g. s_packages_165.csv --> W = 165)

from utility import *
from q1 import *
import os, csv, copy, time


packages_csv = "./data/s_packages_26.csv" # <-- change!!!
fn = os.path.basename(packages_csv)
W = int(fn[:-len('.csv')].split('_')[2])  # <-- W = the number after the 2nd underscore in the CSV filename (e.g. for s_packages_165.csv, W = 165)

packages = package_reader(packages_csv)
packages_dict = {pkg[0]: pkg for pkg in packages}


# call your function
start_time = time.time()    
your_packageSet = select_packageSet(W, packages)   # CALL YOUR FUNCTION
time_taken = time.time() - start_time
print("Execution time " + str(time_taken) + " seconds.")    # display time lapsed


# print results or error msg (if any)
err_msg, rS, wS = get_rS_and_wS_q1(your_packageSet, packages_dict, W)

if err_msg !=None:
    print("Error : " + err_msg)
else:  
    print("The sum of weights for this package selection : %d, maximum W: %d" % (wS, W))
  
    if wS > W:
        print("Error : the sum of weights is more than W!")
    else:
        print("Quality score (the sum of rewards) for q1 is : %d" % rS) # higher score is better
