'''Write a program in Python to break and continue if the following cases occur:
If a user enters a negative number just break the loop and print “It’s Over”
If a user enters a positive number just continue in the loop and print “Good Going”'''

while True:
    num = int(input("Enter the value : "))
    if num < 0:
        print("It's over")
        break
    if num > 0:
        print("It's good")
        continue

