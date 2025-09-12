# Example 1

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)


# Example 2

message = "This is a new message"
print(message)
message = "And another one"
print(message)

# Example 3

pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dog"))
print(pets.index("s"))

# Example 4
pets="Cats & Dogs"
print("Dragons" in pets)
print("Cats" in pets)