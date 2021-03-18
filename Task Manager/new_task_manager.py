import datetime

#open file
file = open("user.txt", "r")
task_file= open("tasks.txt", "r+")
               
            
    
            
def overview_user():
    file=open("user.txt", "r")
    
    task_file= open("tasks.txt", "r")
    total_user=0
    total= 0
#counts the total amount of users
    for line in file:
        line=line.strip("\n")
        total_user+= 1
    
#count the total amount of tasks     
    for line in task_file:
        line=line.strip("\n")
        total+= 1
    
    
    
    
    
    task_file= open("tasks.txt", "r")
    file = open("user.txt", "r")
    user_overview= open("user_overview.txt", "w")
    user_overview.write(f"\nTotal amount of users: {total_user}")
    user_overview.write(f"\nTotal amount of generated task: {total}\n")
    for line in file:
        valid_user, valid_pass= line.strip("\n").split(", ")
        count=0
        i=0
        p=0
        j=0
        
        
        for line in task_file:
            name, task, discription, start_date, due_date, complete=line.strip("\n").split(", ")
            
            if valid_user == name:
                #if valid user and name are the same it will count how many task that user has
                count+=1
                #calculate percentage of tasks the user has
                per_tasks= 100*count/total
                if complete == "yes":
                    i+=1
                devide= i / count
                #calculate the percentage of completed tasks for that user
                complete_per= devide * 100
                if complete == "no":
                    p+=1
                d= p / count
                #calculate the percentage of incompleted tasks
                incom= d * 100
            
            
                today= datetime.datetime.today()
                if complete == "no" and datetime.datetime.strptime(due_date, "%Y-%m-%d") < today:
                    j+=1
                z= j / count
                #calculates the precentage of incompleted overdue tasks
                overdue_per= z * 100
        #writes all results to new output file
        user_overview.write(f"\nUser: {valid_user}")
        user_overview.write(f"\nPersentage of tasks assigned to user: {per_tasks}")
        user_overview.write(f"\nPersentage of assigned tasks completed: {complete_per}")
        user_overview.write(f"\nPersentage of assigned tasks incompleted: {incom}")
        user_overview.write(f"\nPersentage of incompleted overdue tasks: {overdue_per}\n") 
        
    
       
        task_file.seek(0)
    print("Report generated please see text files")
    user_overview.close()
        
        
    

    
            
        
   
        

    
    
        

        





        
    
def date():
    overview_file= open("task_overview.txt.", "a")
   
    amount= 0
    overdue= 0
    today= datetime.datetime.today()
    #using the datetime module to check if there are any overdue tasks and counts all overdue tasks
    with open("tasks.txt") as f:
        
        for line in task_file:
            name, task, discription, start_date, due_date, complete =line.split(", ")
            if datetime.datetime.strptime(due_date, "%Y-%m-%d") < today:
                overdue+=1
        overview_file.write(f"\nThe amount of overdue: {overdue}")
    #calculates the percentage of overdue tasks    
    file=open("tasks.txt", "r")
    for line in file:
        line=line.strip("\n")
        amount+= 1
    overdue_per= 100*overdue/amount
    overview_file.write(f"\nThe persentage of overdue task are: {overdue_per}%")    
    overview_file.close()
    
def generate():
    overview_file= open("task_overview.txt.", "w")
    task_file= open("tasks.txt", "r")
    total_task = 0
    #calculates all number of task generated
    for line in task_file:
        line=line.strip("\n")
        total_task+= 1
    overview_file.write(f"The total number of tasks is: {total_task}")
    

    with open("tasks.txt") as f:
        #find the number of completed and incompleted task and writes it to a text file
        data= f.read()
        occurrences= data.count("yes")
        no_shows= data.count("no")
        overview_file.write(f"\nThe number of completed tasks are: {occurrences}")
        overview_file.write(f"\nThe number of tasks not completed are: {no_shows}")

    #calculate the percentage of incompleted tasks    
    per_incomplete= 100*no_shows/total_task
    overview_file.write(f"\nThe persentage of incomplete tasks are: {per_incomplete}%")
    overview_file.close()
    task_file.close()
    
        
    
    

            
