# main.py

from db import add_task, list_tasks, delete_task_by_number

def main():
    while True:
        print("\nTodo App")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                task_num = int(input("Enter task number to delete: "))
                delete_task_by_number(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
