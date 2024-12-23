import csv
from datetime import datetime

# Function to log expenses to a CSV file
def log_expense(amount, category, description):
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Write headers if the file is empty
        if file.tell() == 0:
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), amount, category, description])

# Function to generate a summary report from the CSV file
def generate_report():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            total = 0.0
            expenses_by_category = {}

            # Skip the header row
            next(reader, None)

            for row in reader:
                # Skip empty rows or rows with missing data
                if len(row) != 4:
                    continue

                date_time, amount, category, description = row
                amount = float(amount)

                # Update the total expense
                total += amount

                # Track total expenses by category
                if category in expenses_by_category:
                    expenses_by_category[category] += amount
                else:
                    expenses_by_category[category] = amount

            # Display total expenses
            print(f'\n{"="*30}\nSummary of Expenses\n{"="*30}')
            print(f'Total Expenses: ₱{total:.2f}')

            # Display expenses by category
            print("\nExpenses by Category:")
            for category, total_category in expenses_by_category.items():
                print(f'  - {category}: ₱{total_category:.2f}')

            print("\nDetails saved in 'expenses.csv'.")
    
    except FileNotFoundError:
        print('No expenses logged yet. Please add expenses to generate a report.')
    except Exception as e:
        print(f'An error occurred: {e}')

# Example usage of the expense tracker functions
log_expense(150.75, 'Groceries', 'Bought fruits and vegetables')
log_expense(250.00, 'Transportation', 'Taxi ride to work')
log_expense(500.00, 'Entertainment', 'Movie tickets')
log_expense(200.50, 'Utilities', 'Paid electricity bill')
log_expense(300.00, 'Health', 'Bought medicine')
log_expense(100.00, 'Dining Out', 'Lunch with friends')

# Generate a detailed summary report
generate_report()
