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


def select_packageSets(n, W, packages):
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
        packages.sort(key=lambda x: (x[2]), reverse=True)
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

    fresh_deviation = numpy.std(set_rewards)
    fresh_set = copy.deepcopy(p_sets)
    fresh_thresholds = copy.deepcopy(set_thresholds)
    fresh_rewards = copy.deepcopy(set_rewards)

    while can_still_fit_differential((n * W) - sum(set_thresholds), avail_packages):
        shifted_deviation = numpy.std(set_rewards)
        if shifted_deviation > fresh_deviation:
            reduce_deviation(readonly_package_dict, p_sets, set_thresholds, set_rewards, W)

        least_filled_set_index = get_least_filled_set_index(set_thresholds)
        if least_filled_set_index < 0 and not can_still_fit_differential((n * W) - sum(set_thresholds), avail_packages):
            break
        one_last_time = get_best_fit_in_set(set_thresholds[least_filled_set_index], avail_packages, W)
        if one_last_time is None and not can_still_fit_differential((n * W) - sum(set_thresholds), avail_packages):
            break
        if one_last_time is not None:
            p_sets[least_filled_set_index].append(one_last_time[0])
            set_rewards[least_filled_set_index] += one_last_time[1]
            set_thresholds[least_filled_set_index] += one_last_time[2]
            avail_packages.remove(one_last_time)

        if not fill_smallest(readonly_package_dict, avail_packages, p_sets, set_thresholds, set_rewards,
                             W) and not can_still_fit_differential((n * W) - sum(set_thresholds), avail_packages):
            break
        else:
            skewer(readonly_package_dict, p_sets, set_thresholds, set_rewards, W, avail_packages)

        if shifted_deviation == numpy.std(set_rewards):
            break

    # reduce_deviation(readonly_package_dict, p_sets, set_thresholds, set_rewards, W)
    post_differential_deviation = numpy.std(set_rewards)
    if post_differential_deviation > fresh_deviation:
        p_sets = fresh_set
        set_thresholds = fresh_thresholds
        set_rewards = fresh_rewards

    if max_index < len(packages) - 1 or post_differential_deviation > fresh_deviation:
        new_deviation = numpy.std(set_rewards)
        while True:
            prev_deviation = numpy.std(set_rewards)
            reduce_deviation(readonly_package_dict, p_sets, set_thresholds, set_rewards, W)
            new_deviation = numpy.std(set_rewards)

            if prev_deviation == new_deviation:
                break

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


def compute_threshold(package_dict, p_set):
    threshold = 0
    for p in p_set:
        if p in package_dict.keys():
            threshold += package_dict[p][1]

    return threshold


def compute_reward(package_dict, p_set):
    reward = 0
    for p in p_set:
        if p in package_dict.keys():
            reward += package_dict[p][0]

    return reward


def reduce_deviation(package_dict, p_sets, set_thresholds, set_rewards, W):
    # reward_sd = numpy.std(set_rewards)
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

                if (lrs_least_profitable[1] / lrs_least_profitable[2]) < (
                        mrs_least_profitable[1] / mrs_least_profitable[2]) \
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


def fill_smallest(package_dict, avail_packages, p_sets, set_thresholds, set_rewards, W):
    set_threshold_ranking = numpy.argsort(set_thresholds)

    if len(set_threshold_ranking) >= 2:
        lightest_index = set_threshold_ranking[0]
        heavier_index = set_threshold_ranking[1]

        # Drain and fit
        smaller_package_set = regenerate_set(package_dict, p_sets[lightest_index] + p_sets[heavier_index])
        heavier_package_set = select_packageSet(W, smaller_package_set)
        smaller_set_threshold = sum([package[2] for package in smaller_package_set])
        smaller_package_set = [package[0] for package in smaller_package_set]

        # Get the heavier out of the way first
        set_thresholds[heavier_index] = compute_threshold(package_dict, heavier_package_set)
        set_rewards[heavier_index] = compute_reward(package_dict, heavier_package_set)
        p_sets[heavier_index] = heavier_package_set

        # Additional fit
        for package in avail_packages:
            if package[2] + smaller_set_threshold <= W:
                smaller_set_threshold += package[2]
                smaller_package_set.append(package[0])

        set_thresholds[lightest_index] = smaller_set_threshold
        set_rewards[lightest_index] = compute_reward(package_dict, smaller_package_set)
        p_sets[lightest_index] = smaller_package_set

        if can_still_fit([set_thresholds[lightest_index], set_thresholds[heavier_index]], avail_packages, W):
            return True
        else:
            return False
    return False


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


