# Question 1
result=list(filter(lambda x: x % 7 == 0 and x % 5 != 0, range(1, 100)))
print(result)

# Question 2
li=[2, 3, 4, 5, 6]


def multi(l):
    return l * l


result = list(map(multi,li))
print(result)

# Question_3

data = input("Enter the string:")

result = [x.upper() for x in data]
print(result)


# Question_4
Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']
res = dict(zip(Student, capital))
print(res)

# Question_5
# Learn More about Yield, next and Generators
"""
Yield : yield is a keyword in Python that is used to return from a function without destroying the states of its 
local variable and when the function is called, the execution starts from the last yield statement.
Any function that contains a yield keyword is termed as generator. Hence, yield is what makes a generator. 
yield keyword in Python is less known off but has a greater utility which one can think of.

Advantages of yield
1.Since it stores the local variable states, hence overhead of memory allocation is controlled.
2.Since the old state is retained, flow doesn’t start from the beginnning and hence saves time.
Disadvantages of yield:
1.Sometimes, the use of yield becomes erroneous is calling of function is not handled properly.
2.The time and memory optimization has a cost of complexity of code and hence sometimes hard to understand logic behind it.
    
Next: Python file method next() is used when a file is used as an iterator, typically in a loop, the next() method is called repeatedly.
This method returns the next input line, or raises Stopiteration when EOF is hit.
Combining next() method with other file methods like readline() does not work right. However, usingseek() to reposition 
the file to an absolute position will
flush the read-ahead buffer.

Generators: These are used to create iterators, but with a different approach. Generators are simple functions which 
return an iterable set of items,in a special way. When an iteration over a set of item starts using the for statement, 
the generator is run.

"""


# Question_6

def sampleGenerator(s):
    yield s[::-1]


s = input("Enter the string:")
res = sampleGenerator(s)
print(next(res))


# Question_7

# Example of decorator
def smart_fun(func):
    def inner_fun(a, b):
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner_fun


@smart_fun
def divide(a, b):
    print(a / b)


res=divide(7, 5)

print(res)

# Question_8
'''
What is the Front_End Technologies?
    It is a set of technologies that are used in developing the user interface of web if applications and webpages:
With the help of front-end technologies, developers create the design, structure, animation, and everything
that you see on the screen while opening up a website, web application, or mobile app.
The prime goal of front-end development tools and technologies is to help mobile and web developers increase
their efficiency and make the development process quicker, simpler, and better.

Benefits of Front-End Technologies for Web and Mobile Development?

Reusable templates and elements
Provide task automation
Offer code optimization and debugging
Enhances developers’ productivity
Ease the development process for developers

Top Front-End Technologies :

1. Vue.js : Facebook, Netflix, Adobe, etc...
2. Npm : eBay, Coinbase, Nvida, etc...
3. Vue.js : Behance, Gitlab, Laravel Spark , etc...
4.Bootstrap : Spotify, Twitter, Intel, Wlamart, etc ...
5.  Angular: Nike, Google, Weather, Autodesk , etc... '''

