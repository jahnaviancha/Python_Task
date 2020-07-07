# Question 1
x_list=[1, 'janu', (1 + 2j), 0.25, 36, 2.5, 'Consultadd', 25, (-4 + 8j), 45, 4.4]

print(x_list)

# Question 2
x=[1, 2, 3, 4, 5]
# printing entire list
print(x[:])
# left:right index , i need (3,4)
print(x[2:-1])
# :right index, i need (1,2,3)
print(x[:3])
# :left index i need (3,4,5)
print(x[2:])
# negative index
print(x[-2:])  # (4,5)
print(x[:-2])  # (1,2,3)

# Question 3
e_list=[2, 3, 4]
product=1
for i in e_list:
    product=product * i
print(product)  # product of the list
print(sum(e_list))  # sum of the list

# Question 4
x=[24, 35, 78, 89, 90, 15, 9]
print("largest num of my list:", max(x))
print("smallest num of my list :", min(x))

# Question 5
# list contains even and odd

my_list=[2, 7, 15, 16, 25, 18, 34, 42, 29]

print(my_list)

# find even numbers and remove form list by using remove fun
for i in my_list:
    if i % 2 == 0:
        my_list.remove(i)
print("list after removing the even numbers:", my_list)

# Question 6
my_list=[]
for i in range(1, 31):  # [1,2,3,4,5,..25,26,27,28,29]
    my_list.append(i ** 2)
print(my_list[:5])  # [:right index]
print(my_list[25:])  # [left index:]

# Question 7
sample_list=[[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]]

# List Concatenating and removing the last element in first list
print(sample_list[0][1] + sample_list[1])

# Question 8
a={1: 10, 2: 20}
b={3: 30, 4: 40}
c=a, b
result={}
for x in c:
    result.update(x)
print(result)

# Question 9
n = 5
d = {}
for x in range(1, n + 1):
    d[x] = x * x

# Question 10
values = input("Enter comma-separated numbers : ")
my_list = values.split(",")
my_tuple = tuple(my_list)
print('List : ', my_list)
print('Tuple : ', my_tuple)
