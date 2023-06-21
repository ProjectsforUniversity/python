import datetime

# Empty list to store the to-do items
todo_list = []

# Function to display the to-do list
def display_list():
    if len(todo_list) == 0:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for i, item in enumerate(todo_list):
            print(f"{i+1}. {item['task']} (Added on: {item['timestamp']})")

# Function to add an item to the to-do list
def add_item(item):
    if not item:
        print("Task cannot be empty!")
        return

    item = item.strip()
    for todo in todo_list:
        if todo['task'].lower() == item.lower():
            print(f"'{item}' already exists in the to-do list.")
            return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    todo_list.append({"task": item, "timestamp": timestamp})
    print(f"Added '{item}' to the to-do list.")

# Function to remove an item from the to-do list
def remove_item(item):
    if not item:
        print("Task cannot be empty!")
        return

    item = item.strip()
    if item.isdigit():
        index = int(item)
        if 1 <= index <= len(todo_list):
            task = todo_list[index-1]['task']
            todo_list.pop(index-1)
            print(f"Removed '{task}' from the to-do list.")
            return
        else:
            print("Invalid index. Please enter a valid index number.")
            return

    for todo in todo_list:
        if todo['task'].lower() == item.lower():
            todo_list.remove(todo)
            print(f"Removed '{item}' from the to-do list.")
            return

    print(f"'{item}' is not in the to-do list.")

# Main program loop
while True:
    print("1. Display to-do list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear the list")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_list()
    elif choice == "2":
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == "3":
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == "4":
        todo_list.clear()
        print("Your to-do list has been cleared.")
    elif choice == "5":
        print
