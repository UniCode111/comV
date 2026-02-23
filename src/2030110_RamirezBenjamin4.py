"""
"""
# ==================================================
# Problem 1: Full Name Formatter
# ==================================================
"""
Description:
Normalizes a full name, formats it in Title Case,
and generates the initials separated by dots.

Inputs:
- full_name (string)

Outputs:
- Formatted name
- Initials

Validation:
- Must not be empty after strip()
- Must contain at least two words

Test cases:
1) Normal: "juan carlos tovar"
2) Edge case: "  ANA   LOPEZ  "
3) Error: "   "
"""

full_name = input("Enter full name: ").strip()

if full_name == "":
    print("Error: invalid input")
else:
    words = full_name.split()
    if len(words) < 2:
        print("Error: invalid input")
    else:
        formatted_name = " ".join(words).title()
        initials = ""
        for word in words:
            initials += word[0].upper() + "."
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")


# ==================================================
# Problem 2: Simple Email Validator
# ==================================================
"""
Description:
Validates a basic email structure.

Inputs:
- email_text (string)

Outputs:
- Valid email: True/False
- Domain if valid

Validation:
- Not empty
- Exactly one '@'
- No spaces
- Domain contains '.'

Test cases:
1) Normal: "user@mail.com"
2) Edge case: "USER@DOMAIN.CO"
3) Error: "user mail.com"
"""

email_text = input("Enter email: ").strip()

if email_text == "":
    print("Error: invalid input")
else:
    if email_text.count("@") == 1 and " " not in email_text:
        at_index = email_text.find("@")
        domain_part = email_text[at_index + 1:]
        if "." in domain_part and domain_part.find(".") > 0:
            print("Valid email: True")
            print(f"Domain: {domain_part}")
        else:
            print("Valid email: False")
    else:
        print("Valid email: False")


# ==================================================
# Problem 3: Palindrome Checker
# ==================================================
"""
Description:
Determines whether a phrase is a palindrome ignoring
spaces and case.

Inputs:
- phrase (string)

Outputs:
- Is palindrome: true/false

Validation:
- Not empty
- At least 3 characters after cleaning

Test cases:
1) Normal: "Anita lava la tina"
2) Edge case: "oso"
3) Error: "   "
"""


phrase = input("Enter phrase: ").strip()

if phrase == "":
    print("Error: invalid input")
else:
    normalized_phrase = phrase.lower().replace(" ", "")
    if len(normalized_phrase) < 3:
        print("Error: invalid input")
    else:
        is_palindrome = normalized_phrase == normalized_phrase[::-1]
        print(f"Normalized phrase: {normalized_phrase}")
        print(f"Is palindrome: {str(is_palindrome).lower()}")


# ==================================================
# Problem 4: Sentence Word Statistics
# ==================================================
"""
Description:
Analyzes a sentence and provides word statistics.

Inputs:
- sentence (string)

Outputs:
- Word count
- First word
- Last word
- Shortest word
- Longest word

Validation:
- Not empty
- At least one word

Test cases:
1) Normal: "Python is very powerful"
2) Edge case: "Hello"
3) Error: "   "
"""

sentence = input("Enter sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    words = sentence.split()
    if len(words) == 0:
        print("Error: invalid input")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]

        shortest_word = words[0]
        longest_word = words[0]

        for word in words:
            if len(word) < len(shortest_word):
                shortest_word = word
            if len(word) > len(longest_word):
                longest_word = word

        print(f"Word count: {word_count}")
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")


# ==================================================
# Problem 5: Password Strength Classifier
# ==================================================
"""
Description:
Classifies password strength as weak, medium, or strong.

Rules:
- Weak: length < 8
- Medium: length >= 8 and contains letters and digits
- Strong: length >= 8 and contains uppercase,
  lowercase, digit, and symbol

Inputs:
- password_input (string)

Outputs:
- Password strength

Validation:
- Not empty

Test cases:
1) Normal: "Abc123!"
2) Edge case: "abcdefgh"
3) Error: ""
"""

password_input = input("Enter password: ").strip()

if password_input == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    if len(password_input) < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    elif (has_upper or has_lower) and has_digit:
        strength = "medium"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")


# ==================================================
# Problem 6: Product Label Formatter
# ==================================================
"""
Description:
Formats a product label to exactly 30 characters.

Inputs:
- product_name (string)
- price_value (string or number)

Outputs:
- Label (exactly 30 characters)

Validation:
- product_name not empty
- price_value must be positive number

Test cases:
1) Normal: ("Laptop", 999.99)
2) Edge case: ("Pen", 1)
3) Error: ("", -5)
"""

product_name = input("Enter product name: ").strip()
price_value = input("Enter price: ").strip()

if product_name == "":
    print("Error: invalid input")
else:
    try:
        price_number = float(price_value)
        if price_number <= 0:
            print("Error: invalid input")
        else:
            base_label = f"Product: {product_name} | Price: ${price_number}"
            if len(base_label) > 30:
                label = base_label[:30]
            else:
                label = base_label + " " * (30 - len(base_label))

            print(f'Label: "{label}"')
    except:
        print("Error: invalid input")
