# main.py

from db import tasks, add_task, list_tasks

def main():
    while True:
        print("\nTodo App")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
