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
import numpy
import sys


def select_packageSets(n, W, packages, variations=200):
    readonly_package_dict = {pkg[0]: pkg[1:] for pkg in packages}
    avail_packages = copy.deepcopy(packages)
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

    # Setup the bins
    set_thresholds = [0] * n
    set_rewards = [0] * n
    p_sets = []
    while len(p_sets) < n:
        p_sets.append([])

    if max_index == len(packages) - 1:
        packages.sort(key=lambda x: x[1], reverse=True)
    elif max_index < len(packages) - 1:
        overflowing_packages = packages[max_index + 1:]
        overflowing_packages.sort(key=lambda x: x[1], reverse=True)
        packages = packages[:max_index + 1] + overflowing_packages

    while can_still_fit(set_thresholds, avail_packages, W):
        for package in packages:
            # Try to fit item into a bin
            i = get_next_fit_index(p_sets, set_thresholds, set_rewards, package[2], W)

            if i > -1:
                # print 'Adding', item, 'to', bin
                p_sets[i].append(package[0])
                set_thresholds[i] += package[2]
                set_rewards[i] += package[1]
                del avail_packages[avail_packages.index(package)]

    # while can_still_fit_differential((n * W) - sum(set_thresholds), avail_packages):
    #     print()

    reduce_deviation(readonly_package_dict, p_sets, set_thresholds, set_rewards, W)

    while True:
        # differential = (n * W) - sum(set_thresholds)
        can_fit = can_still_fit_differential((n * W) - sum(set_thresholds), avail_packages)
        least_filled_set_index = get_least_filled_set_index(set_thresholds)
        if least_filled_set_index < 0 and not can_fit:
            break
        one_last_time = get_best_fit_in_set(set_thresholds[least_filled_set_index], avail_packages, W)
        if one_last_time is None and not can_fit:
            break
        if one_last_time is not None:
            p_sets[least_filled_set_index].append(one_last_time[0])
            set_rewards[least_filled_set_index] += one_last_time[1]
            set_thresholds[least_filled_set_index] += one_last_time[2]
            avail_packages.remove(one_last_time)

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


def get_best_fit_in_set(threshold, available_packages, limit):
    available_packages.sort(key=lambda x: (x[1] / x[2]), reverse=True)
    for package in available_packages:
        if threshold + package[2] <= limit:
            return package

    return None


def can_still_fit(thresholds, available_packages, limit):
    for package in available_packages:
        for threshold in thresholds:
            if threshold + package[2] <= limit:
                return True

    return False


def can_still_fit_differential(differential, available_packages):
    for package in available_packages:
        if differential - package[2] >= 0:
            return True

    return False


def get_least_filled_set_index(thresholds):
    smallest_threshold = (-1, sys.maxsize)
    for i in range(len(thresholds)):
        if thresholds[i] < smallest_threshold[1]:
            smallest_threshold = (i, thresholds[i])

    return smallest_threshold[0]


def get_most_filled_set_index(thresholds):
    biggest_threshold = (-1, -sys.maxsize)
    for i in range(len(thresholds)):
        if thresholds[i] > biggest_threshold[1]:
            biggest_threshold = (i, thresholds[i])

    return biggest_threshold[0]


def reduce_deviation(package_dict, p_sets, set_thresholds, set_rewards, W):
    # set_threshold_ranking = numpy.argsort(set_thresholds)
    reward_sd = numpy.std(set_rewards)
    set_reward_ranking = numpy.argsort(set_rewards)
    set_combinations_left = choose(len(p_sets), 2)
    lower = 0
    upper = lower + 1
    while set_combinations_left > 0:
        least_reward_index = set_reward_ranking[lower]
        lower_set_threshold = set_thresholds[least_reward_index]
        least_reward_set_reward = set_rewards[least_reward_index] + 0
        most_reward_index = set_reward_ranking[upper]
        upper_set_threshold = set_thresholds[most_reward_index]
        most_reward_set_reward = set_rewards[most_reward_index] + 0
        orig_reward_sd = numpy.std([least_reward_set_reward, most_reward_set_reward])

        if orig_reward_sd > 5:
            new_reward_sd = orig_reward_sd + 0

            least_reward_set = regenerate_set(package_dict, p_sets[least_reward_index])
            least_reward_set.sort(key=lambda x: (x[2]))
            most_reward_set = regenerate_set(package_dict, p_sets[most_reward_index])
            most_reward_set.sort(key=lambda x: (x[2]))

            iter_allowed = len(p_sets[least_reward_index]) * len(p_sets[most_reward_index])
            set_lower = 0
            set_upper = 0
            while new_reward_sd >= orig_reward_sd and iter_allowed > 0 and len(least_reward_set) > 0 \
                    and len(most_reward_set) > 0:
                lrs_least_profitable = least_reward_set.pop(set_lower)
                if set_upper >= len(most_reward_set):
                    print()
                mrs_least_profitable = most_reward_set.pop(set_upper)

                if (lrs_least_profitable[1] / lrs_least_profitable[2]) < (mrs_least_profitable[1] / mrs_least_profitable[2]) \
                        and (numpy.std([least_reward_set_reward - (lrs_least_profitable[1] + mrs_least_profitable[1]),
                                        most_reward_set_reward - (mrs_least_profitable[1] + lrs_least_profitable[1])])) \
                        and (lower_set_threshold - lrs_least_profitable[2] + mrs_least_profitable[2] <= W) \
                        and (upper_set_threshold - mrs_least_profitable[2] + lrs_least_profitable[2] <= W):
                    # Reduce
                    least_reward_set_reward -= lrs_least_profitable[1]
                    lower_set_threshold -= lrs_least_profitable[2]
                    most_reward_set_reward -= mrs_least_profitable[1]
                    upper_set_threshold -= mrs_least_profitable[2]

                    # Increase
                    least_reward_set_reward += mrs_least_profitable[1]
                    lower_set_threshold += mrs_least_profitable[2]
                    most_reward_set_reward += lrs_least_profitable[1]
                    upper_set_threshold += lrs_least_profitable[2]

                    # Replace
                    least_reward_set.append(mrs_least_profitable)
                    most_reward_set.append(lrs_least_profitable)

                    new_reward_sd = numpy.std([least_reward_set_reward, most_reward_set_reward])
                else:
                    least_reward_set.append(lrs_least_profitable)
                    most_reward_set.append(mrs_least_profitable)

                iter_allowed -= 1

                if set_upper == len(most_reward_set) - 1 and set_lower + 1 < len(least_reward_set):
                    set_lower += 1
                    set_upper = 0
                elif set_upper + 1 < len(most_reward_set):
                    set_upper += 1
                else:
                    break

            if new_reward_sd < orig_reward_sd:
                p_sets[least_reward_index] = [tuple[0] for tuple in least_reward_set]
                p_sets[most_reward_index] = [tuple[0] for tuple in most_reward_set]

                set_thresholds[least_reward_index] = lower_set_threshold
                set_thresholds[most_reward_index] = upper_set_threshold

                set_rewards[least_reward_index] = least_reward_set_reward
                set_rewards[most_reward_index] = most_reward_set_reward

        reward_sd = numpy.std(set_rewards)
        set_combinations_left -= 1
        if upper == len(set_rewards) - 1:
            lower += 1
            upper = 0
        else:
            upper += 1


def regenerate_set(package_dict, p_set):
    res = []

    for i in p_set:
        if i in package_dict.keys():
            res.append((i, package_dict[i][0], package_dict[i][1]))
        else:
            print("Critical! Key " + str(i) + " missing!")

    return res


def choose(n, k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return choose(n - 1, k - 1) + choose(n - 1, k)
