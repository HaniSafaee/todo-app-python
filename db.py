# db.py

import mysql.connector
from mysql.connector import Error

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

def delete_task_by_number(task_number):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, description FROM tasks")
            results = cursor.fetchall()
            if 0 < task_number <= len(results):
                task_id, task_desc = results[task_number - 1]
                cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
                conn.commit()
                print(f'Task deleted: "{task_desc}"')
            else:
                print("Invalid task number.")
        except Error as e:
            print(f"[ERROR] Failed to delete task: {e}")
        finally:
            conn.close()
