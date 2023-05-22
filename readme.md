# Todo List Manager

A command-line todo list manager where users can add, view, and delete tasks.

## Features

- Add tasks with descriptions
- View all tasks
- Delete tasks by ID

## Requirements

- Python 3.x
- PostgreSQL
- psycopg2

## Installation

1. Clone the repository:

```shell
git clone https://github.com/your-username/todo-list-manager.git

Navigate to the project directory:

cd todo-list-manager

Install the required dependencies:
pip install -r requirements.txt

Create a PostgreSQL database for the todo list manager.

Create a .env file in the project directory and provide the necessary database credentials. Here's an example:

DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

Run the todo list manager:

python todo_manager.py
Usage
Add a task: Select option 1 from the menu and enter the task description when prompted.

View tasks: Select option 2 from the menu to display all tasks.

Delete a task: Select option 3 from the menu and enter the ID of the task you want to delete.

Exit: Select option 4 from the menu to exit the program.

Contributing
Contributions are welcome! If you find any issues or want to suggest enhancements, please create a new issue or submit a pull request.

License
This project is licensed under the MIT License.



Feel free to customize this template to include more specific information about your todo list manager or add any additional sections as needed.



