#CIS261
#Nakee Hayes
#Week 4 Library Book Tracker 

from datetime import datetime

def display_welcome():
    today = datetime.now()
    date_string = today.strftime("%Y-%m-%d")
    print("=" * 50)
    print("LIBRARY BOOK RETURN SYSTEM")
    print(f"Today's Date: {date_string}")
    print("=" * 50)
    print("Instructions:")
    print("- Enter book information when prompted.")
    print("- Type 'ESC' to end book return process when finished.")
    print("- Late Fee: $0.25 per day after 14 days.")
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
    late_fee = 0.0              #Set defalut values first and change them if needed based on conditions
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
    print(f"Book Condition: {condition}")
    print(f"Total Fee: ${fee:.2f}")
    print("=" * 50)
    print("Book return recorded successfully!\n")

def display_summary(total_books, total_fees, average_fees, highest_fee, lowest_fees):
    today = datetime.now()
    date_string = today.strftime("%m/%d/%Y")
    print("\n")
    print("=" * 50)
    print("END OF DAY SUMMARY")
    print("=" * 50)
    print(f"Date: {date_string}")
    print("=" * 50)
    print(f"Total Books Processed: {total_books}")
    print(f"Total Fees Collected: $ {total_fees: .2f}")
    print(f"Average Fee per Book: $ {average_fees:.2f}")
    print(f"Highest Fee Charged:  $ {highest_fee:.2f}")
    print(f"Lowest Fee Charged:  $ {lowest_fees:.2f}")
    print("=" * 50)
    print("Thank you for using the Library Book Tracker!\n")

def display_all_checkouts(checkouts):
     print("=" * 50)
     print("All Book Checkouts - Detailed List")
     print("=" * 50)
     for i, checkout in enumerate(checkouts, 1):
        date_string = checkout["date"].strftime("%m/%d/%Y")
        print(f"\nCheckout #{i}:")
        print(f"  Date:  {date_string}")
        print(f"  Book:  {checkout['title']}")
        print(f"  Borrower:  {checkout['borrower']}")
        print(f"  Days:   {checkout['days']}")
        print(f"  Condition: {checkout['condition']}")
        print(f"  Fee:  ${checkout['fee']:.2f}")
     print("=" * 50)

def calculate_statistics(checkouts):
     if len(checkouts) == 0:
          return 0.0, 0.00, 0.00, 0.00
     fees = [checkout["fee"] for checkout in checkouts]
     total_fees = sum(fees)
     average_fees = total_fees / len(fees)
     highest_fee = max(fees)
     lowest_fees = min(fees)
     return total_fees, average_fees, highest_fee, lowest_fees

def find_checkouts_by_borrower(checkouts, borrower_name):
    results = []
    for checkout in checkouts:
            if checkout["borrower"].lower() == borrower_name.lower():
                results.append(checkout)
    return results

def find_overdue_books(checkouts):
    overdue = []
    for checkout in checkouts:
        if checkout['days'] > 14:
            overdue.append(checkout)
    return overdue

def find_damaged_books(checkouts):
    damaged = []
    for checkout in checkouts:
        if checkout['condition'] == "Fair" or checkout['condition'] == "Damaged":
            damaged.append(checkout)
    return damaged

def display_filtered_checkouts(checkouts, filter_description):
    print("\n" + "=" * 50)
    print(f"{filter_description.upper()}")
    print("=" * 50)
    if len(checkouts) == 0:
        print("No matching records found.")
    else:
        print(f"Found {len(checkouts)} record(s):\n")
        for checkout in checkouts:
            date_string = checkout['date'].strftime("%m/%d/%Y")
            print(f"  Book:  {checkout['title']}")
            print(f"  Date:  {date_string}")
            print(f"  Borrower:  {checkout['borrower']}")
            print(f"  Days:   {checkout['days']}, Condition: {checkout['condition']}")
            print(f"  Fee:  ${checkout['fee']:.2f}")
            print()
    print("=" * 50)

def save_checkouts_to_file(checkouts, filename):
    try:
        with open(filename, 'a') as file:
            for checkout in checkouts:
                date_string = checkout["date"].strftime("%Y-%m-%d")
                line = f"{checkout['title']}|{checkout['borrower']}|{checkout['days']}|{checkout['condition']}|{checkout['fee']:.2f}|{date_string}\n"
                file.write(line)
        print("\n" + "=" * 50)
        print("FILE SAVE SUCCESSFUL")
        print("=" * 50)
        print(f"Saved {len(checkouts)} record(s) to: {filename}")
        print("=" * 50)
    except Exception as e:
        print(f"\nError saving file: {e}")





def main():
    display_welcome()
    titles = []
    borrowers = []
    days_lists = []
    conditions = []
    fees = []
    dates = []
    
    while True:
        title, borrower, days, condition = get_book_info()
        if title == "ESC":
            break 
        fee = calculate_fees(days, condition)
        display_checkout(title, borrower, days, condition, fee)
        titles.append(title)
        borrowers.append(borrower)
        days_lists.append(days)
        conditions.append(condition)
        fees.append(fee)
        dates.append(datetime.now())

    if len(titles) > 0:
        display_all_checkouts(titles, borrowers, days_lists, conditions, fees)
        total_fees, average_fees, highest_fee, lowest_fees = calculate_statistics(fees)
        display_summary(len(titles), total_fees, average_fees, highest_fee, lowest_fees)
    else:
            print("\nNo books were processed today.")






main()