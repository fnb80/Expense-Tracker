RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"

# Dictionary to store all expenses by category
expenses = {
  "food": [],
  "transport": [],
  "entertainment": []
}

def main_menu():
  print(YELLOW+"Welcome to the Expense Tracker!"+RESET)
  print ("")
  print ("[1] Add expense ")
  print ("[2] View All Expenses ")
  print ("[3] Delete an Expense ")
  print ("[4] Enter Calculator Mode")
  print("[q] Quit")

while True:
    # Show menu
    main_menu()
    # Get user choice
 choice = input(CYAN + "Select an option (1-4 or q): " + RESET)

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        calculating_total_expenses()

    elif choice == "4":
         deleting_expenses ()

    elif choice.lower() == "q":
        print(GREEN + "Goodbye!" + RESET)
        break

    else:
        print(RED + "Invalid option. Please choose 1-4 or q." + RESET)

def add_expense():
  # Ask the user to choose a category
  category = input(CYAN + "Enter category (food / transport / entertainment): " + RESET).lower()

  # Check if the category exists in the dictionary
  if category not in expenses:
    print(RED + "Invalid category. Expense not added." + RESET)
    return

  # Ask the user to enter the expense amount
  # Use try-except to prevent crashes if the input is not a number
  try:
    amount = float(input(CYAN + "Enter amount: " + RESET))
  except ValueError:
    print(RED + "Invalid amount. Please enter a number." + RESET)
    return

  # Ask the user to enter the date of the expense
  date = input(CYAN + "Enter date (YYYY-MM-DD): " + RESET)

  # Create a dictionary to represent one expense
  expense = {
    "amount": amount,
    "date": date
  }

  # Add the expense to the correct category list
  expenses[category].append(expense)

  # Confirm that the expense was added successfully
  print(GREEN + "Expense added successfully!" + RESET)
  
  def view_expenses():
  # Check if there are any expenses stored
  # If all categories are empty, show a message
  if not expenses["food"] and not expenses["transport"] and not expenses["entertainment"]:
    print(YELLOW + "No expenses have been added yet." + RESET)
    return

  # Loop through each category and its expense list
  for category, expense_list in expenses.items():
    print(BOLD + CYAN + f"\nCategory: {category.capitalize()}" + RESET)

    # If the category has no expenses, let the user know
    if not expense_list:
      print("  No expenses in this category.")
    else:
      # Loop through each expense in the list
      for expense in expense_list:
        # Display each expense with amount and date
        print(f"  - ${expense['amount']:.2f} on {expense['date']}")
  





