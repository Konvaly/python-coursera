x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

##

# task-1
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)

##
# task-2
my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1


##
# task-3
x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10:
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1

##
# task-4
multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")


# This while loop prints the multiples of 5 between 1 and 50. The
# "multiplier" variable is initialized with the starting value of 1. 
# The "result" variable is initialized with the value of the 
# "multiplier" variable times 5. 

# The while loop specifies that the loop must iterate while it is True
# that the "result" is less than or equal to 50. Within the while loop, 
# the code tells the Python interpreter to print the value of the 
# "result" variable. Then, the "multiplier" is incremented by 1 and the
# "result" is assigned the new value of the "multiplier" times 5. 

# The end of the while loop is indicated by the indentation of the next 
# line of code moving one tab to the left. At this point, the Python
# interpreter automatically loops back to the beginning of the while
# loop to check the condition again with the new value of the "result"
# variable. When the while loop condition becomes False (meaning
# "result" is no longer less than or equal to 50), the interpreter exits
# the loop and reads the next line of code outside of the loop. In this 
# case, that next line tells the interpreter to print the string "Done". 

# Click the "Run" button to check the result of this while loop.    


##
# task-5
# This function counts the number of integer factors for a 
# "given_number" variable, passed through the function’s parameters.
# The "count" return value includes the "given_number" itself as a 
# factor (n*1). 
def count_factors(given_number):

    # To include the "given_number" variable as a "factor", initialize
    # the "factor" variable with the value 1 (if the "factor" variable
    # were to start at 2, the "given_number" itself would be excluded). 
    factor = 1
    count = 1

    # This "if" block will run if the "given_number" equals 0.
    if given_number == 0:
        # If True, the return value will be 0 factors. 
        return 0

    # The while loop will run while the "factor" is still less than
    # the "given_number" variable.
    while factor < given_number:
        # This "if" block checks if the "given_number" can be divided by
        # the "factor" variable without leaving a remainder. The modulo
        # operator % is used to test for a remainder.
        if given_number % factor == 0:
            # If True, then the "factor" variable is added to the count of
            # the "given_number"’s integer factors.
            count += 1
        # When exiting the if block, increment the "factor" variable by 1
        # to divide the "given_number" variable by a new "factor" value
        # inside the while loop.
        factor += 1

    # When the interpreter exits either the while loop or the top if
    # block, it will return the value of the "count" variable.
    return count


print(count_factors(0)) # Count value should be 0
print(count_factors(3)) # Should count 2 factors (1x3)
print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8, and 4x6). 