# todo-app-python

A simple command-line to-do list application built with Python and MySQL.

##  Features

- Add new tasks  
- View all tasks (with numbering)  
- Delete tasks by number  
- Persistent storage using MySQL  
- Designed to run locally using WAMP/XAMPP or any MySQL setup  

##  Requirements

- Python 3.10+ (tested with 3.13.3)  
- MySQL (WAMP, XAMPP, or standalone)  
- mysql-connector-python  

##  Setup & Installation

### 1. Install required Python packages

Using requirements.txt:  
`pip install -r requirements.txt`

Or manually:  
`pip install mysql-connector-python`

### 2. Database Setup

**Option A: Using phpMyAdmin**  
- Open: http://localhost/phpmyadmin  
- Go to the SQL tab  
- Paste the contents of `db_export.sql`  
- Click Go  

**Option B: Using Command Line**  
`mysql -u root -p < db_export.sql`  

> This will create the `todo_app` database and populate it with sample tasks.

##  Run the App

`python main.py`

##  Project Structure

todo-app-python/  
├── main.py              # Main CLI logic  
├── db.py                # Database interaction functions  
├── db_export.sql        # SQL file to create/populate database  
├── requirements.txt     # Python dependencies  
└── README.md            # Project instructions  

##  Notes

- This project is built for local use and educational/demo purposes  
- Works well as a beginner-friendly backend/CLI example  

##  Author

Hani Safaee Khosbani  
hani.safaee1993@gmail.com  
https://github.com/HaniSafaee
