# Options for the user
print("user option 1: Additon")
print("user option 2: Subtraction")
print("user option 3: Multiplication")
print("user option 4: Division")
print("User option 5: Average")

# Ask the user to choose the option
choice = int(input("Choose the number in between(1/2/3/4/5) :"))
if 1 <= choice <= 5:
    # Ask the user to enter two numbers
    print("Enter two numbers")
    x = int(input("Enter the First value :"))
    y = int(input("Enter the Second value :"))
    if choice == 1:
        result = x + y
        print(x, '+', y, '=', result)
    elif choice == 2:
        result = x - y
        print(x, '-', y, '=', result)
    elif choice == 3:
        result = x / y
        print(x, '/', y, '=', result)
    elif choice == 4:
        result = x * y
        print(x, '*', y, '=', result)
    elif choice == 5:
        print("Enter two more values :")
        first1 = int(input("Enter the value :"))
        first2 = int(input("Enter the value :"))
        average = (x+y+first1+first2) / 4
        result = average
        print(result)
    if result < 0:
        print('Zsa')

else:
    print("Wrong input value")