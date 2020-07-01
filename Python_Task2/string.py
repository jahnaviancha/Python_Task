# Write a program that accepts a string as an input from the user and calculates the number of digits and letters.

data = input("Please Enter a string:")
num = 0
str = 0
for i in data:
    if i.isdigit():
        num = num + 1
    elif i.isalpha():
        str = str + 1
    else:
        pass
print("The number of digits is:", num)
print("The number of letters is:", str)
