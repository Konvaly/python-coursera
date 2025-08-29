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