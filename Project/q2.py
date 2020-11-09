# G7-T22
# BENJAMIN CHEW PIN HSIEN, NICHOLAS CHEN HAN WEI

# Q2

# Replace the content of this function with your own algorithm
# inputs: 
#   n: the number of members in your team
#   W: weight limit of each vehicle used for deliveries.
#   packages: 2D list [[packageID, reward, weight], [packageID, reward, weight], ...]
# returns:
#   2D list of package IDs to represent n sets of packages. 
#   e.g. if n = 2, this is a possible solution: [["P001", "P003"], ["P010"]]
import copy
import math
import random
from itertools import chain

def select_packageSets(n, W, packages, variations=80):
    backup_packages = copy.deepcopy(packages)
    packages_dict = {pkg[0]: pkg for pkg in backup_packages}
    # Split into chunks, sort them via profitability.
    # Profitability = reward/weight
    # Best to worst
    backup_packages.sort(key=lambda x: (x[1]/x[2]), reverse=True)

    # Take the best packages till we hit the total weight limit
    weight_total = 0
    max_index = 0
    for i in range(len(backup_packages)):
        max_index = i
        if weight_total > (W * n):
            break
        weight_total += backup_packages[i][2]

    p_set_results = []
    best_score = 0
    # Method 1: Non-leaky variation
    # When we're in a scenario where we can never fill the members entirely
    if max_index == len(backup_packages) - 1:
        generated_shuffles = gen_unique_shuffles(backup_packages[:max_index], variations)
        for generated_shuffle in generated_shuffles:
            set_thresholds = [0] * n
            p_sets = []
            while len(p_sets) < n:
                p_sets.append([])
            for package in generated_shuffle:
                c_index = get_avail_member(set_thresholds, W, package[2])
                pushed = False

                if c_index < 0:
                    break

                while not pushed:
                    if set_thresholds[c_index] + package[2] <= W:
                        set_thresholds[c_index] += package[2]
                        p_sets[c_index].append(package[0])
                        pushed = True

            err_msg, mS, wSm = get_mS_and_wSm_q2(p_sets, packages_dict, W)
            if best_score < mS:
                best_score = mS
                p_set_results = copy.deepcopy(p_sets)

        return p_set_results
    # Method 2: Leaky variation
    else:
        unique_sets = []
        for i in range(variations):
            unused_packages = backup_packages[max_index + 1:]
            packages = backup_packages[:max_index]

            # We can multi-init like that
            # https://stackoverflow.com/questions/6142689/initialising-an-array-of-fixed-size-in-python
            set_threshold = [0] * n
            package_sets = []
            while len(package_sets) < n:
                package_sets.append([])

            # BEGIN FULL BIN PACKING ALGORITHM
            gen_unique_shuffle(packages, unique_sets)
            package_index = 0

            while len(packages) > package_index:
                # Obtain the biggest package
                package = packages[package_index]

                # Find the first bin that can accommodate
                first_avail = get_avail_member(set_threshold, W, package[2])

                # Always check to ensure we don't exceed the threshold
                if (set_threshold[first_avail] + package[2] <= W) and not exists(package, package_sets):
                    package_sets[first_avail].append(package[0])
                    set_threshold[first_avail] += package[2]
                elif not exists(package, package_sets):
                    unused_packages.insert(0, package)

                package_index += 1

            # Check out the last threshold, the last one should be incomplete.
            # for i in range(len(set_threshold)):
            # Since the threshold is not maxed, lets see if we can max it out.
            if set_threshold[n - 1] < W:
                # Clear up all the packages and add it as unused.
                for index in range(len(package_sets[n - 1]) - 1, -1, -1):
                    # Obtain the current package's id first
                    package_id = package_sets[n - 1][index]
                    # Search the package database to repopulate the package data into unused_packages again.
                    for back_pack in backup_packages:
                        if back_pack[0] == package_id:
                            unused_packages.insert(0, back_pack)
                            break
                package_sets[len(set_threshold) - 1].clear()
                set_threshold[len(set_threshold) - 1] = 0

            tracked_packages = []
            remaining_packages = []
            for i in range(len(unused_packages) - 1):
                unused_package = unused_packages[i]
                if unused_package[0] not in tracked_packages and not exists(unused_package, package_sets):
                    tracked_packages.append(unused_package[0])
                    remaining_packages.append(unused_package)

            package_sets[len(package_sets) - 1] = select_packageSet(W, remaining_packages)

            err_msg, mS, wSm = get_mS_and_wSm_q2(package_sets, packages_dict, W)
            if best_score < mS:
                best_score = mS
                p_set_results = copy.deepcopy(package_sets)

        # Check
        # tracked_packages = []
        # for p_set in package_sets:
        #     for package in p_set:
        #         if package in tracked_packages:
        #             print('Duplicate package detected: ' + package)
        #         else:
        #             tracked_packages.append(package)

        return p_set_results


