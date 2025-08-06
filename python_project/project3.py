import sqlite3
from datetime import datetime

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INT PRIMARY KEY AUTOINCREMENT,
    amount INT NOT NULL,
    category TEXT NOT NULL,
    note TEXT,
    timestamp TEXT NOT NULL
)
""")
conn.commit()

def add_expense():
    try:
        amount = float(input("Enter amount: Rs. "))
        category = input("Enter category (e.g. Food, Travel, Shopping,Other): ")
        note = input("Enter a note (optional): ")
        timestamp = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("INSERT INTO expenses (amount, category, note, timestamp) VALUES (?, ?, ?, ?)",
                       (amount, category, note, timestamp))
        conn.commit()
        print("✅ Expense added successfully!\n")
    except ValueError:
        print("Invalid input. Please enter a number for amount.\n")


def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if not rows:
        print("📭 No expenses found.\n")
        return

    print("\nID | Amount | Category | Note | Timestamp")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]} | Rs. {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    print()


def total_expense():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    print(f"\n💰 Total Expense: Rs. {total if total else 0}\n")


def view_by_date():
    date = input("Enter date (YYYY-MM-DD): ")
    cursor.execute("SELECT * FROM expenses WHERE DATE(timestamp) = ?", (date,))
    rows = cursor.fetchall()

    if not rows:
        print("📭 No expenses found on this date.\n")
        return

    print("\nID | Amount | Category | Note | Timestamp")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]} | Rs. {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    print()


def main():
    while True:
        print("====== My Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expense")
        print("4. View by Date")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            view_by_date()
        elif choice == '5':
            print("👋 Exiting. Your expenses are saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()


conn.close()
