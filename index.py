import hashlib
import getpass


def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    file = open("database.txt", "a")
    file.write(f"{username} : {hashed_password}\n")
    print("Account created successfully!")


def login():
    username = input("Enter your username: ")
    entered_password = getpass.getpass("Enter your password: ")
    entered_password = hashlib.sha256(entered_password.encode()).hexdigest()
    file = open("database.txt")
    for line in file:
        user, password = line.strip().split(" : ")
        if user == username:
            if entered_password == password:
                print("Login successful!")
            else:
                print("Invalid username or password.")
        else:
            print("Invalid username or password.")


def main():
    while True:
        choice = input("Enter a command (create, login, exit): ")
        if choice == "create":
            create_account()
        elif choice == "login":
            login()
        elif choice == "exit":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
