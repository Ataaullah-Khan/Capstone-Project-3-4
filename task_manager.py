
# Used for date. Thereafter formatted to DD MMM YYY as required.
import datetime
today = datetime.date.today().strftime("%d %b %Y")

# Used to convert string dates to date type.
from datetime import datetime


##########################################################################################################################################################################################


def reg_user():
    
    print("register user ")
    print()
    
    username_exists = False

    # Add a username so long as it does not already exist
    while not username_exists:
        new_username = input("Enter a new username: ")

        
        if new_username not in username_list:
            username_exists = True
        else:
            print("Username already exists, Please try again")
            
    
    new_password = input("Enter a new password: ")
    confirm_password = input("Please confirm the password: ")


    # Write to file if password confirmed in the required format.
    if confirm_password == new_password:

        userfile = open("user.txt", "a")
        userfile.write("\n" + new_username + ", " + new_password)
        print("\nUser Added Successfully")
        userfile.close()
        menu()
    else:
        ("Passwords do not match ")
        reg_user()





##########################################################################################################################################################################################


def add_task():    
    print()
    print("Add new task ")
    print()


    # Add task
    new_assigned_user = input("Enter username to assign task to: \t")
    new_task_title = input("Enter task title: \t\t\t")
    new_task_description = input("Enter task description: \t\t")
    new_date_assigned = today
    dateformat_check = False

    # Entering the wrong date format causes errors when generating reports. A loop to check is necessary for human error.
    while not dateformat_check:
        
        new_date_due = input("Enter due date (DD MMM YYYY):\t\t")

        print("Did you eneter the date in the correct format? Eg. 05 AUG 2021 ")

        date_check = input("1 - Yes\n2 - No\n")

        if date_check == "1":
            dateformat_check = True
            break
        if date_check == "2":
            print("Please try again ")
        else:
            print("Invalid entry")


    new_task_complete = "No"


    # Write to file in required format. "a" appends instead of overwriting
    tasksfile = open("tasks.txt", "a")
    tasksfile.write("\n" + new_assigned_user + ", " + new_task_title + ", " + new_task_description + ", " + new_date_assigned + ", " +  new_date_due + ", " +  new_task_complete)
    print()
    print("Task successfully added ")
    tasksfile.close()

    menu()


##########################################################################################################################################################################################


def view_all():
    print()
    print("View all tasks")
    print()

    tasksfile = open("tasks.txt", "r")
        

    # Iterate through the file and print relevant index.
    
    for line in tasksfile:
        data = line.strip("\n").split(", ")


        print("Task: \t\t\t",data[1] )
        print("Assigned to: \t\t",data[0] )
        print("Date assigned: \t\t",data[3] )
        print("Due date: \t\t",data[4] )
        print("Task Complete? \t\t",data[5] )
        print("Task description: \t",data[2] )
        print()
        print()
        

    tasksfile.close()

    go_back = input("Options: \n 1 - Back to main menu ")
    if go_back == "1":
        menu()



