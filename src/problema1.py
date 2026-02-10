def calculate_area(width, heigth):
	return width*heigth
def calculate_perimeter(width,heigth):
	return 2*(width+heigth)
width=float(input())
heigth=float(input())
if (width>0) and (heigth>0):
	
	a=calculate_area(width,heigth)
	p=calculate_perimeter(width,heigth)
	print(f"Area= ",a)
	print(f"Perimeter= ", p)
else:
	print("Error: invalid input")

