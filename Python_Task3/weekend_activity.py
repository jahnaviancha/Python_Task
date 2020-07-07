# Question 3
# Create a list of given structure and run
x=[100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]

# Access list [1, 2, 3, 4]
print(x[5][:4])

# Access list [600,  700]
print(x[6:8])

# Access list [100, 300, 500, 600, 800]
print(x[::2])

# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[::-1])

# Access list [10]
print(x[5][5][0])

# Access list [ ]
print(x[:])

# Question 4
x=list(range(1, 1001))
print(x)
print(type(x))  # <class 'list'>

y=list(xrange(1, 1001))
print(y)
print(type(y))  # <type 'list'>
# python3x not supporting xrange() but python2x will support xrange() and the difference is that range()
# returns a Python list object and xrange returns an xrange object

# Question 5
# How Tuple is beneficial as compared to the list?
'''Tuples are fixed size in nature where as lists are dynamic.
List has mutable nature, where as tuple has immutable nature'''

# Question 6
i=list(range(1, 1000))
for x in i:
    if x % 3 and x % 2 == 0:
        print(x)

# Question 7
x=input("Enter the string :")
vowels=['a', 'e', 'i', 'o', 'u']
for char in x:
    if char in vowels:
        print(char, end="")

# Question 8
my_str="hello my name is janu"
result=""
for i in range(len(my_str)):
    if i % 2 == 0:
        result=result + my_str[i]
print(result)

# Question 9
arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
n=len(arr)
sum1=8
for i in range(0, n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == sum1:
            print(arr[i], arr[j])
# Question 10
Even_list=[]
Odd_list=[]

while True:
    if len(Even_list) == 5 and len(Odd_list) == 5:
        print("Sum of the Even numbers:", sum(Even_list))
        print("Max of Even Numbers ", max(Even_list))
        print("Sum of the Odd numbers:", sum(Odd_list))
        print("Max of Even Numbers ", max(Odd_list))
        break
    n=int(input("Enter the value in the range(1,50)"))
    if n % 2 == 0:
        if len(Even_list) < 5:
            Even_list.append(n)
    else:
        if len(Odd_list) < 5:
            Odd_list.append(n)

print("Element in Even List is : ", Even_list)
print("Element in Odd List is : ", Odd_list)

# Question 11
word='12abcbacbaba344ab'
print("Number of a = ", word.count('a'))
print("Number of b = ", word.count('b'))
print("Number of c = ", word.count('c'))

# Question 12
tup =(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
li = list()
for i in tup:
    if i % 2 == 0:
        li.append(i)
tup2 = tuple(li)
print(tup2)

# Class activity
letter = "consultaddinc python training"
demo = {}
for i in letter:
    if i in demo:
        demo[i] += 1
    elif i != ' ':
        demo[i] = 1
print(demo)
