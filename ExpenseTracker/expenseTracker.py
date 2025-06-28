# Function to add a new expense to the list
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})  # Adds a dictionary to the expenses list

# Function to print all expenses
def print_expenses(expenses):
    for expense in expenses:  # Loop through each expense in the list
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')  # Print formatted expense

# Function to calculate the total amount spent
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))  # Extract amounts and sum them

# Function to filter expenses by a specific category (✅ FIXED by converting to list)
def filter_expenses_by_category(expenses, category):
    return list(filter(lambda expense: expense['category'] == category, expenses))  
    # Filter returns an iterator, so we convert it to a list for reuse and clarity

# Main function to run the expense tracker
def main():
    expenses = []  # Initialize an empty list to hold all expenses

    while True:  # Infinite loop until user chooses to exit
        # Display menu
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')  # Take user's menu choice

        if choice == '1':  # Add expense
            amount = float(input('Enter amount: '))  # Take amount as float
            category = input('Enter category: ')  # Take category name
            add_expense(expenses, amount, category)  # Call function to add

        elif choice == '2':  # List all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)  # Print all recorded expenses
    
        elif choice == '3':  # Show total expenses
            print('\nTotal Expenses: ', total_expenses(expenses))  # Print total of all expenses
    
        elif choice == '4':  # Filter by category
            category = input('Enter category to filter: ')  # Get category from user
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)  # Get filtered list
            print_expenses(expenses_from_category)  # Print filtered expenses
    
        elif choice == '5':  # Exit the program
            print('Exiting the program.')
            break  # Exit the loop and end the program

# Run the program
main()
