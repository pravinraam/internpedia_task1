class Todo:
    def __init__(self):
        print('Welcome to Console todo List Project')
        print('-'*len('Welcome to Console todo List Project'))
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def mark_task_as_pending(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = False
            print("Task marked as pending.")
        else:
            print("Invalid task index.")

    def edit_task(self, task_index, new_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["task"] = new_task
            print("Task edited successfully.")
        else:
            print("Invalid task index.")

    def show_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task["completed"]]
        if pending_tasks:
            print("Pending Tasks:")
            for index, task in enumerate(pending_tasks, start=1):
                print(f"{index}. {task['task']}")
        else:
            print("No pending tasks.")

    def show_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task["completed"]]
        if completed_tasks:
            print("Completed Tasks:")
            for index, task in enumerate(completed_tasks, start=1):
                print(f"{index}. {task['task']}")
        else:
            print("No completed tasks.")
        
    def show_all_tasks(self):
        if self.tasks:
            print("All Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['task']} - {status}")
        else:
            print("No tasks.")

def main():
    todo_list = Todo()

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Pending")
        print("4. Mark Task as Completed")
        print("5. Edit Task")
        print("6. Show Pending Tasks")
        print("7. Show Completed Tasks")
        print("8. Show All Tasks")
        print("9. Quit")
        print('-'*20)

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print()
            print('-'*20)
        elif choice == '2':
            todo_list.show_pending_tasks()
            todo_list.show_completed_tasks()
            index = int(input("Enter task index to remove: "))
            todo_list.remove_task(index)
            print()
            print('-'*20)
        elif choice == '3':
            todo_list.show_completed_tasks()
            index = int(input("Enter task index to mark as pending: "))
            todo_list.mark_task_as_pending(index)
            print()
            print('-'*20)
        elif choice == '4':
            todo_list.show_pending_tasks()
            index = int(input("Enter task index to mark as completed: "))
            todo_list.complete_task(index)
            print()
            print('-'*20)
        elif choice == '5':
            todo_list.show_pending_tasks()
            todo_list.show_completed_tasks()
            index = int(input("Enter task index to edit: "))
            new_task = input("Enter new task: ")
            todo_list.edit_task(index, new_task)
            print()
            print('-'*20)
        elif choice == '6':
            todo_list.show_pending_tasks()
            print()
            print('-'*20)
        elif choice == '7':
            todo_list.show_completed_tasks()
            print()
            print('-'*20)
        elif choice == '8':
            todo_list.show_all_tasks()
            print()
            print('-'*20)
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
