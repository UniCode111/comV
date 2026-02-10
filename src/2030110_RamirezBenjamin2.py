# --------------------------------------------------
# Problem 1: Sum of integers in a range
# --------------------------------------------------
# Description:
# Calculates the sum of all integers from 1 to n, and
# also calculates the sum of even numbers in the same range.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>
#
# Validations:
# - n must be convertible to int
# - n >= 1
#
# Test cases:
# 1) Normal: n = 5  -> Sum = 15, Even sum = 6
# 2) Edge: n = 1    -> Sum = 1, Even sum = 0
# 3) Error: n = -3  -> Error: invalid input

n_input = input("Enter n: ")

try:
    n = int(n_input)
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum = total_sum + i
            if i % 2 == 0:
                even_sum = even_sum + i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Multiplication table with for
# --------------------------------------------------
# Description:
# Displays the multiplication table of a base number
# from 1 up to a given limit.
#
# Inputs:
# - base (int)
# - m (int)
#
# Outputs:
# - "base x i = result"
#
# Validations:
# - base and m must be convertible to int
# - m >= 1
#
# Test cases:
# 1) Normal: base=5, m=4
# 2) Edge: base=3, m=1
# 3) Error: m=0

base_input = input("Enter base: ")
m_input = input("Enter limit: ")

try:
    base = int(base_input)
    m = int(m_input)

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
# --------------------------------------------------
# Description:
# Reads numbers until a sentinel value is entered.
# Calculates the average and count of valid numbers.
#
# Inputs:
# - number (float)
#
# Outputs:
# - "Count:" <count>
# - "Average:" <average>
#
# Validations:
# - Input must be convertible to float
# - Only numbers >= 0 are accepted
#
# Test cases:
# 1) Normal: 2, 4, 6, -1
# 2) Edge: 0, -1
# 3) Error: -1 only

SENTINEL_VALUE = -1

count = 0
total_sum = 0.0

while True:
    number_input = input("Enter number (-1 to stop): ")

    try:
        number = float(number_input)

        if number == SENTINEL_VALUE:
            break
        elif number < 0:
            print("Error: invalid input")
        else:
            total_sum = total_sum + number
            count = count + 1
    except ValueError:
        print("Error: invalid input")

if count == 0:
    print("Error: no data")
else:
    average = total_sum / count
    print("Count:", count)
    print("Average:", average)


# --------------------------------------------------
# Problem 4: Password attempts with while
# --------------------------------------------------
# Description:
# Simulates a password system with limited attempts.
#
# Inputs:
# - user_password (string)
#
# Outputs:
# - "Login success" or "Account locked"
#
# Validations:
# - MAX_ATTEMPTS > 0
#
# Test cases:
# 1) Normal: correct password within attempts
# 2) Edge: correct password on last attempt
# 3) Error: all attempts incorrect

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3

attempts = 0

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
    else:
        attempts = attempts + 1

if attempts == MAX_ATTEMPTS:
    print("Account locked")


# --------------------------------------------------
# Problem 5: Simple menu with while
# --------------------------------------------------
# Description:
# Displays a menu that repeats until the user exits.
#
# Inputs:
# - option (int)
#
# Outputs:
# - Menu actions and messages
#
# Validations:
# - option must be convertible to int
#
# Test cases:
# 1) Normal: 1, 3, 2, 0
# 2) Edge: 0 immediately
# 3) Error: invalid option

counter = 0
option = -1

while option != 0:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_input = input("Select option: ")

    try:
        option = int(option_input)

        if option == 1:
            print("Hello!")
        elif option == 2:
            print("Counter:", counter)
        elif option == 3:
            counter = counter + 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
        else:
            print("Error: invalid option")
    except ValueError:
        print("Error: invalid option")


# --------------------------------------------------
# Problem 6: Pattern printing with nested loops
# --------------------------------------------------
# Description:
# Prints a right triangle pattern using asterisks.
#
# Inputs:
# - n (int)
#
# Outputs:
# - Star pattern line by line
#
# Validations:
# - n must be convertible to int
# - n >= 1
#
# Test cases:
# 1) Normal: n = 4
# 2) Edge: n = 1
# 3) Error: n = 0

n_input = input("Enter number of rows: ")

try:
    n = int(n_input)

    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            line = ""
            for j in range(i):
                line = line + "*"
            print(line)
except ValueError:
    print("Error: invalid input")
