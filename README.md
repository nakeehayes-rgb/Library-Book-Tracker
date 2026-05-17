# Library Book Tracker

A playful command-line tracker for library returns, fees, and reports.

## What it does

- Lets Admins log returns and record fees
- Lets Staff generate and view reports
- Saves entries in `checkouts.txt`
- Uses built-in classes for clean data handling
- Uses the Python `datetime` library for dates and due-date math

## How it works

- `Checkout` class stores each return record and calculates fees
- `LibrarianUser` class manages user accounts and access roles
- `checkouts.txt` is the main data file for saved return history
- `save_checkouts_to_file()` writes new records
- `load_checkouts_from_file()` reads saved records back in

## Login & security

- Simple authorization is built in with hard-coded users
- Admin can process returns and run reports
- Staff can only generate reports
- Access control is enforced by role checks in the menu

## Run it

```bash
python CIS261_libraryBook_Tracker_.py
```

Then log in and choose what to do.

## Quick rules

- Borrowed over 14 days? Late fee applies.
- Condition fees:
  - `Good` = $0
  - `Fair` = $5
  - `Damaged` = $15

## Files

- `CIS261_libraryBook_Tracker_.py` — main script
- `checkouts.txt` — saved return records