##########################################################################################################################################################################################

    
def view_mine():
    print()
    print("View my tasks ")
    print()

    updated_task = []
    updated_taskstring = ""

    tasksfile = open("tasks.txt", "r")

    # Iterate through the file and print relevant index.
    # J is the counter and gives the task number. The task number is depends on which line it is located in the file.
    j = 1
    for line in tasksfile:
        data = line.strip("\n").split(", ")
        
        
        
        if active_username == data[0]:
                
            print(f"Task {j}:\t\t\t",data[1] )
            print("Assigned to: \t\t",data[0] )
            print("Date assigned: \t\t",data[3] )
            print("Due date: \t\t",data[4] )
            print("Task Complete? \t\t",data[5] )
            print("Task description: \t",data[2] )
            print()
            print()
        j+=1
            
        
    tasksfile.close()

   
    # Display options for the tasks the user can carry out    
    task_option = input("Would you like to select a task function or return to the the main menu? \n 1 - Select a task function \n-1 - Return to main menu\n ")    

    if task_option == "-1":
        menu()

    if task_option == "1":

        task_edit = input("\nDo you want to edit the task or mark the task as complete? \n1 - Edit Task \n2 - Mark as Complete \n")


        if task_edit == "1":
            edit_choice = input("Editing options: \n1- Change user \n2- Change due date \n")            


            # Change assigned user
            if edit_choice == "1":      

                task_num =int(input("\nWhich task number would you like to reassign? \n"))                                

                task_file = open("tasks.txt","r")


                # k is the counter. task_num refers to the line in the text file that needs to be changed. During the iteration, only 1 index needs to be changed.
                # The updated task list is created below and the if - else statement only changes 1 list element when the required condition is met.
                # K is incremented for each line iterated to make sure the value on the correct line is changed.
                k = 1
                for lines in task_file:

                    datas = lines.strip("\n").split(", ")

                    if active_username == datas[0] and task_num == k:

                        # If the task has not been completed, proceed with changes. If the task has been completed, display message and return to view my tasks.
                        if datas[5] == "No":
                            reassign = input("Enter username to reassign to: \n")                            
                            datas[0] = reassign
                            updated_task.append(datas)
                            k+=1

                        elif datas[5]== "Yes":                            
                            print("Task has been completed, cannot change user ")
                            view_mine()

                    else:
                        updated_task.append(datas)
                        k+=1

                # Convert to desired string format
                for elements in updated_task:
                    updated_taskstring += elements[0] + ", " + elements[1] + ", " + elements[2] + ", " + elements[3] + ", " +  elements[4] + ", " +  elements[5] + "\n"

                task_file.close()

                # Close the file that was opened only for reading, then reopen the file as write in order to overwrite the entire text file with the new task list.
                task_file = open("tasks.txt","w")
                task_file.write(updated_taskstring)
                task_file.close()
                print(f"\nTask {task_num} user has been changed ")

                view_mine()


            # Change date
            if edit_choice == "2":      

                task_num =int(input("\nWhich task number would you like to change the due date? \n"))                                

                task_file = open("tasks.txt","r")

                # k is the counter. task_num refers to the line in the text file that needs to be changed. During the iteration, only 1 index needs to be changed.
                # The updated task list is created below and the if - else statement only changes 1 list element when the required condition is met
                # K is incremented for each line iterated to make sure the value on the correct line is changed.
                k = 1
                for lines in task_file:
                    datas = lines.strip("\n").split(", ")
                    if active_username == datas[0] and task_num == k:

                        # If the task has not been completed, proceed with changes. If the task has been completed, display message and return to view my tasks.
                        if datas[5]=="No":
                            new_date = input("Enter new due date: (DD MMM YYYY) \n")                            
                            datas[4] = new_date
                            updated_task.append(datas)
                            k+=1

                        elif datas[5] == "Yes":
                            print("Task has been completed, cannot change date ")
                            view_mine()

                    else:
                        updated_task.append(datas)
                        k+=1

                # Convert to desired string format
                for elements in updated_task:
                    updated_taskstring += elements[0] + ", " + elements[1] + ", " + elements[2] + ", " + elements[3] + ", " +  elements[4] + ", " +  elements[5] + "\n"

                task_file.close()


                # close the file that was opened only for reading, then reopen the file as write in order to overwrite the entire text file with the updated task list.
                task_file = open("tasks.txt","w")
                task_file.write(updated_taskstring)
                task_file.close()
                print(f"\nTask {task_num} due date been changed ")

                view_mine()





        # Mark task as complete
        if task_edit == "2":
        
            task_num =int(input("\nWhich task number would you like to mark as complete? \n"))
                
            task_file = open("tasks.txt","r")
            
            
            # k is the counter. task_num refers to the line in the text file that needs to be changed. During the iteration, only 1 index needs to be changed.
            # The updated task list is created below and the if - else statement only changes 1 list element when the required condition is met.
            # K is incremented for each line iterated to make sure the value on the correct line is changed.
            k = 1
            for lines in task_file:                
                datas = lines.strip("\n").split(", ")


                if active_username == datas[0] and task_num == k:

                    # If the task has not been completed, proceed with changes. If the task has been completed, display message and return to view my tasks.
                    if datas[5] == "No":                                        
                        datas[5] = "Yes"
                        updated_task.append(datas)
                        k+=1

                    elif datas[5] == "Yes":
                        print("Task has already been completed ")
                        view_mine()
                    
                else:
                    updated_task.append(datas)
                    k+=1

            # Convert to desired string format
            for elements in updated_task:
                updated_taskstring += elements[0] + ", " + elements[1] + ", " + elements[2] + ", " + elements[3] + ", " +  elements[4] + ", " +  elements[5] + "\n"

            task_file.close()
            

            # close the file that was opened only for reading, then reopen the file as write in order to overwrite the entire text file with the updated task list.
            task_file = open("tasks.txt","w")
            task_file.write(updated_taskstring)
            task_file.close()
            print(f"\nTask {task_num} marked as complete")

            view_mine()
            

    # If incorrect menu choices are entered, start over
    if task_option != "-1" or task_option != "1":
        print("Incorrect input entered, please try again")
        view_mine()

        if task_edit != "1" or task_edit != "2":
            print("Incorrect input entered, please try again")
            view_mine()
        

        
    
