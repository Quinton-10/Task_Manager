# Task_Manager
when the programme starts a log in screen will appear if the user name and password is in the text file user.txt the user will be able to log in else an error message will appear for them to try again.  
When a user is logged in with user name admin a specific menu will pop:
* r- register user
* a - add task  
* va- view all
* vm - view mine
* gr - generate report
* s - stats
* e - exit

If user enters "r" they are able to register a new user and it will save the new username and password to user.txt file but if the username they select has already been taken a message will pop to say user name has been taken please select another one.  
If the user enters "a" the programme will ask the user to input and after user input the new task will be saved to tasks.txt file.

if user enters "va" they will be able to view all tasks that are saved in tasks.txt file in a readable format.

if user enters "vm" they wil be able to see all their task number and the programme asks the user to input the task number they would like to view, when they type in a number that specific task will be displayed in a readable manner then a menu will pop up where they can either:
* mark the task as complete 
* mark the task as incomplete
* change the due date
* change the username
* -1 to exit 
what ever the user chooses the changes will be saved to the necessary text file and if user enters "-1" it will take them back to the main menu

If the user enters "gr" it will generate a report in two text file task_overview.txt and user_overview.txt.

in task_overview.txt it will show :  
*  The total number of tasks that have been generated and tracked using the ​task_manager.py​.   
*  The total number of completed tasks.   
*  The total number of uncompleted tasks.   
*  The total number of tasks that haven’t been completed and that are overdue.    
*  The percentage of tasks that are incomplete.   
*  The percentage of tasks that are overdue.


In user_overview.txt it will show :  
*  The total number of users registered with ​task_manager.py​.   
*  The total number of tasks that have been generated and tracked using the ​task_manager.py​.   
*  For each user also describe:   
*  The total number of tasks assigned to that user.   
*  What percentage of the total number of tasks have been assigned to that user?   
*  What percentage of the tasks assigned to that user have been completed?   
*  What percentage of the tasks assigned to that user must still be completed?   
*  What percentage of the tasks assigned to that user have not yet been completed and are overdue? 

If user enters "s" the total amount of tasks and total amount of users will be displayed in a readable manner.

If user enters "e" the programme stops.

If user name is not admin the this menu will be displayed:  
* va - view all
* vm - view mine 
* a - add task
* e - exit 
And will do the same as mentioned above.
