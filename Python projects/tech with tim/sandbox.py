
import random
from math import sin, cos, tan, sqrt, ceil

def sin_squared_theta_plus_cos_squared_theta(theta):
    return (sin(theta)**2 + cos(theta)**2)

class pythag:

    def length(x1, x2):
        return abs(max(x1, x2) - min(x1, x2))

    def distance(coord1, coord2):
        return sqrt((pythag.length(coord1[0], coord2[0]))**2 + (pythag.length(coord1[1], coord2[1]))**2)

    # Write coord1 and coord2 as lists i.e. pythag.distance([x1, y1], [x2, y2]).

def rand_int_between_numbers(num1, num2):
    return random.randrange(min(num1, num2), max(num1, num2))

def dice_roll():
    return (random.randrange(0, 6) + random.randrange(0, 6))

class compound_interest:

    def compound_interest_formula(p, r, t):
        return round((p * ((1 + (r/100)) ** t)), 2)

    # Rate must be the actual %, not the decimal. So for 10% input 10, not 0.1.

    def comp_interest_main():
        yay_or_nay = input("Would you like to continue: (y/n) ")
        while yay_or_nay == 'y':
            p = float(input("Principle: "))
            r = float(input("Rate: "))
            t = float(input("Years: "))
            print(compound_interest.compound_interest_formula(p, r, t))
            yay_or_nay = input("Would you like to continue: (y/n) ")

def checkerboard(num):
    num = int(num)
    for i in range(num):
        if (i % 2) == 0:
            print("* " * num)
        else:
            print(" *" * (num - 1))

def gcd(x, y):
    dividend = max(x, y)
    divisor = min(x, y)
    while divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder
    return dividend

class r_p:

    def relatively_prime(n):
        if n > 99:
            print("Please pick a smaller number")
        else:
            print(f'  {" ".join(map(str, range(n + 1)))}')
            for i in range(n + 1):
                row = []
                for j in range(n + 1):
                    if gcd(i, j) == 1:
                        if len(str(j)) > 1:
                            row.append("* ")
                        else:
                            row.append("*")
                    else:
                        if len(str(j)) > 1:
                            row.append("  ")
                        else:
                            row.append(" ")
                print(f'{str(i)}{" " * (2-len(str(i)))}{" ".join(row)}')

    def main():
        n = int(input("Pick a number: "))
        while n:
            r_p.relatively_prime(n)
            n = int(input("Pick a number: "))

def printTaxicab2(N):
 
    # Starting from 1, check every number if
    # it is Taxicab until count reaches N.
    i, count = 1, 0
    while (count < N): 
     
        int_count = 0
 
        # Try all possible pairs (j, k) 
        # whose cube sums can be i.
        for j in range(1, ceil(\
                    pow(i, 1.0 / 3)) + 1): 
             
            for k in range(j + 1,\
              ceil(pow(i, 1.0 / 3)) + 1): 
                if (j * j * j + k * k * k == i):
                    int_count += 1
         
        # Taxicab(2) found
        if (int_count == 2): 
         
            count += 1
            print(count, " ", i) 
 
        i += 1

    # This code is contributed by Anant Agarwal.

printTaxicab2(10)