##########################################################################################################################################################################################        
            
    

def menu():
    print("Please select one of the following options: ")
    print()
    print("r  - register user ")
    print("a  - add task ")
    print("va - view all tasks ")
    print("vm - view my tasks ")
    

    if active_username == "admin":
        print("gr - generate reports")
        print("ds  - statistics")    # only admin can see these 2

    print("e  - exit ")     
    print()

    menu_option = input("")
    menu_option = menu_option.lower()


    # View all tasks specific to logged in user.
    if menu_option == "vm":
        view_mine()


    # Allows admin to register users. Request username and password.
    if menu_option == "r" and active_username == "admin":
        reg_user()


    # Message displayed when any user other than admin selects "register user"
    if menu_option == "r" and active_username != "admin":
        print("Only admin is allowed to register new users! \n")
        menu()

    # Add task
    if menu_option == "a":
        add_task()


    # View all tasks in a user friendly manner.
    if menu_option == "va":
        view_all()


    # Generate reports
    if menu_option == "gr" and active_username == "admin":
        generate_reports()


    # Even though only admin can see menu option gr, other users can still access gr by entering it in the menu select.
    # This code prevents that from happening
    if menu_option == "gr" and active_username != "admin":
        print("Only admin is allowed to view generate reports! \n")        
        menu()


    # Display statistics. Only for admin
    if menu_option == "ds" and active_username == "admin":
        display_statistics()


    # Even though only admin can see menu option ds, other users can still access ds by entering it in the menu select.
    # This code prevents that from happening
    if menu_option == "ds" and active_username != "admin":
        print("Only admin is allowed to view statistics! \n")        
        menu()


    # Exit program
    if menu_option == "e":
        exit()
        
        
##########################################################################################################################################################################################

def display_statistics():
    
    # Read files and display text.
    userfile = open("user_overview.txt", "r")
    userlines = userfile.readlines()    
    userfile.close()
    
    print("\nUser Overview:\n")
    for line in userlines:
        print(line)

    taskfile = open("task_overview.txt","r")
    tasklines = taskfile.readlines()
    taskfile.close()

    print("\nTask Overview:\n")
    for line in tasklines:
        print(line)

    print()
    menu()
    
    
        







##########################################################################################################################################################################################

