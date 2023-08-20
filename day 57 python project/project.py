from datetime import datetime
import re

users = []


# Function to validate name
def validate_name(names):
    name_list = names.split()
    return len(name_list) == 2 and all(re.match(r'^[A-Za-z]+$', name) for name in name_list)


# Function to validate mobile number
def validate_mobile_num(mobile_number):
    return re.match(r'^0\d{9}$', mobile_number) is not None


# Function to validate password
def validate_pssd(password):
    return re.match(r'^(?=.*[A-Za-z])[\w@&]+$', password) is not None


# Function to validate date of birth
def validate_dob(date_birth):
    try:
        dob_date = datetime.strptime(date_birth, '%d/%m/%Y')
        current_date = datetime.now()
        age = current_date.year - dob_date.year - (
                (current_date.month, current_date.day) < (dob_date.month, dob_date.day))
        return age >= 16
    except ValueError:
        return False


# Function to add a new user
def add_user(name, address, mobile_number, password, date_birth):
    users.append({
        'name': name,
        'address': address,
        'mobile_number': mobile_number,
        'password': password,
        'date_birth': date_birth
    })


# Function to validate user credentials during sign-in
def validate_signin_credentials(mobile_number, password):
    for user in users:
        if user['username'] == mobile_number and user['password'] == password:
            return True
    return False


# Function to check if a username is already taken
def is_username_taken(mobile_number):
    for user in users:
        if user['username'] == mobile_number:
            return True
    return False


# Signup page
def signup():
    names = input("Please enter your name:\n")
    if not validate_name(names):
        print("Invalid name, Ensure to put your Two names and Start with a capital:\n")
        return

    address = input("Please enter your address or press enter to skip:\n")

    mobile_number = input("Please enter your Mobile number:\n")
    if is_username_taken(mobile_number):
        print("Invalid. Phone Number already taken. Please choose a different one.")
        return

    if not validate_mobile_num(mobile_number):
        print("Invalid mobile number format")
        return

    password = input("Please enter your Password:\n")
    if not validate_pssd(password):
        print("Invalid password format.\n")
        return

    date_birth = input("Please enter your date of birth # DD/MM/YYYY (No space):\n")
    if not validate_dob(date_birth):
        print("Invalid date of birth or you are underage. You need to be at least 16 years old.")
        return

    # Add the new user to the list
    add_user(names, address, mobile_number, password, date_birth)
    print("Signup successful!")


# Sign-in page
def signin():
    print("Sign In")
    mobile_number = input("Enter your username (Mobile number): ")
    password = input("Enter your password: ")

    if validate_signin_credentials(mobile_number, password):
        print(f"Login successful! Welcome, {mobile_number} !")
        main_page()
        # You can add code here to continue to the main page or perform other actions
    else:
        print("Login failed. Invalid username or password.")


def main_page():
    print("Please Enter 2.1 to start Ordering")
    print("Please Enter 2.2 to Print Statistics")
    print("please enter 2.3 for Logout")


print("Please Enter 1 for Sign up")
print("Please Enter 2 for Sign in")
print("Please Enter 3 for Quit")
choice = int(input("Enter your choice: "))

if choice == 1:
    signup()
elif choice == 2:
    signin()
elif choice == 3:
    exit("Bye")
else:
    print("Invalid choice. Please try again.\n")
