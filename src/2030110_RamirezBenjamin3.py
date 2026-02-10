# --------------------------------------------------
# Problem 1: Shopping list basics (list operations)
# --------------------------------------------------
# Description:
# Works with a shopping list represented as a list.
# Allows adding items, counting elements, and searching
# for a specific product using normalized strings.
#
# Inputs:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)
#
# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" True|False
#
# Validations:
# - initial_items_text not empty after strip()
# - new_item and search_item not empty
#
# Test cases:
# 1) Normal: "apple:2, banana:5", add "orange", search "apple"
# 2) Edge: single item list
# 3) Error: empty initial string

initial_items_text = input("Enter initial items: ").strip()

if initial_items_text == "":
    print("Error: invalid input")
else:
    raw_items = initial_items_text.split(",")
    items_list = []

    for item in raw_items:
        clean_item = item.strip().lower()
        if clean_item != "":
            items_list.append(clean_item)

    new_item = input("Enter new item: ").strip().lower()
    search_item = input("Enter item to search: ").strip().lower()

    if new_item == "" or search_item == "":
        print("Error: invalid input")
    else:
        items_list.append(new_item)
        print("Items list:", items_list)
        print("Total items:", len(items_list))
        print("Found item:", search_item in items_list)


# --------------------------------------------------
# Problem 2: Points and distances with tuples
# --------------------------------------------------
# Description:
# Uses tuples to represent two points in a 2D plane,
# calculates the Euclidean distance and the midpoint.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)
#
# Validations:
# - Inputs convertible to float
#
# Test cases:
# 1) Normal: (0,0) and (3,4)
# 2) Edge: same points
# 3) Error: non-numeric input

try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 3: Product catalog with dictionary
# --------------------------------------------------
# Description:
# Manages a product catalog using a dictionary
# and calculates total cost for a purchase.
#
# Inputs:
# - product_name (string)
# - quantity (int)
#
# Outputs:
# - Unit price, quantity, total
# - Or error if product not found
#
# Validations:
# - product_name not empty
# - quantity > 0
#
# Test cases:
# 1) Normal: apple, 3
# 2) Edge: quantity = 1
# 3) Error: product not found

product_prices = {
    "apple": 10.0,
    "banana": 5.5,
    "orange": 7.0
}

product_name = input("Enter product name: ").strip().lower()

try:
    quantity = int(input("Enter quantity: "))

    if product_name == "" or quantity <= 0:
        print("Error: invalid input")
    elif product_name in product_prices:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity

        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total_price)
    else:
        print("Error: product not found")
except ValueError:
    print("Error: invalid input")


# --------------------------------------------------
# Problem 4: Student grades with dict and list
# --------------------------------------------------
# Description:
# Stores student grades in a dictionary of lists,
# calculates average and pass/fail status.
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - Grades, average, passed
#
# Validations:
# - student exists
# - grades list not empty
#
# Test cases:
# 1) Normal: existing student
# 2) Edge: student with one grade
# 3) Error: student not found

grades = {
    "alice": [85.0, 90.0, 78.0],
    "bob": [60.0, 70.0, 65.0],
    "carol": [95.0]
}

student_name = input("Enter student name: ").strip().lower()

if student_name == "":
    print("Error: invalid input")
elif student_name in grades:
    grades_list = grades[student_name]

    if len(grades_list) == 0:
        print("Error: no grades")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0

        print("Grades:", grades_list)
        print("Average:", average)
        print("Passed:", is_passed)
else:
    print("Error: student not found")


# --------------------------------------------------
# Problem 5: Word frequency counter (list + dict)
# --------------------------------------------------
# Description:
# Counts word frequency in a sentence using a list
# and a dictionary.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Words list
# - Frequencies
# - Most common word
#
# Validations:
# - sentence not empty
#
# Test cases:
# 1) Normal: "Hello world hello"
# 2) Edge: one word
# 3) Error: empty sentence

sentence = input("Enter sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    clean_sentence = sentence.lower()
    for ch in ".,!?;:":
        clean_sentence = clean_sentence.replace(ch, "")

    words_list = clean_sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        most_common_word = ""
        highest_count = 0

        for word, count in freq_dict.items():
            if count > highest_count:
                highest_count = count
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


# --------------------------------------------------
# Problem 6: Simple address book (dictionary CRUD)
# --------------------------------------------------
# Description:
# Implements a simple address book using a dictionary
# with basic CRUD operations.
#
# Inputs:
# - action_text (ADD, SEARCH, DELETE)
# - name, phone (depending on action)
#
# Outputs:
# - Result of the operation
#
# Validations:
# - Valid action
# - name and phone not empty
#
# Test cases:
# 1) Normal: ADD then SEARCH
# 2) Edge: update existing contact
# 3) Error: delete non-existing contact

contacts = {
    "alice": "1234567890",
    "bob": "5551234567"
}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid input")
else:
    name = input("Enter contact name: ").strip().lower()

    if name == "":
        print("Error: invalid input")
    else:
        if action_text == "ADD":
            phone = input("Enter phone: ").strip()
            if phone == "":
                print("Error: invalid input")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")
