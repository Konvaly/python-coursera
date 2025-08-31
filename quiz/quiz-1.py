# Example-1
# This function will accept an integer variable "end" and count by 10
# from 0 to the "end" value.
def count_by_10(end):
    # Initializeq the "count" variable as a string.
    count = ""

    # The range function parameters instruct Python to start the count  
    # at 0 and stop at the variable given as the upper end of the range. 
    # Since the value of the high end of a range is excluded by default,  
    # you can make Python include the "end" value by adding +1 to it. 
    # The third parameter tells Python to increment the count by 10.
    for number in range(0,end+1,10):

        # Although the variable "count" will hold a count of integers,  
        # this example will be converted to a string using "str(number)" 
        # in order to display the incremental count from 0 to the "end" 
        # value on the same line with a space " " separating each 
        # number.  
        count += str(number) + " "
        
    # The .strip() method will trim the final space " " from the end of 
    # the string "count"  
    return count.strip()

# Call the function with 1 integer parameter.
print(count_by_10(100))

# Should print 0 10 20 30 40 50 60 70 80 90 100

# Example-2
# This function uses a set of nested for loops with the range() function 
# to create a matrix of numbers. The upper range value in the range() 
# function should be included in the matrix. The matrix should consist 
# of a set of numbers that fill both rows and columns.
def matrix(initial_number, end_of_first_row):


    # It is an optional code style to assign the long variable names in the
    # function parameters to shorter variable names. 
    n1 = initial_number 
    n2 = end_of_first_row+1  # include the upper range value with +1

    # The first for loop will create the columns.
    for column in range(n1, n2):

        # The nested for loop will create the rows.
        for row in range(n1, n2):

            # To make the matrix of numbers easier to read, include a space
            # between each number in the rows until the loop reaches the 
            # end of the row. You can override the default behavior of the 
            # print() function (which inserts a new line character after 
            # the print command runs) by using the "end=" "" parameter 
            # inside the print() function.  
              print(column*row, end=" ")

        # The row ends when the upper range value is encountered within the 
        # nested for loop. The outer (column) for loop should insert a new line
        # to create the next row. Use the print() function new line default 
        # behavior with an empty print() function:
        print()


# Call the function with 2 integer parameters. 
matrix(1, 4)
# Should print:
# 1 2 3 4 
# 2 4 6 8 
# 3 6 9 12 
# 4 8 12 16 
