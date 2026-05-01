
import json
def show_menu():
    print("------Expense Manger-------")
    print("1. Add Expense ")
    print("2. View Expense ")
    print("3. Show Summary ")
    print("4. Exit ")


class Expense:

    def __init__(self,name,amount,category):
        self.name = name
        self.amount = amount 
        self.category = category
    
    def __str__(self):
        return f"{self.name} - {self.amount}Rs - {self.category}"

class ExpenseManager :
    def __init__(self):
        self.expenses = []

    def add_expense(self,expense):
        self.expenses.append(expense)
    
    def view_expenses(self):
        if not self.expenses:
            print("No expenses found")
            return
        for exp in self.expenses:
            print(exp)

manager = ExpenseManager()

def add_expense():
    name = input("Enter expense name : ")
    amount = float(input("Enter amount : "))
    category = input("Enter category : ")

    expense = Expense(name,amount,category)

    manager.add_expense(expense)

    
def view_expenses():
    manager.view_expenses()

def save_to_file(manager):
    data = []

    for exp in manager.expenses:
        data.append({
            "name" : exp.name,
            "amount" : exp.amount,
            "category" : exp.category
        })
    
    with open("expenses.json","w") as f:
        json.dump(data,f)

def load_from_file(manager):

    try : 

        with open("expenses.json", "r") as f:
            data = json.load(f)

            for item in data:
                expense = Expense(item["name"],item["amount"],item["category"])
                
                manager.add_expense(expense)
    
    except FileNotFoundError:
        pass            

load_from_file(manager)

def show_summary():
    
    summary = {}
    for exp in manager.expenses:
        if exp.category in summary:
            summary[exp.category] += exp.amount
        else:
            summary[exp.category] = exp.amount

    print("\n--------Summary----------")
    for category,total in summary.items():
        print(f'{category} : {total} Rs')

while True : 
    show_menu()
    choice = input("Enter you choice : ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        save_to_file(manager)
        print("Data Saved. Exiting .....")
        break
    else : 
        print("Invalid Choice")


