import os

FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILE, "w") as f:
        for t in tasks:
            f.write(t + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Added!")

        elif choice == "3":
            show_tasks(tasks)
            i = int(input("Task number to delete: ")) - 1
            if 0 <= i < len(tasks):
                tasks.pop(i)
                save_tasks(tasks)
                print("Deleted!")
            else:
                print("Invalid number")

        elif choice == "4":
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
