from datetime import datetime
from book import empty_basket

def update_order_history(user_email, basket, total_price):
    with open('order_history.txt', 'a') as file:
        current_date = datetime.now().strftime("%d-%m-%Y")
        book_titles = ', '.join(book.title for book in basket)
        file.write(f"{current_date}, {user_email}, {book_titles}, {total_price}\n")

def member_checkout(user_email, basket):
    total_price = 0
    for Book in basket:
        total_price += float(Book.price)
    update_order_history(user_email, basket, total_price)
    print("**********************************************")
    print("*                 Checkout.                  *")
    print("**********************************************")
    print(f"Your total will be: {total_price}. Please enter payment details...")
    print("=============================================================")
    print("Purchase complete.")
    empty_basket()
    quit = input("Would you like to continue shopping? Y / N: ").lower()
    if quit == 'n':
        print("Thank you for shopping at BookIo! Goodbye.")
        exit()

def guest_checkout(basket):
    total_price = 0
    for book in basket:
        total_price += float(book.price)
    print("**********************************************")
    print("*                 Checkout.                  *")
    print("**********************************************")
    print(f"Your total will be: {total_price}. Please enter payment details...")
    print("=============================================================")
    print("Purchase complete.")
    empty_basket()
    quit = input("Would you like to continue shopping? Y / N: ").lower()
    if quit == 'n':
        print("Thank you for shopping at BookIo! Goodbye.")
        exit()