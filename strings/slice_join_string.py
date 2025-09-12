## SLICE
# Example 1

string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”

# Example 2
# Prints “Earthlings” again
print(string1[-10:])

# Example 3
# If your index is beyond the end of the string, Python returns an empty string.
# Prints “” 
print(string1[55:])

# Example 4
# An optional way to slice an index is by the stride argument, 
# indicated by using a double colon. 
# This allows you to skip over the corresponding number of characters in your index, 
# or if you’re using a negative stride, the string prints backwards.
# Prints “Getns atlns”
print(string1[0::2])

# Prints “sgnilhtraE ,sgniteerG”
print(string1[::-1])

## JOIN
# Example 5
greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"

# You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!")  # Prints "Hello, Alice!"

# Example 6
# How to combine slicing and joining strings
# Now you know how to slice strings and join strings. 
# Now, let’s put the two operations together by taking an unformatted phone number, 2025551212, 
# and return it as a properly formatted U.S. number. In this example, 
# we’ll use phonenum to refer to the unformatted phone number. 
# You can define a function format_phone() to perform the whole operation. Here is a breakdown of the steps.

# This slices the first three numbers from the string:
phonenum = '2025551212'

# The first 3 digits are the area code:
area_code = "(" + phonenum[:3] + ")"

# This slices the numbers 4–6 from the string.
# The next 3 digits are called the “exchange”:
exchange = phonenum[3:6]

# Negative indexing counts backwards from the end of the numbers, 
# slicing the last four numbers in the string.
# The last 4 digits are the line number:
line = phonenum[-4:]

# And you can put them all together:
# Put the pieces back together into a nicely formatted string:
area_code + " " + exchange + "-" + line

# When all the steps are assembled into a function:
def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

format_phone('2025551212')  # Returns "(202) 555-1212"