bitmap = """
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
"""
def print_bitmap(word):
    list_word = list(word)
    x = 0
    sentence = []
    for i in list(bitmap):
        if i == " ":
            sentence.append(" ")
        elif i == "*":
            sentence.append(list_word[x])
            x += 1
            if x >= len(word):
                x = 0
        else:
            print("".join(sentence))
            sentence = []

def alt_solution(word):
    for line in bitmap.splitlines():
        for num, cha in enumerate(line):
            if cha == " ":
                print(" ", end="")
            else:
                print(list(word)[num % len(word)], end="")
        print()

def main():
    word = input("Word: ")
    alt_solution(word)
    yes_or_no = input("Would you like to continue? (y/n) ")
    if yes_or_no == "n":
        quit()
    elif yes_or_no == "y":
        main()
    else:
        print("Type 'y' or 'n'.")

main()