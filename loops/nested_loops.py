# Example-1

for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

# Example-2
teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)

# Example-3
# Example of nested for loops:
# This code demonstrates the outer and inner loop iterations of a pair 
# of nested for loops. Click "Run" to see the results. The outer loop
# will run twice for the range pointer positions [0, 1] in range(2).
# The inner loop will run 4 times for the range pointer positions 
# [0, 1, 2, 3] in range(3+1) or range(4) each time the outer loop runs.
# So, the inner loop will execute 8 times in total.

for x in range(2):
  print("This is the outer loop iteration number " + str(x))
  for y in range(3+1):
    print("Inner loop iteration number " + str(y))
print("Exit inner loop")

# Example-4
# for loop with nested if Statement
# The syntax of a for Loop with nested if Statement:
# This for loop iterates through the numbers 0 to 6. The if statement
# uses the modulo operator to test if the "x" variable is divisible by
# 2. If True, the if statement will print the value of "x" and exit
# back into the for loop for the next iteration of "x". Since no 
# incremental value is specified in the range() parameters, the default
# increment is +1. 

for x in range(7):
    if x % 2 == 0:
        print(x)

# The loop should print 0, 2, 4, 6

# As a list comprehension:
even_numbers = [x for x in range(7) if x % 2 == 0]
print(even_numbers)


# Example-5
# With a list comprehension, you could achieve the same result in a more concise way:
sequence = range(10)
new_list = [x for x in sequence if x % 2 == 0]

print(new_list)

# An example of a useful one-liner is:
print("*" * 8)

for n in range(10):
  print(n+n)

for x in range(0,101): 
    if x % 7 == 0
       print(x, end=" ")