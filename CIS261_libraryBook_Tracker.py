#CIS261
#Nakee Hayes
#Week 2 Library Book Tracker 

from datetime import datetime

def display_welcome():
    today = datetime.now()
    date_string = today.strftime("%Y-%m-%d")
    print("=" * 50)
    print("LIBRARY BOOK RETURN SYSTEM")
    print(f"Today's Date: {date_string}")
    print("=" * 50)
    print("Instructions:")
    print(" -Enter book information when prompted.")
    print("- Type 'ESC' to end book return process when finished.")
    print("- Late Fee: $0.25 per dat after 14 days.")
    print("- Damage Fees: Good=$0, Fair=$5, Damaged=$15")
    print("=" * 50)

def get_book_info():
    print("\n---Enter Book Return Information---")
    title = input("Book title (or type 'ESC' to finish):  ")
    if title.upper() == "ESC":
        return "ESC", "", 0, ""
    borrower = input("Borrower name:  ")
    days = int(input("Day's borrowed:  "))
    print("Condtion option: Good, Fair, Damaged")
    condition = input("Book condition:  ")
    return title, borrower, days, condition 

def calculate_fees(days_borrowed, condition):
    late_fee = 0.0              #Set defalut values first and change them if needed based on conditions # Do I need to set default values because its in a function? 
    damage_fee = 0.00
    if days_borrowed > 14:     
        late_fee = days_borrowed - 14
        late_fee = late_fee * 0.25
    if condition == "Good":
        damage_fee = 0.0
    elif condition == "Fair":
        damage_fee = 5.0
    elif condition == "Damaged":
        damage_fee = 15.0
    total_fee = late_fee + damage_fee
    return total_fee

def display_checkout(title, borrower, days, condition, fee):
    today = datetime.now()
    date_string = today.strftime("%m/%d/%Y")
    print("\n" + "=" * 50)
    print("CHECKOUT PROCESSED")
    print(f"Date: {date_string}")
    print("=" * 50)
    print(f"Book Title: {title}")
    print(f"Borrower: {borrower}")
    print(f"Days Borrowed: {days}")
    print(f"Total Fee: ${fee:.2f}")
    print("=" * 50)
    print("Book return recorded successfully!\n")

def display_summary(total_books, total_fees):
    today = datetime.now()
    date_string = today.strftime("%m/%d/%Y")
    print("\n")
    print("=" * 50)
    print("END OF DAY SUMMARY")
    print("=" * 50)
    print(f"Date: {date_string}")
    print("=" * 50)
    print(f"Total Books Processed: {total_books}")
    print(f"Total Fees Collected: ${total_fees: .2f}")
    print("=" * 50)
    print("Thank you for using the Library Book Tracker!\n")


def main():
    display_welcome()
    total_books = 0 
    total_fees = 0.0
    while True:
        title, borrower, days, condition = get_book_info()
        if title == "ESC":
            break 
        fee = calculate_fees(days, condition)
        display_checkout(title, borrower, days, condition, fee)
        total_books = total_books + 1
        total_fees = total_fees + fee
    if total_books > 0:
            display_summary(total_books, total_fees)
    else:
            print("\nNo books were processed today.")

main()