# Check for dupes
def exists(package, package_sets):
    for package_set in package_sets:
        for pack in package_set:
            if pack == package[0]:
                return True
    return False


def gen_unique_shuffle(packages, shuffles):
    while True:
        random.shuffle(packages)

        found = False
        for shuffle in shuffles:
            found = packages == shuffle

        if not found:
            shuffles.append(packages)
            return packages


def gen_unique_shuffles(packages, shuffles=50):
    if math.factorial(len(packages)) < shuffles:
        shuffles = math.factorial(len(packages))

    results = [copy.deepcopy(packages)]
    while shuffles > 0:
        found = False
        random.shuffle(packages)

        for results_item in results:
            if results_item == packages:
                found = True
                break

        if not found:
            results.append(copy.deepcopy(packages))
            shuffles -= 1
    return results


# you may insert other functions here, but all statements must be within functions before submitting to red,
# check that there are no print statements in your code. Nothing should be printed when your code runs.
def get_smallest_index(thresholds):
    index = 0
    for i in range(len(thresholds)):
        if thresholds[i] < thresholds[index]:
            index = i
    return index


def all_have_exceeded(thresholds, val, lim):
    for threshold in thresholds:
        if threshold + val < lim:
            return False
    return True


def get_package_dict(packages):
    res = {}
    for package in packages:
        res[package[0]] = package[1:]

    return res


def get_avail_member(thresholds, limit, incoming):
    for i in range(len(thresholds)):
        if thresholds[i] + incoming <= limit:
            return i

    return -1


# Adapted from q1.
def select_packageSet(W, packages):
    val = []
    wt = []
    package = []
    package_select = []

    for i in range(len(packages)):
        val.append(packages[i][1])
        wt.append(packages[i][2])
        package.append(packages[i][0])

    n = len(val)

    selected_wt_index = knapSack(W, wt, val, n)

    for wt_index in selected_wt_index:
        package_select.append(package[wt_index])

    return (package_select)


def knapSack(W, wt, val, n):
    selected_weight = []

    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
                # print(K)

    # return K[n][W]
    while K[n][W] != 0:
        if K[n][W] != K[n - 1][W]:
            selected_weight.append(n - 1)
            W -= wt[n - 1]
        n -= 1

    return selected_weight


# for Q2
# checks if your answer (packageSet) has syntax errors
def get_syntax_error_msg_q2(your_packageSet):
    if type(your_packageSet) != list:
        return "Your answer is not a list. Your route must be a list of package IDs"

    selPackages = list(chain(*your_packageSet))
    if not all(type(elem) == str for elem in selPackages):
        return "Your answer must be a list of strings (packageIDs) only."

    # check if there are duplicate flagIDs in your_route
    if len(selPackages) != len(set(selPackages)):
        return "There are duplicate package IDs in your package selection. packageIDs in your package selection must be unique."

    return None  # all ok


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
                return "Package ID in your package selection is not valid : " + pid, 0, 0  # error
            rS += packages_dict[pid][1]
            wS += packages_dict[pid][2]
        if rS < mS:
            mS = rS
        wSm.append(wS)
    return None, mS, wSm  # no error
