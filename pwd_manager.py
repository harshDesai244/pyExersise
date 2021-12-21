master_pwd = input("What is the master password? ")


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line)


def add():
    name = input("Account Name: ")
    pwd = input("password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + pwd + "\r\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ons (view, add), press q ti quit? ")

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input")
        continue
