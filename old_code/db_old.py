# db.py


import mysql.connector


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


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="todo_app"
    )           

def add_task(description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (%s)", (description,))
    conn.commit()
    conn.close()

def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, description FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks
