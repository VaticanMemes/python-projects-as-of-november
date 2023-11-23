from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def set_master_password():
    master_password = input("Enter a master password: ")
    with open ("little_note.txt", "w") as f:
        f.write(str(master_password))
    with open("master_password.txt", "w") as f:
        f.write(fer.encrypt(master_password.encode()).decode())

"""
#Hint hint, I have no idea what I'm doing
def check_master_password():
    user_mp = input("What is the master password? ")
    f = open("little_note.txt", "r")
    g = open("master_password.txt", "r")
    if fer.decrypt(g.readlines()) == user_mp:
        return True
    else:
        return False
"""

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password_display = data.split("|")
            print("User: " + user + "\nPassword: " + fer.decrypt(password_display.encode()).decode())

def add():
    name = input("Account name: ")
    password = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

# check_master_password()

while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view/quit) ").lower()
    if mode == "quit":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue