
from datetime import datetime, timedelta

class Checkout:
    def __init__(self, title, borrower, days, condition, checkout_date_str=None): #NONE is used to show that a value is missing - its a defualt value
        self.title = title
        self.borrower = borrower
        self.days = days
        self.condition = condition
        if checkout_date_str is None:
            self.checkout_date = datetime.now()
            self.return_date = self.checkout_date - timedelta(days=days)
        else:
            self.checkout_date = datetime.strptime(checkout_date_str, "%Y-%m-%d")
            self.return_date = self.checkout_date +timedelta(days=days)
        self.due_date = self.checkout_date + timedelta(days= 14)
        self.late_fee = 0.0
        self.damage_fee = 0.0
        self.total_fee = 0.00
        self.calculate_fees()

    def calculate_fees(self):
        if self.days > 14:
            late_days = self.days - 14
            self.late_fee = late_days * 0.25
        if self.condition == "Good":
            self.damage_fee = 0.0
        elif self.condition == "Fair":
            self.damage_fee = 5.0
        elif self.condition == "Damaged":
            self.damage_fee = 15.0
        self.total_fee = self.late_fee + self.damage_fee

    def is_overdue(self):
        return self.days > 14
    
    def is_damaged(self):
        return self.condition =="Fair" or self.condition == "Damaged"
    
    def to_file_string(self):
        checkout_date_str = self.checkout_date.strftime("%Y-%m-%d")
        return f"{self.title}|{self.borrower}|{self.days}|{self.condition}|{self.total_fee:.2f}|{checkout_date_str}"
    
    def __str__(self): #String represenation method. Called automatically hen you print object. Can you furhter exaplin this?
        checkout_str = self.checkout_date.strftime("%m/%d/%Y")
        due_str = self.due_date.strftime("%m/%d/%Y")
        return_str = self.return_date.strftime("%m/%d/%Y")
        return (f"Book: {self.title}\n"
                f"      Borrower: {self.borrower}\n"
                f"      Checkout Date: {checkout_str}\n"
                f"      Due Date: {due_str}\n"
                f"      Return Date: {return_str}\n"
                f"      Days Borrowed: {self.days}\n"
                f"      Condition: {self.condition}\n"
                f"      Fee: ${self.total_fee:.2f}"
                )
    

class LibrarianUser:
    def __init__(self, username, password, role):
        self.username = username 
        self.password = password
        self.role = role


def creaate_default_users(): #Why didnt we pass self in the argument?
    users = [] #Why the empty list 
    admin = LibrarianUser("admin", "library2024", "Admin")
    users.append(admin)
    staff = LibrarianUser("staff", "books123", "Staff")
    users.append(staff)
    return users

def display_login_screen():
    print("\n" + "=" * 50)
    print("LIBRARY BOOK TRACKER - SECURE LOGIN")
    print("=" * 50)
    print("Please log in to continue.") #Shouldnt this be an input statment? 
    print("=" * 50)

def authenticate_user(users, username, password):
    for user in users:
        if user.username == username and user.password == password: #Why is it formatted as user. ? We didnt create a class called user??? 
            return user
    return None

def display_access_granted(username, role):
    print("\n" + "=" * 50)
    print("ACCESS GRANTED")
    print("=" * 50)
    print(f"Welcome, {username}!")
    print(f"Your Role: {role}")
    if role == "Admin":
            print(f"\nFull Acess: Proess returns + Generate Reports")
    else:
            print("\nRead-Only Access: Generate reprots only")
    print("=" * 50)
    input("\nPress Enter to continue...")

def display_accsess_denied():
    print("\n" + "=" * 50)
    print("ACCESS DENIED")
    print("=" * 50)
    print("Invalid Username or password.")
    print("\n" + "=" * 50)

def display_menu(role):
    print("\n" + "=" * 50)
    print(f"MAIN MENU - {role} Access")
    print("=" * 50)
    if role == "Admin":
        print("1. Process Book Returns")
        print("2. Generate Reports")
        print("3. Exit")
    else:
        print("1. Generate Reports")
        print("2. Exit")
    print("=" * 50)

