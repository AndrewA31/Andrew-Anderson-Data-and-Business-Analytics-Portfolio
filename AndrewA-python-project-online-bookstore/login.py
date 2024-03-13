# Login Menu        
def login_page():
    print("**********************************************")
    print("*             Welcome to BookIo!             *")
    print("**********************************************")

    user_email = None
    is_guest = False

    membership_response = input("Do you have an account? Y / N ").lower()

    if membership_response == 'y':
        while True:    
            user_email = input("Please enter your email address: ")
            user_pw = input("Please enter your password: ")
            if authenticate_user(user_email, user_pw):
                print("Logged in successfully as", user_email)
                break
            else:
                print("Invalid email or password.")
                #main()
            

    elif membership_response == 'n':
        guest_or_create = input("Would you like to create an account? Y / N ").lower()
        if guest_or_create == 'y':
            first_name = input("Please enter your first name: ")
            last_name = input("Please enter your last name: ")
            user_email = input("Please enter a valid email address: ").strip()
            user_pw = input("Please enter a password: ")
            if user_email == '' or user_pw == '':
                print("Email or password cannot be empty, please enter a valid email and password.")
            elif user_exists(user_email):
                print("Account with that email already exists.")
            else:
                create_user(first_name, last_name, user_email, user_pw)

        elif guest_or_create == 'n':
            print("Proceeding as Guest...")
            is_guest = True            
    else:
        print("Invalid response, please enter 'Y' or 'N'.")
        #main()
    
    return is_guest, user_email





def authenticate_user(user_email, user_pw):
    with open('user_accounts.txt', 'r') as file:
        for line in file:
            stored_first_name, stored_last_name, stored_user_email, stored_user_pw = line.strip().split(',')
            if stored_user_email == user_email and stored_user_pw == user_pw:
                return True
                
    return False

def create_user(first_name, last_name, user_email, user_pw):
    with open('user_accounts.txt', 'a') as file:
        file.write(f"{first_name},{last_name},{user_email},{user_pw}\n")
    print(f"Account created successfully as {user_email}.")
    return True

def user_exists(user_email):
    try:
        file = open("user_accounts.txt", "r")
        for line in file: 
            stored_user_email, _ = line.strip().split(',')
            if stored_user_email == user_email:
                return True
        return False
    except Exception as e:
        #print(f"{type(e)} -> {e}")
        file = open("user_accounts.txt", "a")
        file.close()


def update_user(user_email, old_details, new_details):
    with open('user_accounts.txt', 'r') as file:
        lines = file.readlines()
        
    with open('user_accounts.txt', 'w') as file:
        for line in lines:
            if user_email in line:
                for old, new in zip(old_details, new_details):
                    line = line.replace(old, new)
                    return True
            file.write(line)
            print("Please sign in again to confirm your account details changes.")
        else:
            return False
            





def account_details(user_email):
    with open('user_accounts.txt', 'r') as file:
        for line in file:
            if user_email in line:
                values = line.strip().split(',')
                print(f"First Name: {values[0]}\nLast Name: {values[1]}\nEmail: {values[2]}\nPassword: {values[3]}")
                old_details = values
                ammend_details = input("Would you like to amend your Account Details? Y / N: ").lower()
                if ammend_details == 'y':

                    new_details = []
                    new_first_name = input("Please enter a new first name: ")
                    new_last_name = input("Please enter a new last name: ")
                    new_user_email = input("Please enter a new email address: ").strip()
                    new_user_pw = input("Please enter a new password: ")
                    if new_first_name == '' or new_last_name == '' or new_user_email == '' or new_user_pw == '':
                        print("Fields cannot be empty, please enter valid details.")
                    else:
                        new_details += [new_first_name,new_last_name,new_user_email,new_user_pw]
                        update_user(user_email, old_details, new_details)
                elif ammend_details == 'n':
                    update_user = False