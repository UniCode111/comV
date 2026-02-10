numbers = [7,3,9,1,4,2]
sorted=[]

for i in numbers:
	a=1
	if numbers[a]<numbers[a-1]:
		sorted[a]=numbers[a-1]
	a=a+1
	print(i)
print(sorted)
