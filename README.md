# **Task Manager**

This Program works with four text files:
* user.txt
* tasks.txt
* task_overview.txt
* user_overview.txt

tasks.txt stores a list of all the tasks that the team will be working on
user.txt stores the username and password for each user that has permission to use the program

##The Program allows the users to do the following:

*1. Login. The user should be prompted to enter a username and password. A menu is displayed after a successful login.

      r  - register user
  
      a  - add task
  
      va - view all tasks
  
      vm - view my tasks
  
      gr - generate reports
  
      ds - display statistics
  
      e  - exit
  

*2. If the user chooses ‘r’ to register a user, the user should be prompted for a new username and password.

  Only the user with the username ‘admin’ is allowed to register users.
  The admin user is provided with a menu option that allows them to display statistics


*3. If the user chooses ‘a’ to add a task, the user should be prompted to enter the username of the person the task is assigned to, the title of
the task, a description of the task and the due date of the task.

  If a user tries to add a username that already exists in user.txt , an error message displays
  and allows them to try to add a user with a different username.


*4. If the user chooses ‘va’ to view all tasks, display the information for each task on the screen in an easy to read format.


*5. If the user chooses ‘vm’ to view the tasks that are assigned to them, only display all the tasks that have been assigned to the user that is
currently logged-in in a user-friendly, easy to read manner.

  Each task is displayed with a corresponding number which can be used to identify the task.

  The user selects either a specific task by entering a number or input ‘-1’ to return to the main menu.

  If the user selects a specific task, they should be able to choose to either mark the task as complete or edit the task.
  The task can only be edited if it has not yet been completed.


*6. If the user chooses ‘gr’ to generate reports, two text files, called task_overview.txt and user_overview.txt, should be generated. Both
these text files should output data in a user-friendly, easy to read manner.

task_overview.txt contains:
* The total number of tasks that have been generated and tracked using the task_manager.py .
* The total number of completed tasks.
* The total number of uncompleted tasks.
* The total number of tasks that haven’t been completed and
that are overdue.
* The percentage of tasks that are incomplete.
* The percentage of tasks that are overdue.

user_overview.txt contains:
* The total number of users registered with task_manager.py .
* The total number of tasks that have been generated and tracked using the task_manager.py .
* For each user also describe:
* The total number of tasks assigned to that user.
* The percentage of the total number of tasks have been assigned to that user.
* The percentage of the tasks assigned to that user have been completed.
* The percentage of the tasks assigned to that user must still be completed.
* The percentage of the tasks assigned to that user have not yet been completed and are overdue.


7. If the user chooses 'ds', the reports generated are read from task_overview.txt and user_overview.txt and displayed on the screen in a user-friendly manner.
