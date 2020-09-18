# Name: Nicholas Chen Han Wei
# Section: G7

# lab3b

# All statements should only be in functions. Do not include statements outside functions in this file.


# Takes in a base-10 integer and returns the base-2 (binary) equivalent as a string
# this function does NOT have to handle negative numbers (i.e. d will always be >=0)
# this function must NOT use Python's bin() function.
# this function must be recursive (i.e. it calls itself)
# there should not be leading zeros in the string that this function returns.
def to_binary_old(d):
    # Base-10 -> 0 1 2 3 4 5 6 7 8 9
    # Base-2 -> 0 1
    # 6 => 110
    bin_res = ["0", "0", "0", "0"]
    cur_val = d % 10
    if cur_val // 2 ** 3 > 0:
        bin_res[0] = "1"
        cur_val -= 2 ** 3
    if cur_val // 2 ** 2 > 0:
        bin_res[1] = "1"
        cur_val -= 2 ** 2
    if cur_val // 2 ** 1 > 0:
        bin_res[2] = "1"
        cur_val -= 2 ** 1
    if cur_val // 2 ** 0 > 0:
        bin_res[3] = "1"
        cur_val -= 2 ** 0

    return "".join(bin_res) if d // 10 == 0 else to_binary_old(d // 10) + "".join(bin_res)


def to_binary(d):
    return 0 if d == 0 else (d % 2 + 10 * to_binary(int(d // 2)))


#   10000101010001 - Correct Answer
#   10000101010001
# 1000010100101001 -
