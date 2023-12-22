import uuid
from datetime import datetime, timezone


class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.create_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def update(self, title = None, amount = None):
        if title is not None and amount is not None:
            self.title = title
            self.amount = amount
            self.updated_at = datetime.now(timezone.utc)
            print(f"Expense was successfilly updated at {self.updated_at}")

    def to_dict(self):
        return {
            "Id": self.id,
            "title": self.title,
            "amount": self.amount,
            "create_at": self.create_at.isoformat(sep=' '),
            "updated_at": self.updated_at.isoformat(sep=' ')
        }

class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print ("New expense was added to the Database!!")

    def remove_expense(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
        print("Expense was been removed successfully")

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense

    def get_expense_by_title(self, expense_title):
        expenseslist = [expense for expense in self.expenses if expense.title == expense_title]
        return expenseslist


    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]