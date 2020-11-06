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
from Project.q1 import select_packageSet


def select_packageSets(n, W, packages):
    # Just define a fixed dictionary here.
    package_dict = get_package_dict(packages)
    # Ensure it doesn't exist here.
    used_packages = set()

    # Split into chunks, sort them via profitability.
    # Profitability = reward/weight
    # Best to worst
    valueMergeSort(packages)

    # Take the best packages till we hit the total weight limit
    weight_total = 0
    max_index = 0
    for i in range(len(packages)):
        if weight_total > (W * n):
            max_index = i
            break
        weight_total += packages[i][2]

    unused_packages = packages[max_index:]
    packages = packages[:max_index]

    # We can multi-init like that
    # https://stackoverflow.com/questions/6142689/initialising-an-array-of-fixed-size-in-python
    set_threshold = [0] * n
    package_sets = []
    while len(package_sets) < n:
        package_sets.append([])

    # BEGIN FULL BIN PACKING ALGORITHM
    weightMergeSort(packages)  # Sort by the weight first since we're done filtering out what's nonsense.
    while len(packages) > 0:
        # Obtain the biggest package
        package = packages.pop(0)

        if package[0] not in used_packages:
            # Find the first bin that can accommodate
            first_avail = get_avail_member(set_threshold, W, package[2])

            package_sets[first_avail].append(package[0])
            set_threshold[first_avail] += package[2]
            used_packages.add(package[0])

    # Check out the thresholds, the last one should be incomplete.
    for i in range(len(set_threshold)):
        # Since the threshold is not maxed, lets see if we can max it out.
        if set_threshold[i] < W:
            # Clear up
            for package_id in package_sets[i]:
                used_packages.remove(package_id)
                arr = package_dict[package_id]
                arr.insert(0, package_id)
                unused_packages.insert(0, arr)
            package_sets[i].clear()
            set_threshold[i] = 0

    packages = unused_packages
    for i in range(len(packages) - 1):
        if packages[i][0] in used_packages:
            del packages[i]
    package_sets[len(package_sets) - 1] = select_packageSet(W, packages)
    # while len(packages) > 0:
    #     # Obtain the biggest package
    #     package = packages.pop(0)
    #
    #     # Ensure its never used.
    #     if package[0] not in used_packages:
    #         if set_threshold[len(package_sets) - 1] + package[2] <= W:
    #             package_sets[len(package_sets) - 1].append(package[0])
    #             set_threshold[len(package_sets) - 1] += package[2]
    #             used_packages.add(package[0])

    return package_sets


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


def valueMergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        valueMergeSort(L)  # Sort the first half
        valueMergeSort(R)  # Sort the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            # Profitability = reward/weight
            if L[i][1] / L[i][2] > R[j][1] / R[j][2]:
                # if (L[i][2] < R[j][2]) or (L[i][2] == R[j][2] and L[i][1] / L[i][2] < R[j][1] / R[j][2]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1


def weightMergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        weightMergeSort(L)  # Sort the first half
        weightMergeSort(R)  # Sort the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            # weight
            if L[i][2] > R[j][2]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
