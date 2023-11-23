"""
def zero(operation = None): 
    if operation == None:
        return 0
    else:
        return operation(0)
def one(operation = None): 
    if operation == None:
        return 1
    else:
        return operation(1)
def two(operation = None): 
    if operation == None:
        return 2
    else:
        return operation(2)
def three(operation = None): 
    if operation == None:
        return 3
    else:
        return operation(3)
def four(operation = None): 
    if operation == None:
        return 4
    else:
        return operation(4)
def five(operation = None): 
    if operation == None:
        return 5
    else:
        return operation(5)
def six(operation = None): 
    if operation == None:
        return 6
    else:
        return int(operation(6))
def seven(operation = None): 
    if operation == None:
        return 7
    else:
        return operation(7)
def eight(operation = None): 
    if operation == None:
        return 8
    else:
        return operation(8)
def nine(operation = None): 
    if operation == None:
        return 9
    else:
        return operation(9)

def plus(number):
    return lambda y: y + number
def minus(number):
    return lambda y: y - number
def times(number):
    return lambda y: y * number
def divided_by(number):
    return lambda y: y / number
"""
def identity(a): return a

def zero(f=identity): return f(0)
def one(f=identity): return f(1)
def two(f=identity): return f(2)
def three(f=identity): return f(3)
def four(f=identity): return f(4)
def five(f=identity): return f(5)
def six(f=identity): return f(6)
def seven(f=identity): return f(7)
def eight(f=identity): return f(8)
def nine(f=identity): return f(9)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b

# Best practice: 
#1 you can choose a specific function by making it a variable
#2 you can use lambda functions in this way

print(plus(7))
print(seven(lambda a: a + 7))
test = lambda a: a**3
print(test(2))
def lol(a):
    return "lol"
tester = lol
print(tester(1))