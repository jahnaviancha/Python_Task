# first
x = '123'
for i in x:
    print(i)

#OUTPUT : without quots getting error     for i in x:
#TypeError: 'int' object is not iterable

#OUTPUT: 1 2 3



#Second
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("error")

# OUTPUT : 0 1 2

#Third
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# OUTPUT : 0 1 2 3 4