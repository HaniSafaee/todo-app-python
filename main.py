# main.py
# This is the main entry point for the Todo App (Command Line Interface)

from db import add_task, list_tasks, delete_task_by_number

def main():
    while True:
        # Show menu options to the user
        print("\nTodo App")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            # Option 1: Add a new task
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            # Option 2: List all existing tasks
            list_tasks()
        elif choice == "3":
            # Option 3: Delete a task by its visible number
            try:
                task_num = int(input("Enter task number to delete: "))
                delete_task_by_number(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            # Exit the application
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Ensures main() only runs if this file is executed directly
if __name__ == "__main__":
    main()
