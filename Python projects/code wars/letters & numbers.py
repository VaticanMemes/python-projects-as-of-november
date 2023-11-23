def zero(process = None, num = None):
    brute_force_solution = 0
    if process == None or num == None:
        return 0
    elif process == "plus":
        return brute_force_solution + int(num)
    elif process == "minus":
        return brute_force_solution - int(num)
    elif process == "times":
        return brute_force_solution * int(num)
    elif process == "divided_by":
        return int(brute_force_solution / int(num))
def one(process = None, num = None):
    brute_force_solution = 1
    if process == None or int(num) == None:
        return 1
    elif process == "plus":
        return brute_force_solution + int(num)
    elif process == "minus":
        return brute_force_solution - int(num)
    elif process == "times":
        return brute_force_solution * int(num)
    elif process == "divided_by":
        return int(brute_force_solution / int(num))
def two(process = None, num = None):
    brute_force_solution = 2
    if process == None or num == None:
        return 2
    elif process == "plus":
        return brute_force_solution + int(num)
    elif process == "minus":
        return brute_force_solution - int(num)
    elif process == "times":
        return brute_force_solution * int(num)
    elif process == "divided_by":
        return int(brute_force_solution / int(num))
def three(process = None, num = None):
    brute_force_solution = 3
    if process == None or num == None:
        return 3
    elif process == "plus":
        return brute_force_solution + int(num)
    elif process == "minus":
        return brute_force_solution - int(num)
    elif process == "times":
        return brute_force_solution * int(num)
    elif process == "divided_by":
        return int(brute_force_solution / int(num))
def four(process = None, num = None):
    brute_force_solution = 4
    if process == None or num == None:
        return 4
    elif process == "plus":
        return brute_force_solution + int(num)
    elif process == "minus":
        return brute_force_solution - int(num)
    elif process == "times":
        return brute_force_solution * int(num)
    elif process == "divided_by":
        return int(brute_force_solution / int(num))
def five(process = None, num = None):
    brute_force_solution = 5
    if process == None or num == None:
        return 5
    elif process == "plus":
        return brute_force_solution + int(num)
    elif process == "minus":
        return brute_force_solution - int(num)
    elif process == "times":
        return brute_force_solution * int(num)
    elif process == "divided_by":
        return int(brute_force_solution / int(num))
def six(process = None, num = None):
    brute_force_solution = 6
    if process == None or num == None:
        return 6
    elif process == "plus":
        return brute_force_solution + int(num)
    elif process == "minus":
        return brute_force_solution - int(num)
    elif process == "times":
        return brute_force_solution * int(num)
    elif process == "divided_by":
        return int(brute_force_solution / int(num))
def seven(process = None, num = None):
    brute_force_solution = 7
    if process == None or num == None:
        return 0
    elif process == "plus":
        return brute_force_solution + int(num)
    elif process == "minus":
        return brute_force_solution - int(num)
    elif process == "times":
        return brute_force_solution * int(num)
    elif process == "divided_by":
        return int(brute_force_solution / int(num))
def eight(process = None, num = None):
    brute_force_solution = 8
    if process == None or num == None:
        return 8
    elif process == "plus":
        return brute_force_solution + int(num)
    elif process == "minus":
        return brute_force_solution - int(num)
    elif process == "times":
        return brute_force_solution * int(num)
    elif process == "divided_by":
        return int(brute_force_solution / int(num))
def nine(process = None, num = None):
    brute_force_solution = 9
    if process == None or num == None:
        return 9
    elif process == "plus":
        return brute_force_solution + int(num)
    elif process == "minus":
        return brute_force_solution - int(num)
    elif process == "times":
        return brute_force_solution * int(num)
    elif process == "divided_by":
        return int(brute_force_solution / int(num))

def plus(num): 
    return "plus", num
def minus(num): 
    return "minus", num
def times(num): 
    return "times", num
def divided_by(num): 
    return "divided_by", num

print(f"seven(times(five())): {seven(times(five()))}")
print(f"seven('times', five()): {seven('times', five())}")
print(f"times(five()): {times(five())}")
print()
print(four(plus(nine())))
print(plus(nine()))
print(four('plus', 9))

# this solution is fucked