# Define the login function
def login():
    # Get the username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password are valid
    with open("users.txt", "r") as f:
        for line in f:
            user, passw = line.split()
            if username == user and password == passw:
                print("Login successful!")
                return

    # Display an error message
    print("Invalid username or password")

# Define the register function
def register():
    # Get the username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username is already taken
    with open("Cusers.txt", "r") as f:
        for line in f:
            user, passw = line.split()
            if username == user:
                print("Username already taken")
                return

    # Write the username and password to the text file
    with open("users.txt", "a") as f:
        f.write(f"{username} {password}\n")

    print("Registration successful!")


while True:
   
    print("Welcome to the game! Please Login or Register.")

    # Get the user's choice
    choice = input("Type 'R' to Register or 'L' to Login: or 'Q' to quit ")

    # If the user chooses to login
    if choice.upper() == "L":
        login()

    # If the user chooses to register
    if choice.upper() == "R":
        register()

    # If the user chooses to quit
    if choice.upper()== "Q":
        break