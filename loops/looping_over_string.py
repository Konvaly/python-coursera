# Exanple 1

greeting = 'Hello'
for char in greeting:
	print(char)
	
# Example 2
#What if you don’t want the elements of the string but the position of the string instead? 
# You’re in luck because Python can work that magic too!

for i in range(len(greeting)):
	print(i)


# Example 3
greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1
	
# Example 4
greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index:index+1])
	index += 1
	
# Example 5
# List comprehensions are a concise way to create lists in Python. Let’s look at an example:
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)