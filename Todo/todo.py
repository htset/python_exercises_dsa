from todo_list import TodoList

if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Sort Tasks by Priority")
        print("0. Exit")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
            if choice == 1:
                description = input("Enter task description: ")
                priority = int(input("Enter priority: "))
                todo_list.add_task(description, priority)
                print("Task added successfully.")
            elif choice == 2:
                index = int(input("Enter number of task to remove: "))
                todo_list.remove_task(index - 1)
                print("Task removed successfully.")
            elif choice == 3:
                print("List of tasks:")
                todo_list.display_tasks()
            elif choice == 4:
                todo_list.sort_tasks()
                print("Tasks sorted by priority.")
            elif choice == 0:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
