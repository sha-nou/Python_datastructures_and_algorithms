import operator
import math
def greet():
    print('hello')

greet()

# function to perform addition

def add(a,b):
    result = operator.iadd(a,b)
    print(result)

add(8,3)

# the + sign used for concatenation
x =[1,2,3]
y=[4,5,6]
z= x+y
print(z)


# exponentiation
c,d = 7,5
r=math.pow(c,d)
print(r)

# function to perform subtraction

def subtract(a,b):
    if(a<b):
        result =operator.sub(a,b)
        print(result)
    else:
        result = operator.sub(b,a)
subtract(8,3)
