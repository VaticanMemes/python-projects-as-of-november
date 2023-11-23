import random

BOXES = """
  __________      __________
 /         /|    /         /|
+---------+ |   +---------+ |
|   {}  | |   |   {}  | |
|   BOX   | /   |   BOX   | /
+---------+/    +---------+/
"""

CARROT_IN_BOX = """
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|     __________
 /    ||   /|    /         /|
+---------+ |   +---------+ |
|   {}  | |   |   {}  | |
|   BOX   | /   |   BOX   | /
+---------+/    +---------+/
"""
# .format("RED ", "GOLD") or .format("GOLD", "RED ")

CARROT_NOT_IN_BOX = """
   _________
  |         |
  |         |
  |_________|     __________
 /         /|    /         /|
+---------+ |   +---------+ |
|   {}  | |   |   {}  | |
|   BOX   | /   |   BOX   | /
+---------+/    +---------+/
"""
# .format("RED ", "GOLD") or .format("GOLD", "RED ")

def main():
    while True:
        play = input("Would you like to play? (y/n) ")
        if play == "y":
            break
        elif play == "n":
            quit()
        else: 
            play = "Would you like to play? (y/n) "
            continue
    print("Here are two boxes:")
    print(BOXES.format("RED ", "GOLD"))
    print("Mr Red, you can look inside your box when Gold closes their eyes")
    while True:
        enter = input("Mr Red, press enter when Gold has closed their eyes ... ")
        if enter == "enter":
            break
        else:
            continue
    path = random.randint(0, 1)
    if path == 1:
        print(CARROT_IN_BOX.format("RED ", "GOLD"))
    else:
        print(CARROT_NOT_IN_BOX.format("RED ", "GOLD"))
    swap = input("Mr Gold, would you like to swap boxes? (y/n) ")
    while True:
        if swap == "y":
            red_win = 1 - path
            break
        elif swap == "n":
            red_win = path
            break
        else:
            swap = input("Mr Gold, would you like to swap boxes? (y/n) ")
            continue
    if red_win == 1:
        print("Red wins")
    elif red_win == 0:
        print("Gold wins")
    else:
        print("bug lol. no winners")
    main()

main()

#testing lol