# Question1:

num=int(input("Enter the value:"))

# First
if num % 3 == 0 and num % 5 == 0:
    print("Consultadd Pyhton Training")

# Second
elif num % 3 == 0:
    print("Consultadd")

# Three
elif num % 5 == 0:
    print("c")

else:
    print("You Enter wrong number")

# Question:2 Options for the user
print("user option 1: Additon")
print("user option 2: Subtraction")
print("user option 3: Multiplication")
print("user option 4: Division")
print("User option 5: Average")

# Ask the user to choose the option
choice=int(input("Choose the number in between(1/2/3/4/5) :"))
if 1 <= choice <= 5:
    # Ask the user to enter two numbers
    print("Enter two numbers")
    x=int(input("Enter the First value :"))
    y=int(input("Enter the Second value :"))
    if choice == 1:
        result=x + y
        print(x, '+', y, '=', result)
    elif choice == 2:
        result=x - y
        print(x, '-', y, '=', result)
    elif choice == 3:
        result=x / y
        print(x, '/', y, '=', result)
    elif choice == 4:
        result=x * y
        print(x, '*', y, '=', result)
    elif choice == 5:
        print("Enter two more values :")
        first1=int(input("Enter the value :"))
        first2=int(input("Enter the value :"))
        average=(x + y + first1 + first2) / 4
        result=average
        print(result)
    if result < 0:
        print('Zsa')

else:
    print("Wrong input value")

# Question 3 flowchart:

age=int(input("Please enter your age :"))

if age >= 11:
    print("You are eligible to see the Football match.")
    if age <= 20 or age >= 60:
        print("Ticket price is $12")
    else:
        print("Ticket price is $20")
else:
    print("You are not eligible to by a ticket")

# Question 4 find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')

# Question 5
while True:
    num=int(input("Enter the value : "))
    if num < 0:
        print("It's over")
        break
    if num > 0:
        print("It's good")
        continue

# Question 6

# first
x=123
for i in x:
    print(i)

# OUTPUT : TypeError: 'int' object is not iterable

# Second
i=0

while i < 5:
    print(i)
    i+=1
    if i == 3:
        break
else:
    print("error")

# OUTPUT : 0 1 2

# Third
count=0
while True:
    print(count)
    count+=1
    if count >= 5:
        break
# OUTPUT : 0 1 2 3 4

# Question 7:Write a program that prints all the numbers from 0 to 6 except 3 and 6.

for i in range(0, 6):
    if i == 3 or i == 6:
        continue
    print(i, end=' ')

# Question 8:
data=input("Please Enter a string:")
num=0
str=0
for i in data:
    if i.isdigit():
        num=num + 1
    elif i.isalpha():
        str=str + 1
    else:
        pass
print("The number of digits is:", num)
print("The number of letters is:", str)

# Question 9: If the correct number is guessed the program stops, otherwise it continues forever.

guess_number=int(input("Try to guess the lucky number:"))
lucky_number=10
while True:
    if guess_number != lucky_number:
        print("Your guess is wrong")
        guess_number=int(input("Try again :"))
    elif guess_number == lucky_number:
        print("Your guess is correct", lucky_number)
        break

# Question 10:

lucky_number=10
guess_number=int(input("Try to guess the lucky number:"))
while guess_number != lucky_number:
    print("You guess wrong number")
    answer=input("You would like to continue please select your option yes/no:")
    if answer == 'no':
        break
    elif answer == 'yes':
        guess_number=int(input("guess again :"))
if guess_number == lucky_number:
    print("Your guess is correct", guess_number)

# Question 11:

lucky_number=25
counter=1

while counter <= 5:
    guess_number=int(input("Try to guess the lucky number :"))
    counter=counter + 1
    if guess_number == lucky_number:
        print("Good Guess")
    else:
        print("Try Again")
print("Game Over!")

# Question 12:
lucky_number = 25
counter = 1
while counter <= 5:
    guess_number=int(input("Guess the number : "))
    counter = counter + 1
    if guess_number == lucky_number:
        print("Good Guess")
        break
    else:
        print("Try Again")
if guess_number != lucky_number:
    print("Sorry but that wasn't very successful")


