taskList = []

def show_menu():
    print("\n------To-do list--------")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def addTask():
    task = input("Enter a task: ")
    taskList.append({"task": task, "completed": False})
    print("✅ Task added!")

def viewTasks():
    if len(taskList) > 0:
        print("Your tasks:")
        for index, task in enumerate(taskList, start=1):
            status = "✘"
            if task["completed"]:
                status = "✔" 
            print(f"{index}. {task["task"]} {status}")
    else:
        print("No tasks!")

def markCompleted():
    viewTasks()
    if len(taskList) > 0:
        markTask = int(input("\nEnter task number to be marked as completed: "))
        taskList[markTask-1]["completed"] = True
        # del taskList[markTask-1]
        print("✅ Task marked as completed.")

def deleteTask():
    viewTasks()
    if len(taskList) > 0:
        deleteTask = int(input("\nEnter task number to be deleted: "))
        del taskList[deleteTask-1]
        print("✅ Task deleted!")

while True: # Infinite loop
    show_menu()
    user_choice = int(input("\nChoose an option (1-5): "))

    match user_choice:
        case 1:
            addTask()
        case 2:
            viewTasks()
        case 3:
            markCompleted()
        case 4:
            deleteTask()
        case 5:
            print("Goodbye!")
            break # Exit the loop if the choice is 5
        case _:
            print("Invalid choice! Please try again.")