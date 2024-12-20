'''
function


'''
print(ord('z'))
print(abs(-98))
# variable scope: global and local
# parameters and argument
#user defined function
'''
def functionName(parameter):
    statement 1
    statement 2
    .
    statement 3

functionName(argument)
'''
'''
basis on argument function have 4 types:
    1. required/positional argument
    2. keyword argument
    3. default argument
    4. variable length argument
        *args = takes comma seperated, list, tuple -> return tuple
        **kwargs = takes key = value -> retrun dictionary

'''

print("Hello")
print()
print("BYE")
range(2,20)

def show():
    pass

print(show())

def bye():
    a = 100
    return "hello","world",a

a,b,c = bye()
print(a,b,c,end= "\n")
#print(res1)

def one(a,b,c=100):
    c = a + b
    return c

res = one(a=10,b=30,c=20)
print(res)

def average(a,*args):
    su = a
    for i in args:
        su += i
    av = su/(len(args) + 1)
    return av

res = average(5,2)
print(f"AVERAGE: {res}")
def one():
    li = []
    for i in range(1,100000):
        li.append(i)
    return li

def two():
    tu= []
    for i in range(1,100000):
        tu.append(i)

    return tuple(tu)

li = one()
tu = two()

import sys
print(sys.getsizeof(li))
print(sys.getsizeof(tu))


