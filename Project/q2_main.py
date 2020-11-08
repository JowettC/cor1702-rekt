# q2_main.py v1.0
# do not submit this file. You may modify this file, but your final solution in q2.py should run with this original main file
# use this to check that your q2.py works before submitting to red.
# edit line 11 to use a different CSV file as input. The n and W values are extracted from the name of the CSV file (e.g. m_packages_2_75.csv --> n = 2 and W = 75)

from utility import *
from q2 import *
import time, os
from itertools import chain

packages_csv = "./data/m_packages_2_129.csv" ## <-- change!!!

fn = os.path.basename(packages_csv)
_, _, _n, _W =  fn[:-len('.csv')].split('_')
n = int(_n)    # <-- n = the number after the 2nd underscore in the CSV filename (e.g. m_packages_2_75.csv --> n = 2)
W = int(_W)    # <-- W = the number after the 3rd underscore in the CSV filename (e.g. m_packages_2_75.csv --> W = 75)


packages = package_reader(packages_csv)
packages_dict = {pkg[0]: pkg for pkg in packages}

# call your function
start_time = time.time()    
your_packageSet = select_packageSets(n, W, packages)  # CALL YOUR FUNCTION
time_taken = time.time() - start_time
print("Execution time " + str(time_taken) + " seconds.")    # display time lapsed


# print results or error msg (if any)
# mS = min sum of rewards (the lowest reward amongst all members)
# wSM = members' sum of weights (1D list). Each element in wSM should not exceed W
err_msg, mS, wSm = get_mS_and_wSm_q2(your_packageSet, packages_dict, W)

if err_msg != None:
    print("Error : " + err_msg)
else:  
    for i in range(n): # check that each member's weight is <= W
        wS = wSm[i]
        print("The sum of weights for member %d's package selection : %d, W: %d" % (i, wS, W))
        if wS > W:
            print("Error : the sum of weights is more than W!")
    else:
        print("Quality score (the minimum among members’ sum of rewards) for q2 is : %d" % mS) # higher score is better

