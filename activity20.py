from getpass import getpass

u = "vince"
p = "vincethegoat123"

isLogin = False

while isLogin == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    print("")
    print("-------------------------------------------")
    print("")

    if username == u and password == p:
        print("Login successful!")
        isLogin = True
    else:
        print("Invalid username or password. Please try again.")