# project_Task-1

# Simple To-Do List

    A basic Python console application to manage a to-do list. The program allows users to add items, view the list, mark items as done, and remove items from the list.

## Features

     - **Add To-Do Item**: Add a new item to the to-do list.
     - **View To-Do List**: View all the items currently in the to-do list.
     - **Mark Item as Done**: Mark an item as done, which removes it from the list.
     - **Remove Item**: Remove an item from the list.
     - **Exit**: Exit the program.

## Getting Started

### Prerequisites

      - Python 3.x

### Installation

1. Clone the repository:
        ```sh
           git clone https://github.com/your-username/simple-todo-list.git
        ```

2. Navigate to the project directory:
        ```sh
          cd simple-todo-list
        ```

3. Run the program:
       ```sh
         python todo_list.py
       ```

## Usage

1. When you run the program, you will see the menu with options:
    ```sh
    ===== To-Do List Menu =====
    1. Add a to-do item
    2. View to-do list
    3. Mark an item as done
    4. Remove an item
    5. Exit
    ```

2. Choose an option by entering the corresponding number.

3. Follow the prompts to add items, view the list, mark items as done, or remove items.

4. Select `5` to exit the program.

## Example

```sh
===== To-Do List Menu =====
1. Add a to-do item
2. View to-do list
3. Mark an item as done
4. Remove an item
5. Exit
Enter your choice: 1
Enter the to-do item: Buy groceries
To-do item added successfully!

===== To-Do List Menu =====
1. Add a to-do item
2. View to-do list
3. Mark an item as done
4. Remove an item
5. Exit
Enter your choice: 2
===== To-Do List =====
1. Buy groceries

===== To-Do List Menu =====
1. Add a to-do item
2. View to-do list
3. Mark an item as done
4. Remove an item
5. Exit
Enter your choice: 3
===== To-Do List =====
1. Buy groceries
Enter the number of the item to mark as done: 1
Marking 'Buy groceries' as done.
