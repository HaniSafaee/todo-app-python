-- Create the database (optional)
CREATE DATABASE IF NOT EXISTS todo_app;
USE todo_app;

-- Create the tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL
);

-- Insert sample tasks
INSERT INTO tasks (description) VALUES ('Buy groceries');
INSERT INTO tasks (description) VALUES ('Finish Python project');
INSERT INTO tasks (description) VALUES ('Go to Gym');
