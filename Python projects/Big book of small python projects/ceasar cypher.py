letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def ceasar_cipher(sentence, encode_or_decode, key):
    if encode_or_decode == "d":
        key = key * -1
    new_sen = []
    for i in list(sentence):
        if i.upper() in letters:
            new_sen.append(letters[(letters.index(str(i.upper())) + key) % 25])
        else:
            new_sen.append(i)
    return "".join(new_sen)

def ceasar_hacker(sentence):
    for i in range(25):
        print(ceasar_cipher(sentence, "e", i))

def main():
    e_or_d = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    if e_or_d == "e" or e_or_d == "d":
        pass
    else:
        print("piss off")
        main()
    k = input("Please enter the key (0 to 25) to use. ")
    mes = input("Enter the message to encrypt. ")
    print(ceasar_cipher(mes, e_or_d, int(k)))
    main()

ceasar_hacker(ceasar_cipher("meet me by the rose bushes tonight.", "e", 4))