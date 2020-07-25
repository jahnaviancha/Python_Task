# Question_1:
# Reverse a string.


def rev_str(data):
    return data[::-1]


# Taking string from user  “1234abcd”
sample_text=rev_str(input("Enter the string"))

print(sample_text)


# Output : dcba4321


# Question_2:
# checking upper and lower letters
def check_letter(s):
    upperCase_letters=0
    lowerCase_letters=0
    for letter in s:
        if letter.islower():
            lowerCase_letters+=1
        elif letter.isupper():
            upperCase_letters+=1
    print("Number of Upper_Case letters = ", upperCase_letters)
    print("Number of Upper_Case letters = ", lowerCase_letters)


check_letter(input("Enter the string :"))


# Question_3
# a list and returns a new list with unique elements of the first list.
def unique(li):
    new_list=[]
    for x in li:
        if x not in new_list:
            new_list.append(x)
    return new_list


y=unique(input("Enter the list :"))

print(y)


# Question_4
# hyphen-separated sequence of words


def hyphen_separated(user_data):
    words=[word for word in user_data.split('-')]
    print("Sorting the given words:")
    words.sort()
    sequence='-'.join(words)
    return sequence


word=input("Enter a hyphen separated sequence of words:")

word_order=hyphen_separated(word)
print(word_order)


# Question_5

# accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

def sequence_upper():
    while True:
        lines=[]
        li=input('Enter a sentence please:')
        if li:
            lines.append(li.upper())
        else:
            break
        for li in lines:
            return li


res=sequence_upper()
print(res)


# Question_6

# Two integral numbers in string form and compute their sum and print it in console.

def two_integers(a, b):
    str=int(a) + int(b)
    return str


sum_two=two_integers(5, 6)
print("The sum is:", sum_two)


# Question_7

def compare_strings_len(s1, s2):
    if len(s1) > len(s2):
        print('String 1 is longer: ', s1)
    elif len(s1) < len(s2):
        print('String 2 is longer: ', s2)
    elif len(s1) == len(s2):
        print(s1, end="\n")
        print(s1, end="\n")
    else:
        pass


compare_strings_len(s1=input("Enter the first String :"), s2=input("Enter the second string:"))


# Question_8
def square_values():
    li=list()
    for i in range(1, 21):
        li.append(i ** 2)
        tup=tuple(li)
    return tup


square_tup=square_values()
print(square_tup)


# Question_9
def showNumbers(limit):
    for i in range(0, limit + 1):
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")


showNumbers(3)


# Question_10

# Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

def check_filter():
    L=list(filter((lambda x: x % 2 == 0), range(1, 21)))
    return L


new_li=check_filter()
print(new_li)

# Question_11

li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sqr_num=list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, li)))

print(sqr_num)

# Question_12
# Write a function to compute 5/0 and use try/except to catch the exceptions

try:
    def try_fun():
        x=5 / 0
        return x

        res=try_fun()
        print(res)
except:
    print("Error dividing by Zero")

# Question_13
from functools import reduce

li=[[1, 2, 3], [4, 5], [6, 7, 8]]
new_li=reduce(lambda x, y: x + y, li)
print(new_li)
# Convert into string
new_str=""
for i in new_li:
    new_str+=str(i)
print(new_str)


# Question_14

def foo():
    try:
        return 1
    finally:
        return 2


k=foo()
print(k)  # Output = 2


def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')


a()  # Output: NameError: name 'f' is not defined
