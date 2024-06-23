##  TO-DO-LIST

def todolist():
    tasks = []

    while True:
        print("***** To-Do-list *****")
        print("1- for add task ")
        print("2- for show task ")
        print("3- for check the task as done")
        print("4- for Exit ")

        num = (input("please enter the number : "))
        if num == "1":
            # print()
            add = int(input("how many task you want to add: "))

            for i in range(add):
                task = input("enter the task: ")
                tasks.append({"task":task,"Done": False})    
                print("Task added")

        elif num == "2":
            print("\nTasks:") 
            for index,task in enumerate(tasks):
                status = "Done" if task["Done"] else "Not Done"
                print(f"{index+1}. {task["task"]} - {status}")      

        elif num == "3":
            task_ind = int(input("Enter the task number to mark as Done : "))
            if 0 <= task_ind < len(tasks):
                tasks[task_ind]["Done"] = True
                print("Task checked as Done ")
            else:
                print("enter the valid number")  

        elif num =="4":
            print("Exiting to the To-Do-list..") 
            break
        else:
            print("you may enter a invalid number..")
            print("please try again!") 

todolist()                

   
   
