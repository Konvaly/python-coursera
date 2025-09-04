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