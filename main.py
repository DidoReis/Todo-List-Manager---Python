import psycopg2



# Database configuration
DB_NAME = "todo_db"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

def create_table():
    """Create the task table if it doesn't exist"""
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    cur.execute(
        """
       CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            description TEXT NOT NULL
        )"""
    )

    conn.commit()
    cur.close()
    conn.close()

def add_task(description):
    """Add a new task to the database"""
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    cur.execute("INSERT INTO tasks (description) VALUES (%s)", (description,))

    conn.commit()
    cur.close()
    conn.close()

def view_tasks():
    """View all task in the database"""
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    
    cur = conn.cursor()

    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()

    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            print(f"{task[0]}. {task[1]}")

    cur.close()
    conn.close()

def delete_task(task_id):
    """Delete a task from the database"""
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    cur = conn.cursor()

    cur.execute("DELETE FROM tasks WHERE id= %s", (task_id,))

    if cur.rowcount == 0:
        print("Task not found.")
    else:
        print("Tasks deleted successfully.")

    conn.commit()
    cur.close()
    conn.close()

def show_menu():
        """SHOW the menu options"""
        print("\nTodo List Manager")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

def main():
    create_table()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-4):")

        if choice == '1':
            description = input("Enter task description:")
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == "3":
            task_id = input("Enter task ID to delete:")
            delete_task(task_id)
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try Again")

if __name__ =="__main__":
    main()