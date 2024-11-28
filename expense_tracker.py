import csv
import datetime

def add_expense(amount, category, description):
    today = datetime.date.today()
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([today, amount, category, description])

def view_expenses():
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def get_user_input_and_add_expense():
    # Asking the user for input
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")
    description = input("Enter a brief description: ")

    # Calling the add_expense function with the user's input
    add_expense(amount, category, description)

# Example call to get user input
get_user_input_and_add_expense()
view_expenses()
#newline='': This parameter ensures that extra newline characters are not added when writing rows, which helps keep the CSV file correctly formatted.
#csv.writer: The csv.writer() object allows you to write a list of values directly as a row to the file with writer.writerow().
#csv.reader: Reads each line of the file as a list, making each line an element in the reader object. Iterating over reader gives each row as a list of strings.