def generate_reports():
    

    task_file = open("tasks.txt","r")

    no_task = 0    
    completed_tasks = 0
    incomplete_tasks = 0
    overdue = 0
    user_list = []
    users_totaltasks = {}
    users_completed_tasks = {}
    users_incomplete_tasks = {}
    users_overdue_tasks = {}
    
    
    for line in task_file:
        no_task +=1

        data = line.strip("\n").split(", ")

        if data[5] == "Yes":
            completed_tasks += 1

        if data[5] == "No":
            incomplete_tasks +=1
        

        # Store due date as a date type variable. If current date is greater than due date, the task is overdue.
        dates_due = datetime.strptime(data[4],'%d %b %Y')
        if datetime.today() > dates_due and data[5] == "No":
            overdue += 1

            # Add overdue keys and values to dictionary
            if data[0] in users_overdue_tasks:
                users_overdue_tasks[data[0]] +=1
            elif data[0] not in users_overdue_tasks:
                users_overdue_tasks[data[0]] = 1
            

        # Add users to user list
        if data[0] in user_list:
            user_list.remove(data[0])
        user_list.append(data[0])


        # Dictionary to store users and their number of total tasks
        if data[0] in users_totaltasks:
            users_totaltasks[data[0]] = users_totaltasks[data[0]] + 1

        else:
            users_totaltasks[data[0]] = 1


        # Dictionary to store users and their completed tasks. Initially all tasks are added. If the task is incomplete, deduct 1 from the key value.
        if data[0] in users_completed_tasks:
            users_completed_tasks[data[0]] += 1

        else:
            users_completed_tasks[data[0]]= 1

        if data[5]=="No":
            users_completed_tasks[data[0]] -= 1

        # Dictionary to store users and theie incomplete tasks. Initially all tasks are added. If the task is complete, deduct 1 from the key value.
        if data[0] in users_incomplete_tasks:
            users_incomplete_tasks[data[0]] += 1

        else:
            users_incomplete_tasks[data[0]] = 1

        if data[5] == "Yes":
            users_incomplete_tasks[data[0]] -=1


    task_file.close()

        
        

    # Percentage of incomplete tasks
    perc_incomplete = round(incomplete_tasks / no_task * 100, 2)


    # Percentage of overdue tasks
    perc_overdue = round(overdue / no_task * 100, 2)
    


    user_file = open("user.txt","r")
    for line in user_file:
        data = line.strip("\n").split(", ")


        # We iterate through the user file as there may be usernames that are stored here that are not in the tasks file. If it is in the userlist, remove it and
        # add it again so that the usernames stored are not duplicated. If it is duplicated, it will give an incorrect count of users for the len() function.
        if data[0] in user_list:
            user_list.remove(data[0])
        user_list.append(data[0])

    user_file.close()


    no_user = len(user_list)



    # Percentage Tasks assigned per User
    # Percentages below are calculated and stored in new dictionaries. Username is key and the value is the percentage
    perc_user_assigned = {i: round(users_totaltasks[i] / no_task * 100, 2) for i in users_totaltasks}
    
    
    # Percentage Tasks completed per User
    # Here we divide values from one dictionary to another 
    perc_user_complete = {i: round(users_completed_tasks[i] / users_totaltasks[i] *100, 2) for i in users_totaltasks}
    

    # percentage per user incomplete
    perc_user_incomplete = {i:round(users_incomplete_tasks[i] / users_totaltasks[i] * 100, 2) for i in users_totaltasks}
    

    
    # Percentage per user incomplete and overdue
    perc_user_overdue = {i: round(users_overdue_tasks[i] / users_totaltasks[i] * 100, 2) for i in users_totaltasks}
    


    

    # Required information written to the text file in a user friendly format
    taskoverview = open("task_overview.txt","w+")

    taskoverview.write(f"Number of tasks\t\t\t\t:\t{no_task} \nNumber of completed tasks\t\t:\t{completed_tasks} \nNumber of incomplete tasks\t\t:\t{incomplete_tasks} \nNumber of overdue_tasks\t\t\t:\t{overdue}")

    taskoverview.write(f"\nPercentage of tasks incomplete\t\t:\t{perc_incomplete}% \nPercentage of tasks overdue\t\t:\t{perc_overdue}% ")

    taskoverview.close()

   



    # Required information written to the text file in a user friendly format
    useroverview = open("user_overview.txt","w+")

    useroverview.write(f"Number of users\t\t:\t{no_user} \nNumber of Tasks\t\t:\t{no_task} \n\n")


    # Writing a dictionary via .write(dictionary) will result in unwanted commas, brackets and apostrophies.
    # Instead iterate through the dictionary for "key" and "value" in dictionary.items() and write it in the required user friendly format using f"

    useroverview.write("Number of tasks assigned to each user:\n")
    for key, value in users_totaltasks.items():
        useroverview.write(f"{key} : {value} tasks \n")


    useroverview.write("\nPercentage of tasks assigned per user:\n")
    for key, value in perc_user_assigned.items():
        useroverview.write(f"{key} : {value}% \n")


    useroverview.write("\nPercentage of assigned tasks completed per user:\n")
    for key,value in perc_user_complete.items():
        useroverview.write(f"{key} : {value}% \n")


    useroverview.write("\nPercentage of assigned tasks to complete per user:\n")
    for key, value in perc_user_incomplete.items():
        useroverview.write(f"{key} : {value}% \n")


    useroverview.write("\nPercentage of assigned tasks that are incomplete and overdue per user:\n")
    for key, value in perc_user_overdue.items():
        useroverview.write(f"{key} : {value}% \n")

    

    useroverview.close()

    print("\nReports Genereated\n")

    menu()
        




