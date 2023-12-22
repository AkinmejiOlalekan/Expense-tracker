## Project Description
This project code defines two classes, Expense and ExpenseDatabase, which are used to manage 
and store information about expenses.

### Expense Class:
The Expense class represents an individual expense and has the following attributes:

- id: A unique identifier that was generated using the uuid module.
- title: A string representing the title or description of the expense.
- amount: A numerical value representing the expense amount.
- create_at: A timestamp indicating the creation time of the expense in UTC.
- updated_at: A timestamp indicating the last update time of the expense in UTC.

### The class has the following methods:

==> __init__(self, title, amount): Initializes a new expense with the provided title and amount, generating 
    a unique ID and setting the creation and update timestamps.

==> update(self, title=None, amount=None): Updates the expense's title and/or amount if new values are 
    provided, and updates the updated_at timestamp.

==> to_dict(self): Converts the expense object to a dictionary for easy serialization. The dictionary includes the 
    expense's ID, title, amount, creation time, and last update time.

### ExpenseDatabase Class:
The ExpenseDatabase class manages a collection of expenses by storing them in a list and has the following attributes:

- expenses: A list to store instances of the Expense class.

### The class has the following methods:

==> __init__(self): Initializes an empty list to store expenses.

==> add_expense(self, expense): Adds a new expense to the database by appending it to the list of expenses. Prints a 
    message indicating that a new expense has been added.

==> remove_expense(self, expense_id): Removes an expense from the database based on its ID. Prints a message 
    indicating the success of the removal.

==> get_expense_by_id(self, expense_id): Retrieves an expense from the database based on its ID.

==> get_expense_by_title(self, expense_title): Retrieves a list of expenses from the database based on their titles.

==> to_dict(self): Converts all expenses in the database to a list of dictionaries using the to_dict method of 
    each expense.
    
## How the project can be cloned.
1.) On GitHub.com, navigate to the main page of the repository.
2.) Above the list of files, click <> Code.
3.) Copy the URL for the repository.
    - You can clone using HTTPs, SSH key and GitHub CLI by copying the links
4.) Open Git Bash (or another command line interface).
5.) Change the current working directory to where you want the cloned repository to be made.
6.) Type "git clone" followed by the URL you copied. For example: git clone https://github.com/username/repository.git
7.) Press Enter to create your local clone.

## Running the Project Code.
To run a GitHub repository example, the following steps can be followed:

- After cloning the repository to your local machine using the 'git clone' command.
- Change into the directory of the cloned repository using cd.
- Then you can run the project using the implemented codes


### Usage example
```
# Creating an expense
expense1 = Expense("Timeless", 4500)

# Creating an expense database
db_expense = ExpenseDatabase()

# Adding the expense to the database
db_expense.add_expense(expense1)

# Retrieving an expense by ID
retrieved_expense =db_expense.get_expense_by_id(expense1.id)

# Updating the expense
retrieved_expense.update(title="Timeles Album", amount=68000)

# Removing the expense from the database
db_expense.remove_expense(expense1.id)

# Converting the database to a list of dictionaries
db_expense_dict =db_expense.to_dict()

```
