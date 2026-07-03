# #TO-DO-LIST
# tasks = []

# while True : 
#     print("-----TO - DO - LIST------")
#     print("1.Add Tasks")
#     print("2.Show Tasks")
#     print("3.Exit")

#     choice = int(input("what do you want to do today !"))

#     if choice ==1 : 
#         add_task = input("Enter the task : ")
#         new_task = {
#             "id" : len(tasks) + 1,
#             "add_task" : add_task,
#             "status" : "pending"
#         }
#         tasks.append(new_task)
#         print("task added successfully")

#     elif choice == 2 :
#         if len(tasks) == 0 :
#             print("No task available")
#         else :
#             print("\n ----- your work----")
#             for i , kaam in enumerate(tasks,1):
#                 print(f"{kaam['id']}. {kaam['add_task']}")
#     elif choice == 3 :
#         print("sayonara")
#         break
#     else :
#         print("please enter a valid input!!!")

#updated code.................................................. TO-DO-LIST


    # 1. ADD TASK
def add_task():
        add_task = input("Enter the task: ")
        tasks.append(add_task)
        status.append("Pending")  # Every new task starts as Pending
        print("Task added successfully!")
    # 2. SHOW TASKS
def show_task():
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n----- Your Work -----")
            # enumerate(tasks, 1) gives us the index numbers starting from 1
            for i, kaam in enumerate(tasks, 1):
                # i-1 gets the matching index for the status list
                print(f"{i}. [{status[i-1]}] {kaam}")
    # 3. UPDATE TASK
def update_task():
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            task_num = int(input("Enter the task number to edit: "))
            new_name = input("Enter the new task name: ")
            tasks[task_num - 1] = new_name  # Update the text at that position
            print("Task updated!")
    # 4. TASK STATUS
def task_status():
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            task_num = int(input("Enter the task number to mark completed: "))
            status[task_num - 1] = "Completed"  # Change status at that position
            print("Status updated to Completed!")
    # 5. DELETE TASK
def delete_task():
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            task_num = int(input("Enter the task number to delete: "))
            # pop() removes the item at that specific index number
            tasks.pop(task_num - 1)
            status.pop(task_num - 1)  # Remove its status too so they stay aligned
            print("Task deleted successfully!")

    # 6. EXIT
def exit():
        print("sayonara")
        

tasks = []
status = []  # A separate list to keep track of status ("Pending" or "Completed")

    
while True:
    print("\n----- TO - DO - LIST ------")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Update Task")
    print("4. Change Status")
    print("5. Delete Task")
    print("6. Exit")

    choice = int(input("What do you want to do today! : "))

    if choice ==1:        
          add_task()
    elif choice <1 and choice >6:
          print("Enter a valid choice !!!")
    elif choice ==2:
          show_task()
    elif choice ==3:
          update_task()
    elif choice ==4:
          task_status()
    elif choice ==5:
          delete_task()
    elif choice ==6:
          exit()
          break


    

