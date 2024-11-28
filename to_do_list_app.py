tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added to the list.")
    
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' has been removed from the list.")
    else:
        print("Task not found!")
def show_tasks():
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks in list.")

print("Welcome to the To do List App!")
while True:
    print("\n")
    print("Choose what you want to do:")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. Show all tasks")
    print("4. Quit")
    choice = int(input("Enter your choice: "))

    if (choice == 1):
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif (choice == 2):
        task = input("Enter the task you want to remove: ")
        remove_task(task)
    elif (choice == 3):
        show_tasks()
    elif (choice == 4):
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")
