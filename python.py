class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        print("\n--- To-Do List ---")
        for i, task_data in enumerate(self.tasks):
            status = "✓" if task_data["completed"] else " "
            print(f"{i + 1}. [{status}] {task_data['task']}")
        print("------------------")

    def update_task(self, task_index, new_task_description):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["task"] = new_task_description
            print(f"Task {task_index + 1} updated to '{new_task_description}'.")
        else:
            print("Invalid task number.")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Task {task_index + 1} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter the task number to update: ")) - 1
                new_description = input("Enter the new task description: ")
                todo_list.update_task(task_num, new_description)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.complete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '6':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()