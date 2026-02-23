"""
Numeric Types and Boolean Logic Assignment
"""


# ==================================================
# Problem 1: Temperature Converter and Range Flag
# ==================================================
"""
Description:
Converts temperature from Celsius to Fahrenheit and Kelvin.
Also determines whether the temperature is considered high (>= 30°C).

Inputs:
- temp_c (float)

Outputs:
- Fahrenheit
- Kelvin
- High temperature (True/False)

Validations:
- Must be convertible to float
- Must not be below absolute zero (-273.15°C)

Test cases:
1) Normal: 25
2) Edge case: -273.15
3) Error: -300
"""

temp_input = input("Enter temperature in Celsius: ")

try:
    temp_c = float(temp_input)
    if temp_c < -273.15:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0

        print(f"Fahrenheit: {temp_f}")
        print(f"Kelvin: {temp_k}")
        print(f"High temperature: {is_high_temperature}")
except:
    print("Error: invalid input")


# ==================================================
# Problem 2: Work Hours and Overtime Payment
# ==================================================
"""
Description:
Calculates weekly salary including overtime (150% rate after 40 hours).
Also determines if overtime was worked.

Inputs:
- hours_worked (int)
- hourly_rate (float)

Outputs:
- Regular pay
- Overtime pay
- Total pay
- Has overtime

Validations:
- hours_worked >= 0
- hourly_rate > 0

Test cases:
1) Normal: 45, 100
2) Edge case: 40, 50
3) Error: -5, 100
"""
hours_input = input("Enter hours worked: ")
rate_input = input("Enter hourly rate: ")

try:
    hours_worked = int(hours_input)
    hourly_rate = float(rate_input)

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40

        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")
        print(f"Has overtime: {has_overtime}")
except:
    print("Error: invalid input")


# ==================================================
# Problem 3: Discount Eligibility with Booleans
# ==================================================
"""
Description:
Determines if a customer qualifies for a discount.
Eligible if student OR senior OR purchase >= 1000.

Inputs:
- purchase_total (float)
- is_student_text ("YES"/"NO")
- is_senior_text ("YES"/"NO")

Outputs:
- Discount eligible
- Final total

Validations:
- purchase_total >= 0
- Text inputs must be YES or NO

Test cases:
1) Normal: 500, YES, NO
2) Edge case: 1000, NO, NO
3) Error: 300, MAYBE, NO
"""

purchase_input = input("Enter purchase total: ")
student_text = input("Is student (YES/NO): ").strip().upper()
senior_text = input("Is senior (YES/NO): ").strip().upper()

try:
    purchase_total = float(purchase_input)

    if purchase_total < 0 or student_text not in ["YES", "NO"] or senior_text not in ["YES", "NO"]:
        print("Error: invalid input")
    else:
        is_student = student_text == "YES"
        is_senior = senior_text == "YES"

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
        final_total = purchase_total * 0.9 if discount_eligible else purchase_total

        print(f"Discount eligible: {discount_eligible}")
        print(f"Final total: {final_total}")
except:
    print("Error: invalid input")


# ==================================================
# Problem 4: Basic Statistics of Three Integers
# ==================================================
"""
Description:
Reads three integers and calculates sum, average, max, min,
and checks if all are even.

Inputs:
- n1, n2, n3 (int)

Outputs:
- Sum
- Average
- Max
- Min
- All even

Validations:
- Must be valid integers

Test cases:
1) Normal: 2, 4, 6
2) Edge case: -1, 0, 1
3) Error: a, 2, 3
"""
n1_input = input("Enter first integer: ")
n2_input = input("Enter second integer: ")
n3_input = input("Enter third integer: ")

try:
    n1 = int(n1_input)
    n2 = int(n2_input)
    n3 = int(n3_input)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")
except:
    print("Error: invalid input")


# ==================================================
# Problem 5: Loan Eligibility
# ==================================================
"""
Description:
Determines loan eligibility based on income, debt ratio,
and credit score.

Inputs:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)

Outputs:
- Debt ratio
- Eligible

Validations:
- monthly_income > 0
- monthly_debt >= 0
- credit_score >= 0

Test cases:
1) Normal: 10000, 3000, 700
2) Edge case: 8000, 3200, 650
3) Error: 0, 1000, 500
"""

income_input = input("Enter monthly income: ")
debt_input = input("Enter monthly debt: ")
score_input = input("Enter credit score: ")

try:
    monthly_income = float(income_input)
    monthly_debt = float(debt_input)
    credit_score = int(score_input)

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= 8000.0 and
            debt_ratio <= 0.4 and
            credit_score >= 650
        )

        print(f"Debt ratio: {debt_ratio}")
        print(f"Eligible: {eligible}")
except:
    print("Error: invalid input")


# ==================================================
# Problem 6: Body Mass Index (BMI)
# ==================================================
"""
Description:
Calculates BMI and determines category flags.

Inputs:
- weight_kg (float)
- height_m (float)

Outputs:
- BMI (rounded to 2 decimals)
- Underweight
- Normal
- Overweight

Validations:
- weight_kg > 0
- height_m > 0

Test cases:
1) Normal: 70, 1.75
2) Edge case: 50, 1.80
3) Error: -60, 1.70
"""

weight_input = input("Enter weight (kg): ")
height_input = input("Enter height (m): ")

try:
    weight_kg = float(weight_input)
    height_m = float(height_input)

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m ** 2)
        bmi_rounded = round(bmi, 2)

        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print(f"BMI: {bmi_rounded}")
        print(f"Underweight: {is_underweight}")
        print(f"Normal: {is_normal}")
        print(f"Overweight: {is_overweight}")
except:
    print("Error: invalid input")
