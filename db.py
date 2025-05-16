# db.py

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="todo_app"
    )

def add_task(task):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (%s)", (task,))
    conn.commit()
    conn.close()
    print(f"Task added: {task}")

def list_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, description FROM tasks")
    results = cursor.fetchall()
    conn.close()

    if not results:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, (task_id, description) in enumerate(results, 1):
            print(f"{i}. {description}")