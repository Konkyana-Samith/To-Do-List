# To-Do List Manager

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task(description, priority):
    task = {"description": description, "priority": priority}
    tasks.append(task)
    print(f"Task '{description}' with {priority} priority added!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task['description']} (Priority: {task['priority']})")

# Function to remove a task
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task['description']}' removed!")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        description = input("Enter task description: ")
        priority = input("Enter priority (High/Medium/Low): ").capitalize()
        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Please enter High, Medium, or Low.")
        else:
            add_task(description, priority)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        try:
            task_num = int(input("Enter task number to remove: "))
            remove_task(task_num)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "4":
        print("Thank you for using To-Do List Manager!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")