# Define an empty list to store the to-do items
todo_list = []

# Function to display the menu options
def display_menu():
    print("===== To-Do List Menu =====")
    print("1. Add a to-do item")
    print("2. View to-do list")
    print("3. Mark an item as done")
    print("4. Remove an item")
    print("5. Exit")

# Function to add a new to-do item
def add_todo():
    item = input("Enter the to-do item: ")
    todo_list.append(item)
    print("To-do item added successfully!")

# Function to view the current to-do list
def view_todo():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("===== To-Do List =====")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

# Function to mark an item as done
def mark_done():
    view_todo()
    choice = int(input("Enter the number of the item to mark as done: "))
    if 1 <= choice <= len(todo_list):
        print(f"Marking '{todo_list[choice-1]}' as done.")
        del todo_list[choice-1]
    else:
        print("Invalid choice.")

# Function to remove an item from the to-do list
def remove_item():
    view_todo()
    choice = int(input("Enter the number of the item to remove: "))
    if 1 <= choice <= len(todo_list):
        print(f"Removing '{todo_list[choice-1]}'.")
        del todo_list[choice-1]
    else:
        print("Invalid choice.")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_todo()
        elif choice == '2':
            view_todo()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

# Run the main function
if __name__ == "__main__":
    main()
