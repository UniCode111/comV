def summarize_numbers(numbers_list):
	return {
		"min": min(numbers_list),
		"max": max(numbers_list),
		"average": sum(numbers_list)/len(numbers_list)
	}

numbers_text = input("Numbers (coma separated): ").strip()

parts = numbers_text.split(",")
numbers=[]
valid = True

for part in parts:
#	part = part.strip()
	try:
		numbers.append(float(part))
	except ValueError:
		valid = False
if valid and len(numbers) > 0:
	result =summarize_numbers(numbers)
	print("Min:", result["min"])
	print("Max:", result["max"])
	print("Average:", result["average"])
else:
	print("Error: Invalid input")
print(parts)
print(numbers)
