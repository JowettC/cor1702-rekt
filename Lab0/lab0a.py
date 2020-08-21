# Name: Nicholas Chen Han Wei
# Section: G7

# lab0a

# All statements should only be in functions. Do not include statements outside functions in this file.
# fill up the admit method to return either True or False depending on the sex and age
def admit(sex, age):
    if sex is "M":
        return age >= 23
    elif sex is "F":
        return age >= 18
    return False
