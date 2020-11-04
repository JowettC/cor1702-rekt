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

def select_packageSets(n, W, packages):
    # Ensure it doesn't exist here.
    populated = set()

    # Split into chunks, sort them via profitability.
    # Profitability = reward/weight
    # Worst to Best
    valueMergeSort(packages)

    # Weight-based sorting
    weight_sorted_packages = packages.copy()
    weightedMergeSort(weight_sorted_packages)

    # We can multi-init like that
    # https://stackoverflow.com/questions/6142689/initialising-an-array-of-fixed-size-in-python
    set_threshold = [0] * n
    package_sets = []
    final_set = []
    while len(package_sets) < n:
        package_sets.append([])

    index = len(packages) - 1
    while len(package_sets) > 0:
        # Always traverse the shortest or smallest list
        curr_index = get_smallest_index(set_threshold)
        # Obtain the package with the current greatest profitability
        package = packages[index]

        # If the package in question has already been populated,
        if package[0] in populated:
            # Sort it out.
            weight_sorted_packages.remove(packages[index])
            del packages[index]
            index = (len(packages) - 1)
        # If the weight does not exceed if threshold with the current package,
        elif set_threshold[curr_index] + package[2] < W:
            set_threshold[curr_index] += package[2]
            package_sets[curr_index].append(package[0])
            populated.add(package[0])
            weight_sorted_packages.remove(packages[index])
            del packages[index]
            index -= 1

        # If we're done traversing downwards
        if index < 0 or all_have_exceeded(set_threshold, package[2], W):
            # We should begin traversing through weight, going by the weight calculation.
            for i in range(len(weight_sorted_packages) - 1, 0, -1):
                if weight_sorted_packages[i][0] not in populated and weight_sorted_packages[i][2] + set_threshold[curr_index] < W:
                    set_threshold[curr_index] += weight_sorted_packages[i][2]
                    package_sets[curr_index].append(weight_sorted_packages[i][0])
                    populated.add(weight_sorted_packages[i][0])
                    packages.remove(weight_sorted_packages[i])
                    del weight_sorted_packages[i]

            # Since we're done, we can assume we're done.
            index = len(packages) - 1
            final_set.append(package_sets.pop(curr_index))
            del set_threshold[curr_index]

    # curr_set = []
    # threshold = 0
    # index = len(packages) - 1
    # while len(package_sets) > 0:
    #     # Always traverse the shortest or smallest list
    #     curr_index = get_smallest_index(package_sets)
    #     # Obtain the package with the current greatest weight
    #     package = packages[index]
    #
    #     # If the package in question has already been populated,
    #     if package[0] in populated:
    #         # Sort it out.
    #         del packages[index]
    #         index = (len(packages) - 1)
    #     elif set_threshold[curr_index] + package[2] < W:
    #         set_threshold[curr_index] += package[2]
    #         package_sets[curr_index].append(package[0])
    #         populated.add(package[0])
    #         del packages[index]
    #         index -= 1
    #     else:
    #         packages.append(package)
    #         if index - 1 >= 0:
    #             index -= 1
    #         else:
    #             final_set.append(package_sets.pop(curr_index))
    #             del set_threshold[curr_index]
    #
    #     # If we're done traversing downwards or if the threshold + least profitable package
    #     if index < 0 or set_threshold[curr_index] + packages[0][2] > W:
    #         # Reset and push
    #         index = len(packages) - 1
    #         final_set.append(package_sets.pop(curr_index))
    #         del set_threshold[curr_index]



    # loop the packages first
    # while len(packages) > 0:
    #     # Obtain the current package
    #     cur_package = packages.pop()
    #     if cur_package[0] not in populated:
    #         # Loop every member
    #         for j in range(n):
    #             # If the threshold inclusive of the incoming new package to add is within the weight limit,
    #             if set_threshold[j] + cur_package[2] <= W:
    #                 package_sets[j].append(cur_package[0])
    #                 set_threshold[j] += cur_package[2]
    #                 populated.add(cur_package[0])
    #                 break

    # return [[P001, P003], [P011, P007], [P004, P005, P006], [P012]]
    return final_set


# you may insert other functions here, but all statements must be within functions
# before submitting to red, check that there are no print statements in your code. Nothing should be printed when your code runs.
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
            if L[i][1] / L[i][2] < R[j][1] / R[j][2]:
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


def weightedMergeSort(arr):
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
            if L[i][2] < R[j][2]:
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