def get_menu_choice():
    return input("Enter your choice:  ")


def display_all_checkouts(checkouts):
     print("=" * 50)
     print("All Book Checkouts - Detailed List")
     print("=" * 50)
     for i, checkout in enumerate(checkouts, 1):  #enumerate() adds a counter and returns a series of pairs - which is why we have i - integer and checkout - data 
        checkout_str = checkout.checkout_date.strftime("%m/%d/%Y")
        due_str = checkout.due_date.strftime("%m/%d/%Y")
        return_str = checkout.return_date.strftime("%m/%d/%Y")
        print(f"\nCheckout #{i + 1}:")
        print(f" Checkout Date: {checkout_str}")
        print(f" Due Date:      {due_str}")
        print(f" Return Date:   {return_str} ")
        print(f" Book:          {checkout.title}")
        print(f" Borrower:      {checkout.borrower}")
        print(f" Days Borrowed  {checkout.days}")
        print(f" Condition:     {checkout.condition}")
        print(f" Late Fee:      {checkout.late_fee:.2f}")
        print(f" Damage Fee:    {checkout.damage_fee:.2f}")
        print(f" Total Fee:     {checkout.total_fee:.2f}")
     print("=" * 50)

def calculate_statistics(checkouts):
     if len(checkouts) == 0:
          return 0.0, 0.00, 0.00, 0.00
     fees = [checkout.total_fee for checkout in checkouts] 
     total_fees = sum(fees)
     average_fees = total_fees / len(fees)
     highest_fee = max(fees)
     lowest_fees = min(fees)
     return total_fees, average_fees, highest_fee, lowest_fees #This return statment is technically a Tuple 

def find_checkouts_by_borrower(checkouts, borrower_name):
    results = []
    for checkout in checkouts:
            if checkout.borrower.lower() == borrower_name.lower():
                results.append(checkout)
    return results

def find_overdue_books(checkouts):
    overdue = []
    for checkout in checkouts:
        if checkout.is_overdue():
            overdue.append(checkout)
    return overdue

def find_damaged_books(checkouts):
    damaged = []
    for checkout in checkouts:
        if checkout.is_damaged():
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
            dreturn_str = checkout.return_date.strftime("%m/%d/%Y")
            print(f"  Book:  {checkout.title}")
            print(f"  Date:  {dreturn_str}")
            print(f"  Borrower:  {checkout.borrower}")
            print(f"  Days:   {checkout.days}, Condition: {checkout.condition}")
            print(f"  Fee:  ${checkout.total_fee:.2f}")
            print()
    print("=" * 50)

def generate_report(checkouts):
    today = datetime.now().strftime("%m/%d/%Y")
    print("\n" + "=" * 50)
    print("LIBRARY BOOK TRACKER - COMPLETE REPORT")
    print(f"Report Date: {today}")
    print("=" * 50)
    if len(checkouts) == 0:
        print("No records to display")
        print("=" * 50)
        return
    print(f"\nTotal Checkouts in System: {len(checkouts)}")
    print("\n---All Checkouts---")
    for i, checkout in enumerate(checkouts, 1):
        checkout_str = checkout.checkout_date.strftime("%m/%d/%Y")
        due_str = checkout.due_date.strftime("%m/%d/%Y")
        return_str = checkout.return_date.strftime("%m/%d/%Y")
        print(f"\n{i}. {checkout.title} - {checkout.borrower}")
        print(f"Checked Out: {checkout_str} | Due: {due_str} | Returned {return_str}")
        print(f"Days: {checkout.days}, Condition: {checkout.condition}, Fee: ${checkout.total_fee:.2f}")
    fees = [c.total_fee for c in checkouts]  #What is this doing?
    total_fees = sum(fees)
    average_fees = total_fees / len(fees)
    overdue_count = sum(1 for c in checkouts if c.is_overdue()) # Help me understand this for loop nestling. Why are we using c and how come the methods we made can be added here 
    damaged_count = sum(1 for c in checkouts if c.is_damaged())
    print("\n---Statistics---")
    print(f"Total Feed Collectted:      ${total_fees:.2f}")
    print(f"Average Fee per Checkout:    ${average_fees:.2f}")
    print(f"Overdue Returns:        {overdue_count}")
    print(f"Damaged Books:          {damaged_count}")
    print("\n" + "=" * 50)
    input("Press Enter to return to menu...")


