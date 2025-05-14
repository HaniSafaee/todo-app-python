# db.py

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
