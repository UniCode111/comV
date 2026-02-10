# --------------------------------------------------
# Functions practice – input + validation
# --------------------------------------------------

# --------------------------------------------------
# Problem 1: Rectangle area and perimeter
# --------------------------------------------------
# Description:
# Reads width and height from the user and calculates
# the area and perimeter of a rectangle.
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
# 1) Normal: 5, 3
# 2) Edge: 0.1, 0.1
# 3) Error: -2, 4

def calculate_area(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


try:
    width = float(input("Width: ").strip())
    height = float(input("Height: ").strip())

    if width > 0 and height > 0:
        print("Area:", calculate_area(width, height))
        print("Perimeter:", calculate_perimeter(width, height))
    else:
        print("Error: invalid input")
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Grade classifier
# --------------------------------------------------
# Description:
# Classifies a numeric grade into a letter category.
#
# Inputs:
# - score (float or int)
#
# Outputs:
# - Score
# - Category
#
# Validations:
# - 0 <= score <= 100
#
# Test cases:
# 1) Normal: 85
# 2) Edge: 100
# 3) Error: 120

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


try:
    score = float(input("Score: ").strip())

    if 0 <= score <= 100:
        print("Score:", score)
        print("Category:", classify_grade(score))
    else:
        print("Error: invalid input")
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 3: List statistics
# --------------------------------------------------
# Description:
# Reads a comma-separated list of numbers and calculates
# min, max and average.
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
# - Non-empty list
# - All values numeric
#
# Test cases:
# 1) Normal: "10,20,30"
# 2) Edge: "5"
# 3) Error: "10,a,30"

def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }


numbers_text = input("Numbers (comma separated): ").strip()

parts = numbers_text.split(",")
numbers = []
valid = True

for part in parts:
    part = part.strip()
    try:
        numbers.append(float(part))
    except ValueError:
        valid = False

if valid and len(numbers) > 0:
    result = summarize_numbers(numbers)
    print("Min:", result["min"])
    print("Max:", result["max"])
    print("Average:", result["average"])
else:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 4: Apply discount list
# --------------------------------------------------
# Description:
# Applies a discount to a list of prices without
# modifying the original list.
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
# 1) Normal: "100,200,300", 0.1
# 2) Edge: "50", 0
# 3) Error: "100,-20", 0.2

def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        discounted.append(price * (1 - discount_rate))
    return discounted


prices_text = input("Prices: ").strip()
discount_text = input("Discount rate: ").strip()

prices = []
valid = True

try:
    discount_rate = float(discount_text)
except ValueError:
    valid = False

for part in prices_text.split(","):
    part = part.strip()
    try:
        value = float(part)
        if value > 0:
            prices.append(value)
        else:
            valid = False
    except ValueError:
        valid = False

if valid and 0 <= discount_rate <= 1 and len(prices) > 0:
    print("Original prices:", prices)
    print("Discounted prices:", apply_discount(prices, discount_rate))
else:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 5: Greeting function
# --------------------------------------------------
# Description:
# Generates a greeting with optional title.
#
# Inputs:
# - name (string)
# - title (string, optional)
#
# Outputs:
# - Greeting
#
# Validations:
# - name not empty
#
# Test cases:
# 1) Normal: Alice, Dr.
# 2) Edge: Bob
# 3) Error: ""

def greet(name, title=""):
    name = name.strip()
    title = title.strip()

    if title != "":
        return "Hello, " + title + " " + name + "!"
    else:
        return "Hello, " + name + "!"


name = input("Name: ").strip()
title = input("Title (optional): ").strip()

if name != "":
    print("Greeting:", greet(name, title))
else:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 6: Factorial
# --------------------------------------------------
# Description:
# Calculates factorial using a for loop.
#
# Inputs:
# - n (int)
#
# Outputs:
# - n
# - Factorial
#
# Validations:
# - 0 <= n <= 20
#
# Test cases:
# 1) Normal: 5
# 2) Edge: 0
# 3) Error: -3

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


try:
    n = int(input("n: ").strip())

    if 0 <= n <= 20:
        print("n:", n)
        print("Factorial:", factorial(n))
    else:
        print("Error: invalid input")
except ValueError:
    print("Error: invalid input")