def reg_user():
    #lets admin register new users and also check if the new username has already been taken
    reg=True
    while reg == True:
        with open("user.txt") as file:
            new_user = input("Please enter new username: ")
            new_password = input("Please enter password for new user: ")
            if new_user in file.read():
                print("Username already taken")
                file.close()
            else:
                file= open("user.txt", "a+")
                confirm=input("please confirm password")
                if confirm==new_password:
                    reg= False
                    file.write(f"\n{new_user}, {new_password}")
                else:
                    print("Passwords do not match")
           
                file.close()
    
    
   
    
        

def add_task():
    #users can be able to add a new task 
    task_file= open("tasks.txt", "a+")
        #name,title,descrip,start, end ,no
    name=input("Please enter username for person resposible for this task: ")
    task=input("Enter the type f task: ")
    description=input("Enter the description of the task: ")
    start_date=input("Enter Todays date: ")
    due_date= input("Enter the due date for the task: ")
    complete=input("is the task completed?(Yes or No): ")
            
            

    task_file.write(f"\n{name}, {task}, {description}, {start_date}, {due_date}, {complete}")
    task_file.close()

def view_all():
    #lets user view all the tasks
    task_file= open("tasks.txt", "r+")
    for line in task_file:
        name, task, discription, start_date, due_date, complete =line.split(", ")

        print(f"""
            name= {name}
    Type of task= {task}
     Discription= {discription}
      Start Date= {start_date}
        Due Date= {due_date}
is Task complete= {complete}
                """)

         
    task_file.close()


def view_mine():
    #lets user view their task and edit it
    with open("tasks.txt") as task_file:
        for num, line in enumerate(task_file, 1):
            if username in line:
                print("Your task numbers are below:")
                print(num)
    user_num=int(input("Enter the task number you would like to view: "))
    task_file= open("tasks.txt", "r")
    user_task=task_file.readlines(user_num)
    user_task=", ".join(user_task)
    for i in user_task:
        name, task, discription, start_date, due_date, complete=user_task.split(", ")
    print(f"""
                name= {name}
        Type of task= {task}
         Discription= {discription}
          Start Date= {start_date}
            Due Date= {due_date}
    is Task complete= {complete}
                    """)
    
    choose= input("""What would you like to do:
    a- mark this task as completed
    b- mark this task as incompleted
    c- change the Due date
    d- change the username
    -1 - to exit
    """)

    if choose== "a":
        #changes an incomplete task to completed
        for complete in name, task, discription, start_date, due_date, complete:
             new_complete=complete.replace("no", "yes")
        task_file= open("tasks.txt", "r")
        lines=task_file.readlines()
        index= user_num - 1
        lines[index]=f"{name}, {task}, {discription}, {start_date}, {due_date}, {new_complete}"
        task_file= open("tasks.txt", "w")
        task_file.writelines(lines)
        task_file.close()
        print("Changes have been made")
        
    if choose == "b":
        #changes a completed task to incomplete
        for complete in name, task, discription, start_date, due_date, complete:
             new_complete=complete.replace("yes", "no")
        task_file= open("tasks.txt", "r")
        lines=task_file.readlines()
        index= user_num - 1
        lines[index]=f"{name}, {task}, {discription}, {start_date}, {due_date}, {new_complete}"
        task_file= open("tasks.txt", "w")
        task_file.writelines(lines)
        task_file.close()
        print("Changes have been made")

    if choose == "c":
        #lets user change the due date of a task
        new_date=input("Enter new due date(yyyy-mm-dd): ")
        for due_date in name, task, discription, start_date, due_date, complete:
             new_due_date=due_date.replace(due_date, new_date)
        task_file= open("tasks.txt", "r")
        lines=task_file.readlines()
        index= user_num - 1
        print(index)
        lines[index]=f"{name}, {task}, {discription}, {start_date}, {new_due_date}, {complete}"
        task_file= open("tasks.txt", "w")
        task_file.writelines(lines)
        task_file.close()
        print("Changes have been made")
        
    if choose == "d":
        #lets user change the username on a task
        new_username= input("Enter new username here: ")
        for name in name, task, discription, start_date, due_date, complete:
             new_name=name.replace(name, new_username)
        task_file= open("tasks.txt", "r")
        lines=task_file.readlines()
        index= user_num - 1
        print(index)
        lines[index]=f"{new_name}, {task}, {discription}, {start_date}, {due_date}, {complete}"
        task_file= open("tasks.txt", "w")
        task_file.writelines(lines)
        task_file.close()
        print("Changes have been made")
        
    if choose == "-1":
        #if user enters -1 it will take them back to the main menu
        if username== "admin":
            option = input("""
    Please select one of the following options:
     r - register user
     a - add task
    va - view all tasks
    vm - view my tasks
     s - stats
     e - exit
     : """)

            if option == "r":
                reg_user()
            if option == "a":
                add_task()
            if option == "va":
                view_all()
            if option == "vm":
                view_mine()
            if option == "s":
                stats()
            elif option == "e":
                exit
            else:
                print("Not a valid option")
        else:
            option = input("""
    Please select one of the following options:

     a - add task
    va - view all tasks
    vm - view my tasks
     e - exit
     : """)
            if option == "a":
                add_task()
            if option == "va":
                view_all()
            if option == "vm":
                view_mine()
            elif option == "e":
                exit
    else:
        print("Not a valid option")
                 
    
       
           
    
        
    

    
    
            
                
       

