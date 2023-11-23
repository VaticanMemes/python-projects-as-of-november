import random

def correct_check(guess, num):
    return True if int(guess) == int(num) else False

def bagel_check(guess, num):
    for i in list(str(guess)):
        if i in str(num):
            return False
    return True

def fermi_check(guess, num):
    if list(str(guess))[0] == list(str(num))[0] or list(str(guess))[1] == list(str(num))[1] or list(str(guess))[2] == list(str(num))[2]:
        return True
    return False

def pico_check(guess, num):
    # redundant
    for i in list(str(guess)):
        if i in str(num):
            return False
    return True

def main():
    guess = input("Turn 1; Guess a three digit number: ")
    num = random.randint(100, 999)
    turns = 0
    while turns < 10:
        if correct_check(guess, num) == True:
            print(f"Correct; You did it in {str(turns)} turns")
            break
        elif bagel_check(guess, num) == True:
            print("Bagel")
            turns += 1
            guess = input(f"Turn {str(turns + 1)}; Guess a three digit number: ")
            continue
        elif fermi_check(guess, num) == True:
            print("Fermi")
            turns += 1
            guess = input(f"Turn {str(turns + 1)}; Guess a three digit number: ")
            continue
        else:
            print("Pico")
            turns += 1
            guess = input(f"Turn {str(turns + 1)}; Guess a three digit number: ")
            continue
    main()

main()