# =========================================== Variables =============================================

tasks = []
completedTasks = []

# ?==================================================================================================


#! =========================================== Functions =============================================
def Main():
    message = "1- Add Task\n2- View All Tasks\n3- Mark Task To Complete\n4- View Tasks That Completed\n5- Quit"

    while True:
        print(message)
        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_all_tasks()

        elif choice == "3":
            mark_to_complete()

        elif choice == "4":
            view_tasks_That_completed()

        elif choice == "5":
            break

        else:
            print("Invalid Choice!, Please Enter A Valid Choice")

        print("_" * 60 + "\n")


def add_task():
    task = input("Enter Task You Want To Add It: ").strip().capitalize()
    tasks.append(task)
    print("Your Task Is Added Successfully. 👌")


def view_all_tasks():
    print("Your Tasks: 📝")
    z = 1
    while z <= len(tasks):
        print(f"{z}- {tasks[z - 1]} ❌")
        z += 1


def mark_to_complete():
    if len(tasks) < 1:
        print("No Tasks To Mark It Completed! ⁉️, Please Add Task And Try To Mark It.")
    else:
        x = 1
        while x <= len(tasks):
            print(f"{x}- {tasks[x - 1]}")
            x += 1

    task = int(input("Enter Number Of Task You Want To Mark It Done: ").strip())
    completedTasks.append(tasks[task - 1])
    tasks.remove(tasks[task - 1])
    print("Your Task Is Completed, Keep Going. ✅🎊✨👏")


def view_tasks_That_completed():
    if completedTasks == False:
        print("No Tasks Completed To View! ⁉️, Please Mark Task Completed First.")

    else:
        print("Your Tasks That Is Completed: 👏😎")
        z = 1
        for element in completedTasks:
            print(f"{z}- {element}")
            z += 1

        if len(completedTasks) >= 3:
            print("That Is Very Good, Keep Going. 👏😉")


# ? ===================================================================================================

#! =========================================== Main Logic =============================================

Main()

# ?==================================================================================================
