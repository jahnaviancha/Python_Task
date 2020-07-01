num = int(input("Enter the value:"))

# If a number is divisible by both 3 and 5 its should print “Consultadd Python Training” as a string.
if num % 3 == 0 and num % 5 == 0:
    print("Consultadd Pyhton Training")

# If a number is divisible by 3 it should print “Consultadd” as a string
elif num % 3 == 0:
    print("Consultadd")

# If a number is divisible by 5 it should print “c” as a string
elif num % 5 == 0:
    print("c")

else:
    print("You Enter wrong number")

