# Task-1
# Fill in the blanks to print the even numbers from 2 to 12.

number = 2 # Initialize the variable 
while number <= 12: # Complete the while loop condition
    print(number, end=" ")
    number += 2 # Increment the variable

# Should print 2 4 6 8 10 12 


# Task-2
# Fill in the blanks to complete the “factorial” function. This function will accept 
# an integer variable “n” through the function parameters and produce the factorials 
# of this number (by multiplying this value by every number less 
# than the original number [n*(n-1)], excluding 0).  To do this, the function should:

# - accept an integer variable “n” through the function parameters;

# - initialize a variable “result” to the value of the “n” variable;

# - iterate over the values of “n” using a while loop until “n” is equal to 0;

# - starting at n-1, multiply the result by the current “n” value;

# - decrement “n” by -1.

# -  For example, factorial 3 would return the value of 3*2*1, which would be 6.

def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1 # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1

# Task-3
# Fill in the blanks to complete the “rows_asterisks” function. This function should print rows of asterisks (*), where the number of rows is equal to the “rows” variable. The number of asterisks per row should correspond to the row number (row 1 should have 1 asterisk, row 2 should have 2 asterisks, etc.). Complete the code so that “row_asterisks(5)” will print:

# *
# * *
# * * *
# * * * *
# * * * * *

def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(6): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above


# Task-4
# Fill in the blanks to complete the “divisible” function. This function should count the number 
# of values from 0 to the “max” parameter minus 1 that are evenly divisible by the “divisor” parameter. 
# This means they do not have a remainder when divided by the divisor. Complete the code so that 
# a function call like “divisible(100,10)” will return the number “10”.

def divisible(max, divisor):
    count = 0 # Initialize an incremental variable
    for x in range(max): # Complete the for loop
        if x % divisor == 0:
            count += 1 # Increment the appropriate variable
    return count

print(divisible(100, 10)) # Should be 10
print(divisible(10, 3)) # Should be 4
print(divisible(144, 17)) # Should be 9


# Task-5
# Fill in the blanks to complete the “all_numbers” function. This function should return 
# a space-separated string of all numbers, from the starting   “minimum” variable  up to 
# and including the “maximum” variable that's passed into the function. Complete the for loop 
# so that a function call like “all_numbers(3,6)” will return the numbers “3 4 5 6”.  

def all_numbers(minimum, maximum):

    return_string = ""  # Initializes variable as a string

    # Loop через всі числа від minimum до maximum включно
    for x in range(minimum, maximum+1):
        return_string += str(x) + " "  # додаємо число і пробіл

    # Видаляємо зайвий пробіл у кінці
    return return_string.strip()


print(all_numbers(2,6))   # 2 3 4 5 6
print(all_numbers(3,10))  # 3 4 5 6 7 8 9 10
print(all_numbers(-1,1))  # -1 0 1
print(all_numbers(0,5))   # 0 1 2 3 4 5
print(all_numbers(0,0))   # 0

# Task-6
# Fill in the blanks to print the numbers from 15 to 5, counting down by fives.

number = 15 # Initialize the variable
while number >= 5: # Complete the while loop condition
    print(number, end=" ")
    number -= 5 # Decrement the variable

# Should print 15 10 5 


# Task-7
# Fill in the blanks to complete the “factorial” function. This function will accept 
# an integer variable “n” through the function parameters and produce the factorials 
# of this number (by multiplying this value by every number less than the original 
# number [n*(n-1)], excluding 0).  To do this, the function should:
#
# - accept an integer variable “n” through the function parameters;
#
# - initialize a variable “result” to the value of the “n” variable;
#
# - iterate over the values of “n” using a while loop until “n” is equal to 0;
#
# - starting at n-1, multiply the result by the current “n” value;
#
# - decrement “n” by -1.
#
# -  For example, factorial 3 would return the value of 3*2*1, which would be 6.

# Solution-1 with loop
def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1 # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1

# Solution-2 with resursion
def factorial_recursion(n):
     # Base case: 0! and 1! are both 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursion(n - 1)

# Examples
print(factorial_recursion(3))  # 6
print(factorial_recursion(5))  # 120
print(factorial_recursion(0))  # 1


# Task-8
##
# Fill in the blanks to complete the “counter” function. This function should count down
#  from the “start” to “stop” variables when “start” is bigger than “stop”. 
# Otherwise, it should count up from “start” to “stop”. Complete the code so that a function call
#  like “counter(3, 1)” will return “Counting down: 3, 2, 1” and “counter(2, 5)” 
# will return “Counting up: 2, 3, 4, 5”.

def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop: # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            start -= 1 # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while stop >= start: # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            start += 1 # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

# Task-9
# Fill in the blanks to complete the “rows_asterisks” function. This function should print
#  rows of asterisks (*), where the number of rows is equal to the “rows” variable. 
# The number of asterisks per row should correspond to the row number (row 1 should have 1 asterisk, 
# row 2 should have 2 asterisks, etc.). Complete the code so that “row_asterisks(5)” will print:
#
# *
#
# * *
#
# * * *
#
# * * * *
 
# * * * * *

def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(1,rows+1): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above

# Task-10
# Fill in the blanks to complete the “odd_numbers” function. 
# This function should return a space-separated string of all odd positive numbers, 
# up to and including the “maximum” variable that's passed into the function. 
# Complete the for loop so that a function call like “odd_numbers(6)” 
# will return the numbers “1 3 5”.

def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for x in range(maximum+1): 

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        if x % 2 != 0:
            return_string += str(x) + " "  

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed

