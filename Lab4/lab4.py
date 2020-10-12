# Name: Nicholas Chen Han Wei
# Section: G7

# lab4

# All statements should only be in functions. Do not include statements outside functions in this file.

def select_tweeters(followers):
    sorted_followers = []

    # This loop performs a primitive 1-layer check against all users, ignoring an internal sorted_followers comparison.
    for i in range(len(followers)):
        # If theres no sorted follower atm, push one in
        if len(sorted_followers) == 0:
            sorted_followers.append(i)
        else:
            # Loop every sorted follower and compare
            for j in range(len(sorted_followers) - 1, -1, -1):
                # Current Sorted Follower index in accordance to followers
                cs_index = sorted_followers[j]
                # When the current user has more followers than the currently sorted
                if (len(followers[i]) > len(followers[cs_index])) and (count_deficit(followers[i], followers[cs_index]) > 0) and len(sorted_followers) > 5:
                    # Remove the first dude
                    sorted_followers.pop(0)
                    # Insert the current dude at index j, push the upper boys to the right.
                    sorted_followers.insert(j, i)
                    break  # Always break out of the loop.
                elif len(sorted_followers) < 5:
                    if (len(followers[i]) > len(followers[cs_index])) and (count_deficit(followers[i], followers[cs_index]) > 0):
                        # Insert the current dude at index j, push the upper boys to the right.
                        sorted_followers.insert(j + 1, i)
                        break  # Always break out of the loop.
                    elif j == 0:
                        sorted_followers.insert(0, i)

    return sorted_followers


# Function to compare the difference between u1 and u2 followers, ensures that only unique followers are counted.
def count_deficit(u1, u2):
    if len(u1) == 0 and len(u2) > 0:
        return -len(u2)
    elif len(u2) == 0 and len(u1) > 0:
        return -len(u1)
    elif len(u1) == 0 and len(u2) == 0:
        return 0

    difference = 0
    for f in u1:
        found = False
        for f2 in u2:
            found = f == f2

        if not found:
            difference += 1

    for f in u2:
        found = False
        for f2 in u1:
            found = f == f2

        if not found:
            difference -= 1

    return difference
