# db.py
# This file handles all database operations for the Todo App

import mysql.connector
from mysql.connector import Error

# Establish connection to the local MySQL database
def get_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="todo_app"
        )
    except Error as e:
        print(f"[ERROR] Could not connect to the database: {e}")
        return None

# Add a task to the database
def add_task(task):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (description) VALUES (%s)", (task,))
            conn.commit()
            print(f"Task added: {task}")
        except Error as e:
            print(f"[ERROR] Failed to add task: {e}")
        finally:
            conn.close()

# List all tasks in the database
def list_tasks():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, description FROM tasks")
            results = cursor.fetchall()
            if not results:
                print("No tasks found.")
            else:
                print("Tasks:")
                for i, (task_id, description) in enumerate(results, 1):
                    print(f"{i}. {description}")
        except Error as e:
            print(f"[ERROR] Failed to retrieve tasks: {e}")
        finally:
            conn.close()

# Delete a task based on the user's input number (not DB ID)
def delete_task_by_number(task_number):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, description FROM tasks")
            results = cursor.fetchall()

            # Check if task number is valid
            if 0 < task_number <= len(results):
                task_id, task_desc = results[task_number - 1]
                cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
                conn.commit()
                print(f'Task {task_number} deleted: "{task_desc}"')
            else:
                print("Invalid task number.")
        except Error as e:
            print(f"[ERROR] Failed to delete task: {e}")
        finally:
            conn.close()
