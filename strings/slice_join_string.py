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