def stats():
    #print the stats for admin only
    task_file= open("tasks.txt", "r+")
    file= open("user.txt", "r+")
    total_task=0
    total_user=0
    for line in task_file:
        line=line.strip("\n")
        total_task+= 1
    print(f"Total Tasks: {total_task}")

    for line in file:
        line=line.strip("\n")
        total_user+= 1
    print(f"Total users: {total_user}")
#use while to ask user to input username and password if username and password is in txt file user will log in else error message to try again
login = False
while login == False:
    username=input("Please enter your Username: ")
    password=input("Please enter your Password: ")


    for line in file:
        valid_user, valid_password= line.strip("\n").split(", ")
    
        if username== valid_user and password== valid_password:
            login = True
        
    if login == False:
        print("Not valid username or password please try again")
            

        file.seek(0)
    
file.close()


#If users username is admin a menu only they can use will pop up
if username== "admin":

#Ask user to input one of the options in the menu
    option = input("""
    Please select one of the following options:
     r - register user
     a - add task
    va - view all tasks
    vm - view my tasks
    gr - generate reports
     s - stats
     e - exit
     : """)

#if user inputs r they can regiter a new user
    if option == "r":
       reg_user()

#if user input a they can add a new task            
    elif option == "a":
        add_task()
        

#if user input va they can view all the tasks in a readable format
    elif option == "va":
       view_all()

#if user enters vm they can view tasks which is assigned to their user name
    elif option == "vm":
        view_mine()
        

#If user inputs s they can see the total tasks and total users
    elif option == "s":
        stats()
#if user inputs gr it will generate a report in a text file 
    elif option == "gr":
        generate()
        date()
        overview_user()
        
        
#if user enters e they exit            
    elif option == "e":
        exit
#if they dont pick any or something else error message will pop up
    else:
        print("Not a valid option")

        
#if user is not admin this menu will pop up
else:
    option = input("""
    Please select one of the following options:

     a - add task
    va - view all tasks
    vm - view my tasks
     e - exit
     : """)
     

    if option == "a":
        add_task()
        
    elif option == "va":
        view_all()        
        
    elif option == "vm":
            view_mine()       


    elif option == "e":
        exit

    else:
        print("Not a valid option")
