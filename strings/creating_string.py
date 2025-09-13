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

# Example 5
def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return print(new_email)
  return print(email)

replace_domain("asd@fig.com", "fig.com", "gmail.com")  # Returns "


#Example

