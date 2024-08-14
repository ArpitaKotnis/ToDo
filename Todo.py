Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pickle
... 
... def load_tasks():
...     try:
...         with open('tasks.pkl', 'rb') as file:
...             return pickle.load(file)
...     except FileNotFoundError:
...         return []
... 
... def save_tasks(tasks):
...     with open('tasks.pkl', 'wb') as file:
...         pickle.dump(tasks, file)
... 
... def display_tasks(tasks):
...     if not tasks:
...         print("No tasks to display.")
...     else:
...         print("\nYour Tasks:")
...         for idx, task in enumerate(tasks, start=1):
...             print(f"{idx}. {task}")
... 
... def add_task(tasks):
...     task = input("Enter the task: ")
...     tasks.append(task)
...     print("Task added!")
... 
... def remove_task(tasks):
...     display_tasks(tasks)
...     try:
...         task_number = int(input("Enter the task number to remove: "))
...         if 1 <= task_number <= len(tasks):
...             removed_task = tasks.pop(task_number - 1)
...             print(f"Removed task: {removed_task}")
...         else:
...             print("Invalid task number.")
...     except ValueError:
...         print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
