# main.py

from db import add_task, list_tasks, delete_task

def main():
    while True:
        print("\nTodo App")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_to_delete = input("Enter task to delete: ")
            delete_task(task_to_delete)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