def save_checkouts_to_file(checkouts, filename):
    try:
        with open(filename, 'a') as file:
            for checkout in checkouts:
                line = checkout.to_file_string()
                file.write(line + "\n")
        print("\n" + "=" * 50)
        print("FILE SAVE SUCCESSFUL")
        print("=" * 50)
        print(f"Saved {len(checkouts)} record(s) to: {filename}")
        print("=" * 50)
    except Exception as e:
        print(f"\nError saving file: {e}")

def load_checkouts_from_file(filename):
    checkouts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    date_object = datetime.strptime(parts[5], "%Y-%m-%d")
                    checkout = Checkout(
                        title=parts[0], #Why ths formating ? What is the syntax behing this? 
                        borrower=parts[1],
                        days=int(parts[2]), 
                        condition=parts[3], 
                        checkout_date_str=parts[5]

                    )
                    checkouts.append(checkout)
        print(f"Loaded {len(checkouts)} records(s) from {filename}")
        return checkouts
    except FileNotFoundError:
        print(f"No previous data found in {filename}")
        return []
    except Exception as e:
        print(f"Error readin file: {e}")
        return []

def process_return(filename):
    print("\n" + "=" * 50)
    print("PROCESSS BOOK RETURNS")
    print("=" * 50)
    print("Tip: Type 'ESC' when fininshed\n")
    checkouts = []
    while True:
        print("\n--- Enter Book Return Information ---")
        title = input("Book title (or type 'ESC' to fininsh):   ")
        if title.upper() == "ESC":
            break
        borrower = input("Borrower name:    ")
        days = int(input("Days borrowed:    "))
        print("Condtion otions: Good, Fair, Damaged")
        condition = input("Book Condition   ")
        checkout = Checkout(title, borrower, days, condition) #We use this formatiing when ...?
        today = datetime.now().strftime("%m/%d/%Y")
        print("\n" + "=" * 50)
        print("CHECKOUT PROCESSED")
        print(f"Date: {today}")
        print("=" * 50)
        print(f" Book Title:        {checkout.title}")
        print(f" Borrower:          {checkout.borrower}")
        print(f" Days Borrowed      {checkout.days}")
        print(f" Book Condition:    {checkout.condition}")
        print(f" Total Fee:         {checkout.total_fee:.2f}")
        print("=" * 50)
        print("Book return recorded successfully!\n")
        checkouts.append(checkout)
    if len(checkouts) > 0:
        save_checkouts_to_file(checkouts, filename)
    else:
        print("\nNo books were processed.")

def generate_reports(filename):
    print("\n" + "=" * 50)
    print("GENERATE REPORTS")
    print("=" * 50)
    checkouts = load_checkouts_from_file(filename)
    if len(checkouts) == 0:
        print("\nNo checkout records found in the system.")
        input("Press enter to continue...")
        return 
    generate_report(checkouts)  #Why do some functions require it to be called at the end and some require return statments and others dont


def main():
    filename = "checkouts.txt"
    valid_users = creaate_default_users()
    display_login_screen()
    username = input("Username: ")
    password = input("Password: ")
    current_user = authenticate_user(valid_users, username, password)
    if current_user is None:
        display_accsess_denied()
        return
    
    display_access_granted(current_user.username, current_user.role) #Why did we use the dot notation here ? and why pass info in here if the function already has it in the bluepint
    while True:
        display_menu(current_user.role)
        choice = get_menu_choice()
        if choice == "1":
            if current_user.role == "Admin":
                process_return(filename)
            else:
                generate_reports(filename)
        elif choice == "2":
            if current_user.role == "Admin":
                generate_reports(filename)
            else: 
                print(f"\nThank you, {current_user.username}!")
                print("Logging out...")
                break
        elif choice == "3" and current_user.role == "Admin":
            print(f"\nThank you, {current_user.username}!")
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
        

main()