##########################################################################################################################################################################################    


print("Enter login credentials \n")


# Boolean values to control loop
username_check = False
password_check = False


# Usernames stored in list to check condition. (Valid usernames). 
username_list = []


# Iterate through file and remove \n and split words as required. Added usernames to list.
userfile = open("user.txt", "r+")

for line in userfile:
    data = line.strip("\n").split(", ")
    username_list.append(data[0])
userfile.close()


# Repeatedly ask for username until valid username entered. Checks in username_list.
while not username_check:
    active_username = input("Enter username: \t")

    if active_username not in username_list:
        print()
        print("Username incorrect, please try again")


    # Iterate through file and remove \n and split words as required.
    userfile = open("user.txt", "r+")

    for line in userfile:
        data = line.strip("\n").split(", ")
        

        # if username matches index in text file, exit loop.
        if active_username == data[0]:            
            username_check = True


            # Repeatedly ask for password until valid matching password entered. Checks in adjacent index. (username and password stored next to each other)
            while not password_check:
            
                active_password = input("Enter password: \t")
                if active_password == data[1]:
                    print("")
                    print("Login Successful")
                    password_check = True
                    menu()

                else:
                    print()
                    print("Password incorrect, please try again")                    
            
    userfile.close()






##########################################################################################################################################################################################            
        
# References

# Dave Webb
# Jul 23 '10 at 9:28
# https://stackoverflow.com/questions/3316882/how-do-i-get-a-string-format-of-the-current-date-time-in-python/48779287


# Paulo Blu
# Mar 16 '14 at 19:33
# https://stackoverflow.com/questions/22441803/how-to-write-to-a-file-without-overwriting-current-contents


# RichieHindle
# Oct 15 '10 at 17:42                
# https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python


# ettanany
# Dec 16 '16 at 9:43
# https://stackoverflow.com/questions/41181296/short-date-in-python-dd-mmm-yyyy


# foslock
# Jun 22 '17 at 4:25
# https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python/44689597


# Ataaullah Khan
# 20/02/2021
# task_manager.py
# https://www.dropbox.com/s/827n9qsbpty88jw/task_manager.py?dl=0
















    
