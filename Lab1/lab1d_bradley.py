def gcd_d_bradley(x, y):
    k = 0
    # https://stackoverflow.com/questions/15112125/how-to-test-multiple-variables-against-a-value
    if 0 in { x, y }: return 1  # immediately exit the user
    print("x:", x)
    print("y:", y)

    # while x and y % 2 == 0: <= This is not equal to the statement below
    while x % 2 == 0 and y % 2 == 0: # while both x and y are even
        x = x / 2
        y = y / 2
        k = k + 1

    while x != y:
        if x % 2 == 0:
            x = x / 2
        elif y % 2 == 0:
            y = y / 2
        elif x > y:
            x = (x - y) / 2
        else:
            y = (y - x) / 2

    result = x * (2 ** k)
    return result