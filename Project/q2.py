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
import sys


def select_packageSets(n, W, packages, variations=200):
    readonly_package_dict = {pkg[0]: pkg[1:] for pkg in packages}
    avail_package_dict = {pkg[0]: pkg[1:] for pkg in packages}
    # Split into chunks, sort them via profitability.
    # Profitability = reward/weight
    # Best to worst
    packages.sort(key=lambda x: (x[1] / x[2]), reverse=True)

    # Take the best packages till we hit the total weight limit
    weight_total = 0
    max_index = 0
    for i in range(len(packages)):
        max_index = i
        if weight_total > (W * n):
            break
        weight_total += packages[i][2]

    if max_index == len(packages) - 1:
        packages.sort(key=lambda x: x[1], reverse=True)

    # Setup the bins
    set_thresholds = [0] * n
    set_rewards = [0] * n
    p_sets = []
    while len(p_sets) < n:
        p_sets.append([])

    # Next fit algorithm
    # if max_index < len(packages_dict.keys()):
    for package in packages:
        # Try to fit item into a bin
        i = get_next_fit_index(p_sets, set_thresholds, set_rewards, package[2], W)

        if i > -1:
            # print 'Adding', item, 'to', bin
            p_sets[i].append(package[0])
            set_thresholds[i] += package[2]
            set_rewards[i] += package[1]
            del avail_package_dict[package[0]]

    differential = (n * W) - sum(set_thresholds)

    if differential > 0:
        valid_packages = []
        for package in avail_package_dict:
            if avail_package_dict[package][1] <= differential:
                valid_packages.append((package, avail_package_dict[package][0], avail_package_dict[package][1]))

        if len(valid_packages) > 0:
            # Need to find all the sets with gaps
            non_full_set_indexes = get_non_full_set_indexes(set_thresholds, W)

            # Empty all the non-full sets first
            for index in non_full_set_indexes:
                cur_set = p_sets[index]

                while len(cur_set) > 0:
                    cur_set_item = cur_set.pop()
                    valid_packages.insert(0, (cur_set_item, readonly_package_dict[cur_set_item][0],
                                              readonly_package_dict[cur_set_item][1]))
                    set_thresholds[index] -= readonly_package_dict[cur_set_item][1]
                    set_rewards[index] -= readonly_package_dict[cur_set_item][0]

            # Then perform best fit
    return p_sets


def get_next_fit_index(p_sets, thresholds, rewards, cur_item_w, limit):
    # Get all indexes that have exceeded the thresholds in accordance to cur_item_w
    banned_set_indexes = get_exceeded_indexes(thresholds, cur_item_w, limit)
    # Always prioritise rewards first
    l_rw_i = get_lowest_reward(rewards, banned_set_indexes)  # Lowest reward index

    return l_rw_i[0]


def get_lowest_reward(rewards, blacklisted=[]):
    lowest = (-1, sys.maxsize)
    for i in range(len(rewards)):
        if rewards[i] < lowest[1] and i not in blacklisted:
            lowest = (i, rewards[i])
    return lowest


def get_exceeded_indexes(thresholds, cur_item_w, lim):
    res = []

    for i in range(len(thresholds)):
        if thresholds[i] + cur_item_w > lim:
            res.append(i)

    return res


def get_non_full_set_indexes(thresholds, limit):
    non_full_set_indexes = []
    for i in range(len(thresholds)):
        if thresholds[i] < limit:
            non_full_set_indexes.append(i)

    return non_full_set_indexes
