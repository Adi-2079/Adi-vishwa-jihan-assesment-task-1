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
                return True

    # Display an error message
    print("Invalid username or password")
    return False


def register():
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username already exists
    with open("users.txt", "r") as f:
        for line in f:
            user, passw = line.split()
            if username == user:
                print("Username already taken")
                return False

   
    with open("users.txt", "a") as f:
        f.write(f"{username} {password}\n")

    print("Registration successful!")
    return True


def main():
    while True:
        print("Welcome to the login system!")
        print("Choose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            if login():
                # Perform logged-in operations
                print("Logged in. Access granted.")
                break  # Exit the loop after successful login
        elif choice == "2":
            if register():
                # Perform post-registration operations
                print("Registration complete. You can now login.")
        elif choice == "3":
            break  # Exit the loop if the user chooses to quit
        else:
            print("Invalid choice. Please try again.")


# Call the main function to start the login system
main()