def skewer(package_dict, p_sets, set_thresholds, set_rewards, W, avail_packages):
    # threshold_ordering = numpy.argsort(set_thresholds)
    is_rising = numpy.all(numpy.diff(numpy.argsort(set_thresholds)) >= 0)
    cur_ordering = copy.deepcopy(set_thresholds)
    while not is_rising:
        if not can_still_fit(set_thresholds, avail_packages, W):
            break

        for i in range(len(p_sets) - 1, -1, -1):
            if set_thresholds[i] < W:
                # Check all sets to the left and find packages to shift to.
                for j in range(i - 1, -1, -1):
                    k = len(p_sets[j]) - 1
                    while k > -1:
                        if (package_dict[p_sets[j][k]][1] + set_thresholds[i]) <= W:
                            set_thresholds[i] += package_dict[p_sets[j][k]][1]
                            set_rewards[i] += package_dict[p_sets[j][k]][0]
                            set_thresholds[j] -= package_dict[p_sets[j][k]][1]
                            set_rewards[j] -= package_dict[p_sets[j][k]][0]
                            p_sets[i].append(p_sets[j][k])
                            p_sets[j].remove(p_sets[j][k])

                        if set_thresholds[i] == W:
                            break

                        k -= 1

                    if set_thresholds[i] == W:
                        break
        is_rising = numpy.all(numpy.diff(set_thresholds) >= 0)
        new_ordering = copy.deepcopy(set_thresholds)

        if cur_ordering == new_ordering:
            break
        else:
            cur_ordering = new_ordering

    if not is_rising:
        is_falling = numpy.all(numpy.diff(numpy.argsort(set_thresholds[::-1])) >= 0)
        while not is_falling:
            if not can_still_fit(set_thresholds, avail_packages, W):
                break
            for i in range(len(p_sets) - 1):
                if set_thresholds[i] < W:
                    # Check all sets to the left and find packages to shift to.
                    for j in range(i + 1, len(set_thresholds)):
                        k = len(p_sets[j]) - 1
                        while k > -1:
                            if (package_dict[p_sets[j][k]][1] + set_thresholds[i]) <= W:
                                set_thresholds[i] += package_dict[p_sets[j][k]][1]
                                set_rewards[i] += package_dict[p_sets[j][k]][0]
                                set_thresholds[j] -= package_dict[p_sets[j][k]][1]
                                set_rewards[j] -= package_dict[p_sets[j][k]][0]
                                p_sets[i].append(p_sets[j][k])
                                p_sets[j].remove(p_sets[j][k])

                            if set_thresholds[i] == W:
                                break

                            k -= 1

                        if set_thresholds[i] == W:
                            break
            is_falling = numpy.all(numpy.diff(numpy.argsort(set_thresholds[::-1])) >= 0)
            new_ordering = copy.deepcopy(set_thresholds)

            if cur_ordering == new_ordering:
                break
            else:
                cur_ordering = new_ordering


# Adapted from Q1.
def select_packageSet(W, packages):
    val = [package[1] for package in packages]
    wt = [package[2] for package in packages]
    package = [package[0] for package in packages]
    package_select = []

    selected_wt_index = knapSack(W, wt, val, len(val))

    for wt_index in selected_wt_index:
        package_select.append(package[wt_index])
        del packages[wt_index]

    return package_select


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
