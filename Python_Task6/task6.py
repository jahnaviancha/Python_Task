# Question_1
# Write a program in Python to allow the error of syntax to go in exception.
try:
    print(x)
except:
    print("Hey please check again, I didn't see any value of 'x")

# Output: Syntax error

# Question_2
from sys import argv

NameOfProgram=argv

print("Name of the program is:  ", NameOfProgram)
NameOfFile=input("Please enter the file name :")
while True:
    try:
        fh=open(NameOfFile)
        content=fh.read()
        print(content)
        fh.close()
        break
    except:
        print("Hello the name of file is wrong please enter the name again: ")
        try_again=input("Do you want to open the file again(Y/N):")
        if try_again == 'Y':
            NameOfFile=input("Please enter the correct name :")
        else:
            break

# Question 3

value=input("Enter the numbers here: ")
while True:
    try:
        if len(value) < 5:
            print(value)
            break
        else:
            raise Exception
    except:
        print("Please length is too short/long !!! Please provide only four digits")
        value=input("Enter again: ")

# Question 4
print("Welcome to login page")
count=0
username=input("Enter your username : ")
password=input("Enter your Password : ")
while True:
    try:
        if username == "username" and password == 'password':
            print("Your Successfully login")
            break
        else:
            raise Exception
    except:
        if password != 'password':
            print("Retype the Password")
            password=input("Enter your Password")
            count+=1
            if count == 3:
                print("maximum number of attempt reached so Access denied")
                break


# Question_6
with open('doc.txt', 'r') as fh:
    for line in fh:
        if len(line) % 2 == 0:
            print(line.strip())
