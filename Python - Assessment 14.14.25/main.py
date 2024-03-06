from book import Book, book_search, basket, add_book

from login import authenticate_user, create_user, user_exists, account_details

from checkout import member_checkout, guest_checkout

# Menus
def guest_menu():
    print("**********************************************")
    print("*                Guest Menu                  *")
    print("**********************************************")
    print("1. Search Books.")
    print("2. View shopping basket.")
    print("3. Proceed to checkout.")
    print("4. Exit store.")  
        

def member_menu():
    print("**********************************************")
    print("*                Member Menu                 *")
    print("**********************************************")
    print("1. Search Books.")
    print("2. View shopping basket.")
    print("3. Proceed to checkout.")
    print("4. View Order History.")
    print("5. View Account Details.")
    print("6. Exit Store.")
    

# Login logic


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
                main()
            

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
    
    return is_guest, user_email
    

# Search Books
    
def main():

    is_guest, user_email = login_page()

    def menu():

        if is_guest:

            guest_menu()
            while True:

                guest_menu_choice = input("Please enter your menu choice (1-3): ")
                if guest_menu_choice == '1':
                    add_book()
                    menu()
                    break
                    
                elif guest_menu_choice == '2':
                    if basket:
                        total_price = 0
                        for book in basket:
                            total_price += float(book.price)
                        print("**********************************************")
                        print("*                Your Basket:                *")
                        print(f"                Total Price: {total_price}  " )
                        print("**********************************************")
                        for book in basket:
                            print(book.title,book.price)
                        menu()
                        break
                    else:
                        print("**********************************************")
                        print("*              Basket is empty.              *")
                        print("**********************************************")
                        menu()

                elif guest_menu_choice == '3':
                    if basket:
                        guest_checkout(basket)
                        menu()   
                    else:
                        print("**********************************************")
                        print("*   Basket is empty. Nothing to checkout.    *")
                        print("**********************************************")
                        menu()

                elif guest_menu_choice == '4':
                    exit_store = input("Would you like to exit the store? Y / N: ").lower()
                    if exit_store == 'y':
                        print("Thank you for shopping at BookIo. Goodbye.")
                    else:
                        menu()
                    break
              
                else:
                    print("Invalid Choice, please select one of the options")
                
        else:

            member_menu()
            while True:

                member_menu_choice = input("Please enter your menu choice (1-5): ")
                if member_menu_choice == '1':
                    add_book()
                    menu()
                    break
                    
                elif member_menu_choice == '2':
                    if basket:
                        total_price = 0
                        for book in basket:
                            total_price += float(book.price)
                        print("**********************************************")
                        print("*                Your Basket:                *")
                        print(f"                Total Price: {total_price}  " )
                        print("**********************************************")
                        for book in basket:
                            print(book.title,book.price)
                        menu()
                        break
                    else:
                        print("**********************************************")
                        print("*              Basket is empty.              *")
                        print("**********************************************")
                        menu()
                        break

                elif member_menu_choice == '3':
                    if basket:
                        member_checkout(user_email, basket)                     
                        break
                    else:
                        print("**********************************************")
                        print("*   Basket is empty. Nothing to checkout.    *")
                        print("**********************************************")
                        menu()

                  
                elif member_menu_choice == '4':
                    print("**********************************************")
                    print("*               Order History.               *")
                    print("**********************************************")
                    found_history = False
                    with open('order_history.txt', 'r') as file:
                        for line in file:
                            if user_email in line:
                                print(line)
                                found_history = True
                    if not found_history:
                        print("No Order History.")
                    menu()
                                
                elif member_menu_choice == '5':
                    print("**********************************************")
                    print("*              Account Details.              *")
                    print("**********************************************")
                    account_details(user_email)
                    menu()
                                    
                                


                elif member_menu_choice == '6':
                    exit_store = input("Would you like to exit the store? Y / N: ").lower()
                    if exit_store == 'y':
                        print("Thank you for shopping at BookIo. Goodbye.")                       
                    else:
                        menu()
                    break

                else:
                    print("Invalid Choice, please select one of the options")
    menu()
        
        
main()
