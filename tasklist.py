import json
from datetime import datetime, timedelta

TASK_FILE = "tasks_db.json"

def read_tasks():
    tasks = []
    try:
        with open(TASK_FILE, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        pass
    return tasks

def write_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def showtasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. '{t['title']}'\nPriority: {t['priority']}\nDue Date: {t['due_date']}\nCompleted: {t['completed']}\n")

def addtask(tasks):
    title = input("Enter task title: ")
    priority = input("Priority? (high/medium/low): ")
    due_date_str = input("Due date? (DD/MM/YYYY): ")
    try:
        due_date = datetime.strptime(due_date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Use DD/MM/YYYY.")
        return 
    tasks.append({
        "title": title,
        "priority": priority,
        "due_date": due_date_str,
        "completed": False
    })
    print("Task added.")

def removetask(tasks):
    showtasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Removed task: '{removed_task['title']}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def marktaskcompleted(tasks):
    showtasks(tasks)
    try:
        index = int(input("Task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print(f"Marked task '{tasks[index]['title']}' as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def main():
    tasks = read_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Pick your poison (1-5): ")

        if choice == "1":
            showtasks(tasks)
        elif choice == "2":
            addtask(tasks)
        elif choice == "3":
            removetask(tasks)
        elif choice == "4":
            marktaskcompleted(tasks)
        elif choice == "5":
            write_tasks(tasks)
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
