# Name: Nicholas Chen Han Wei
# Section: G7

# lab0b

# All statements should only be in functions. Do not include statements outside functions in this file.
# fill up the weight_category method to return either "underweight", "overweight" or "normal" 
# depending on the height (in cm) and weight (in kg)
def weight_category(weight, height):
    bmi = weight / (height ** height)
    if bmi <= 0:
        return "incorrect weight/height value!"

    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi <= 25:
        return "normal"
    else:
        return "overweight"
