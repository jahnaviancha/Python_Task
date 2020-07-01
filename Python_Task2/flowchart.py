# program in Python to implement the given flowchart

age = int(input("Please enter your age :"))

if age >= 11:
    print("You are eligible to see the Football match.")
    if age <= 20 or age >= 60:
        print("Ticket price is $12")
    else:
        print("Ticket price is $20")
else:
    print("You are not eligible to by a ticket")
