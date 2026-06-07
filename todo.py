import sqlite3

# 1. Connect to the database file (creates 'todo.db' automatically)
connection = sqlite3.connect("todo.db")
cursor = connection.cursor()

# 2. Create a clean database structure if it doesn't exist yet
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
""")
connection.commit()

print("--- 🐹 Database To-Do App ---")

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")  # <-- Added back!
    print("4. Exit")         # <-- Bumped down to 4
    
    choice = input("\nChoose an option (1-4): ")
    
    
    if choice == "1":
        # Pull rows out of the structured table
        cursor.execute("SELECT id, title FROM tasks")
        all_tasks = cursor.fetchall()
        
        print("\n--- Your Current Tasks ---")
        if not all_tasks:
            print("Your database is completely empty!")
        else:
            for row in all_tasks:
                print(f"[{row[0]}] {row[1]}")
                
    elif choice == "2":
        # Insert a brand new record into the database table
        new_task = input("Enter your task: ")
        
        if new_task.strip() != "":
            cursor.execute("INSERT INTO tasks (title) VALUES (?)", (new_task,))
            connection.commit()
            print(f"✅ Saved to database: '{new_task}'")
        else:
            print("❌ Task cannot be empty!")
            
    elif choice == "3":
        # 1. Fetch current tasks so the user knows what IDs exist
        cursor.execute("SELECT id, title FROM tasks")
        all_tasks = cursor.fetchall()
        
        print("\n--- Select a Task ID to Delete ---")
        if not all_tasks:
            print("There are no tasks to delete.")
        else:
            for row in all_tasks:
                print(f"[{row[0]}] {row[1]}")
            
            try:
                # 2. Ask the user for the structural ID number
                task_id = int(input("\nEnter the exact ID number to remove: "))
                
                # 3. Check if that ID actually exists in our database table
                cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
                if cursor.fetchone() is None:
                    print("❌ That ID number does not exist!")
                else:
                    # 4. Execute the SQL command to target and delete that exact row
                    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
                    connection.commit()
                    print(f"🗑️ Task ID [{task_id}] successfully deleted from the database!")
                    
            except ValueError:
                print("❌ Please type a valid number, not letters!")

    elif choice == "4":
            print("\nClosing database connection. Goodbye!")
            connection.close()
            break