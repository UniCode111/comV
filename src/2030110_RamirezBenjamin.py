"""
Author: Benjamin Ramirez Canela
Description: This code is intended to practice lists, functions, 
"""


# --------------------------------------------------
# Problem 1: Rectangle area and perimeter
# --------------------------------------------------
# Description:
# Calculates the area and perimeter of a rectangle using two
# separate functions. Input values are validated before calling
# the functions.
#
# Inputs:
# - width (float)
# - height (float)
#
# Outputs:
# - Area
# - Perimeter
#
# Validations:
# - width > 0
# - height > 0
#
# Test cases:
# 1) Normal: width=5, height=3
# 2) Edge case: width=0.1, height=0.1
# 3) Error: width=-2, height=4


def calculate_area(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


width = 5
height = 3

if width > 0 and height > 0:
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)
    print("Area:", area)
    print("Perimeter:", perimeter)
else:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Grade classifier
# --------------------------------------------------
# Description:
# Classifies a numeric score into a letter grade.
#
# Inputs:
# - score (int or float)
#
# Outputs:
# - Category (A, B, C, D, F)
#
# Validations:
# - 0 <= score <= 100
#
# Test cases:
# 1) Normal: score=85
# 2) Edge case: score=100
# 3) Error: score=120


def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


score = 85

if 0 <= score <= 100:
    category = classify_grade(score)
    print("Score:", score)
    print("Category:", category)
else:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 3: List statistics
# --------------------------------------------------
# Description:
# Receives a list of numbers and returns a dictionary including min, max, and average.
#
# Inputs:
# - numbers_text (string)
#
# Outputs:
# - Min
# - Max
# - Average
#
# Validations:
# - Non-empty input
# - All elements must be numeric
#
# Test cases:
# 1) Normal: "10,20,30"
# 2) Edge case: "5"
# 3) Error: "10,a,30"


def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }


numbers_text = "10,20,30"

numbers_text = numbers_text.strip()

if numbers_text:
    try:
        numbers = []
        for item in numbers_text.split(","):
            numbers.append(float(item.strip()))

        if numbers:
            summary = summarize_numbers(numbers)
            print("Min:", summary["min"])
            print("Max:", summary["max"])
            print("Average:", summary["average"])
        else:
            print("Error: invalid input")

    except ValueError:
        print("Error: invalid input")
else:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 4: Apply discount list (pure function)
# --------------------------------------------------
# Description:
# Applies a discount to a list of prices without modifying
# the original list.
#
# Inputs:
# - prices_text (string)
# - discount_rate (float)
#
# Outputs:
# - Original prices
# - Discounted prices
#
# Validations:
# - prices > 0
# - 0 <= discount_rate <= 1
#
# Test cases:
# 1) Normal: "100,200,300", 0.10
# 2) Edge case: "50", 0
# 3) Error: "100,-20", 0.2

