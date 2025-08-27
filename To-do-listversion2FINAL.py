# v0.1
# menu login and register frames
# v0.2
# improved looks of login and register Frames
# v0.3
# login and register system successfully NotImplemented
# v0.4
# first version of the main Menu
# v0.5
# used canvas instead of listbox to display tasks as widgets
# v0.6
# first version of display tasks and adding tasks
# v0.7
# can now successfully load in users tasks and save them
# v1
# boundary cases and invalid cases fixed
# v2
# aesthethic improvements


from tkinter import *
import json
from datetime import *

class ToDoList():
    def __init__(self, root): # the main thing that this function does is initializing and creating the container for the other frames.
        self.root = root
        self.checkUser = FALSE
        self.iterate = 0
        self.frameList = []

        self.container = Frame(self.root) # the container
        self.container.grid(row=0, column=0, sticky="nsew")

        self.Frames = {}                  # the dictionary to store all the frames.
        self.Frames["MenuFrame"] = self.MenuFrame()
        self.Frames["LoginFrame"] = self.LoginFrame()
        self.Frames["RegisterFrame"] = self.RegisFrame()
        self.Frames["ToDoListFrame"] = self.todolistFrame()
        self.ShowFrame("MenuFrame")       # we then tell it the frame which will be at the top or the frame that will be showing by using a function.

    def ShowFrame(self, name):            # if this function is called, it will raise the frame which has the name we give to it.
        frame = self.Frames[name]
        frame.tkraise()

    def MenuFrame(self):                  # this is the menu frame which will be before the login frame.
        menuFrame = Frame(self.container, background= "#d2d3db")
        menuFrame.grid(row=0, column=0, sticky="nsew", ipadx=300, ipady=600)

        menuLabel = Label(menuFrame, text="Menu", font=("Corbel", 50), background= "#d2d3db")
        menuLabel.place(x= 170, y=150)

        menuButton = Button(menuFrame, text="Login", command=lambda:self.ShowFrame("LoginFrame"), padx=20, pady=6, background="#fafafa")   # once the login button has been pressed it will call the login frame which was stored in the dictionary.
        menuButton.place(x=220,y=240)                       

        return menuFrame                  # returning the frame so it will be stored in the dictionary.
    
    def LoginFrame(self):                 # the login frame which will be shown when they exit the menu frame after pressing the login button.
        loginFrame = Frame(self.container, background= "#d2d3db")
        loginFrame.grid(row=0, column=0, sticky="nsew", ipadx=300, ipady=600)
        
        loginLabel = Label(loginFrame, text="Login", font=("Corbel", 50, "bold"), wraplength=200, background= "#d2d3db")
        loginLabel.place(x= 160, y=130)                                                 

        loginLabelUser = Label(loginFrame, text= "User:", font=("Corbel", 13), background= "#d2d3db")
        loginLabelUser.place(x=133, y=236)

        self.loginEntryUser = Entry(loginFrame)
        self.loginEntryUser.place(x= 185, y=240)

        loginLabelPassword = Label(loginFrame, text= "Password:", font=("Corbel", 13), background= "#d2d3db")
        loginLabelPassword.place(x=98, y=275)

        self.loginEntryPassword = Entry(loginFrame)
        self.loginEntryPassword.place(x=185, y=280)                                        

        self.loginButton = Button(loginFrame, text="Login", width=10, command=lambda:self.LoginVerif(self.loginEntryUser.get(), self.loginEntryPassword.get()), background="#fafafa")
        self.loginButton.place(x=206, y=320)                                                                                                            # This button will serve as a login button and it works by running the function LoginVerif(variable1(username), variable2(password))

        regismenuButton = Button(loginFrame, text="Register Instead", width=12, command=lambda:self.ShowFrame("RegisterFrame"), background="#fafafa")
        regismenuButton.place(x=200, y=500)                                                                                     # If the user does not yet have an account they will have a register button which will lead them to the register frame where they can create a new account

        self.loginText = Label(loginFrame, text="", background= "#d2d3db")                # This will be a confirmation text which will be utilized by the LoginVerif() function where it will tell the user if the user got the password wrong, if the account they are trying to access does not exist and if they have logged in successfully.
        self.loginText.place(x=204, y=300)
        return loginFrame
    
    def LoginVerif(self, username, password):       # login verification
        successuser = 0
        successpass = 0
        if self.iterate != 0:
            self.iterate = 0
        try:
            with open("RegisteredUsers.json", "r") as file:  # it will read the file and once it finds the username and corresponding password, it will successfully log them in and change the login button to continure where it will lead them to the to do list program.
                data = json.load(file)
                for fileusernames in data["users"]:             # first have to read the file and load the data. Then, it check if the username and password are correct if so, the user will be authorized otherwise, it will tell the user the password is incorrect or the account does not exist
                    self.iterate += 1
                    if username == fileusernames:
                        self.username = username
                        successuser += 1                    # this has if statements to check if username and passwords are correct. will tell the user if the user does not exist or if the password is incorrect
                        if password == data["passwords"][self.iterate-1]:
                            successpass += 1
                            self.checkUser = TRUE 
                            self.loadTasks()
                            self.loginText.config(text="Successfully logged in!", fg="green")
                            self.loginText.place(x=185, y=300)
                            self.loginButton.config(text="Continue", command=lambda:self.ShowFrame("ToDoListFrame"))
                            self.todoUser.config(text=f"Welcome, {username}.", font=("Corbel", 30, "bold"))
                            break
                        elif successpass == 0:
                            self.loginText.config(text="Password incorrect.", fg="red")
                    elif successuser == 0:
                        self.loginText.config(text="User not found.", fg="red")

        except FileNotFoundError:                                                       # if the file does not exist, it will create the file and insert test users, their passwords, and the tasks
            with open("RegisteredUsers.json", "w") as file:
                defaultData = {"users": ["1", "ken", "3"], "passwords": ["1", "password", "3"], "tasks": 
                               [[["1task1", "2025/09/1", 4], ["1task2", "2025/09/1", 2]], 
                                [["usertask1", "2025/09/01", 4], ["usertask2", "2025/09/01", 2]], 
                                [["3task1", "2025/09/01", 4], ["3task2", "2025/09/1", 2]]]}
                json.dump(defaultData, file)

    def RegisFrame(self):                 # the login frame which will be shown when they exit the menu frame after pressing the login button.
        regisFrame = Frame(self.container, background= "#d2d3db")
        regisFrame.grid(row=0, column=0, sticky="nsew", ipadx=300, ipady=600)
                                                                                            # it is basically the same as the login menu with the difference being the register button and there will also be a back button when they have finished registering.
        regisLabel = Label(regisFrame, text="Register", font=("Corbel", 50, "bold"), wraplength=600, background= "#d2d3db")
        regisLabel.place(x= 120, y=130)

        regisLabelUser = Label(regisFrame, text= "User:", font=("Corbel", 13), background= "#d2d3db")
        regisLabelUser.place(x=133, y=236)

        self.regisEntryUser = Entry(regisFrame)
        self.regisEntryUser.place(x= 185, y=240)

        regisLabelPassword = Label(regisFrame, text= "Password:", font=("Corbel", 13), background= "#d2d3db")
        regisLabelPassword.place(x=98, y=275)

        self.regisEntryPassword = Entry(regisFrame)
        self.regisEntryPassword.place(x=185, y=280)

        backButton = Button(regisFrame, text="Back", command=lambda:self.ShowFrame("LoginFrame"), background="#fafafa") # if the back button is pressed it will call the showframe function and show the login frame.
        backButton.place(x=300, y=320)

        regisButton = Button(regisFrame, text="Register", width=10, command=lambda:self.Register(self.regisEntryUser.get(), self.regisEntryPassword.get()), background="#fafafa")  # when the register button has been clicked it will run the register function however the register function will need the username and password as parameters so i will use .get() to obtain it from the entry boxes.
        regisButton.place(x=206, y=320)

        self.regisText = Label(regisFrame, text="", background= "#d2d3db")
        self.regisText.place(x=204, y=300)
        return regisFrame
    
    def Register(self, username, password):         # register system
        userexists = 0
        try:
            with open("RegisteredUsers.json", "r") as fileread:  # reading mode in order to check its content
                data = json.load(fileread)                      
                for i in data["users"]:
                    if i == username:
                        self.regisText.config(text="Username taken.", fg="red")
                        self.regisText.place(x=202, y=300)                  # if the username and password have already been registered to the json file, it will tell them that the account has been found and it will not be adding the username and password to prevent duplicates
                        userexists = 1
                if userexists == 0:
                    with open("RegisteredUsers.json", "w") as filewrite:
                        data["users"].append(username)
                        data["passwords"].append(password)
                        data["tasks"].append([["Default Task", "Default date", 1]])
                        json.dump(data, filewrite)              # if it is confirmed that the username and password are not yet added it will then add it to the json file 
                        self.regisText.config(text="User registered.", fg="green")
                        self.regisText.place(x=203, y=300)
        except FileNotFoundError:                                                       # if the file does not exist, it will create the file and insert test users, their passwords, and the tasks
            with open("RegisteredUsers.json", "w") as file:
                defaultData = {"users": ["1", "ken", "3"], "passwords": ["1", "password", "3"], "tasks": 
                               [[["1task1", "2025/09/1", 4], ["1task2", "2025/09/1", 2]], 
                                [["usertask1", "2025/09/01", 4], ["usertask2", "2025/09/01", 2]], 
                                [["3task1", "2025/09/01", 4], ["3task2", "2025/09/1", 2]]]}
                json.dump(defaultData, file)

    def loadTasks(self):                         # this will load the tasks if the user has tasks saved
        with open("RegisteredUsers.json", "r") as file:
            data = json.load(file)
            for i in data["tasks"][self.iterate-1]:
                task, dueDate, priorityLevel = i
                self.displayTask(task, dueDate, priorityLevel)

    def displayTask(self, task, dueDate, priorityLevel):   # this function is used to turn the tasks into widgets. used by add frames and load tasks
        taskItem = Frame(self.taskListFrame, bg="white")

        checkBox = Checkbutton(taskItem, text=task,command=lambda:self.RemoveTask(taskItem, [task, dueDate, priorityLevel]), bg="white", anchor="w")
        checkBox.pack(side=LEFT, anchor="w")                 

        priorityLevelDisplay = Label(taskItem, text=f"Priority: {priorityLevel}", anchor="w")
        priorityLevelDisplay.pack(side=RIGHT, anchor="w")

        dueDateDisplay = Label(taskItem, text=f"Due: {dueDate}", anchor="w")
        dueDateDisplay.pack(side=RIGHT, anchor="w")

        taskItem.pack(fill="x", pady=2, anchor="w")

        self.frameList.append(taskItem)

    def todolistFrame(self):               # this is the main frame for the to do list frame. will display the tasks
        todoFrame = Frame(self.container, background= "#d2d3db")
        todoFrame.grid(row=0, column=0, sticky="nsew", ipadx=300, ipady=600)

        self.todoUser = Label(todoFrame, text="", background= "#d2d3db")
        self.todoUser.place(x=30, y=10)

        todoLabel = Label(todoFrame, text="To do list", font=("Corbel", 15), background= "#d2d3db")
        todoLabel.place(x=200, y=70)

        self.taskCanvas = Canvas(todoFrame, height=400, width=460, background="white")
        self.taskCanvas.place(x=15, y=100)

        scrollbar = Scrollbar(todoFrame, orient="vertical", command=self.taskCanvas.yview)
        scrollbar.place(x=460, y=100, height=400)

        self.taskCanvas.configure(yscrollcommand=scrollbar.set)

        self.taskListFrame = Frame(self.taskCanvas, background="white")
        self.taskCanvas.create_window((0, 0), window=self.taskListFrame, anchor="nw")

        self.taskListFrame.bind(
            "<Configure>", 
            lambda e: self.taskCanvas.configure(scrollregion=self.taskCanvas.bbox("all"))
        )

        newactivityButton = Button(todoFrame, text="New Task", command=self.AddTasksFrame, height=2, font="Corbel", background="#fafafa")         # if button is clicked, it will show the addtasksframe where the user can add new tasks
        newactivityButton.place(x=170, y=520)

        logoutButton = Button(todoFrame, text="Logout", command=self.logoutFunction, height=2, fg="red", font="Corbel", background="#fafafa")    # if this button is clicked, the logout function is called
        logoutButton.place(x=270, y=520)

        # cleartasksButton = Button(todoFrame, text="Clear tasks", command=self.clearTasks, height=2, fg="red", font="Corbel")
        # cleartasksButton.place(x=300, y=520)

        return todoFrame

    def logoutFunction(self):       # function is used when the user logs out. it removes the previous login credentials, revert the continue button to login and sends the user back to main menu. it also removes the verification text and destroys all the widgets
        self.ShowFrame("MenuFrame")
        self.loginButton.config(text="Login", width=10, command=lambda:self.LoginVerif(self.loginEntryUser.get(), self.loginEntryPassword.get()))
        self.loginText.config(text="")
        self.loginEntryPassword.delete(0, END)
        self.loginEntryUser.delete(0, END)
        for i in self.frameList:
            i.destroy()                  

    # def clearTasks(self, listDelete):
    #     for i in self.frameList:
    #         with open("RegisteredUsers.json", "r") as file:
    #             data = json.load(file)
    #             if listDelete in data["tasks"][self.iterate-1]:
    #                 data["tasks"][self.iterate-1].remove(listDelete)
    #                 with open("RegisteredUsers.json", "w") as file:
    #                     json.dump(data, file)
    #             i.destroy()

    def AddTasks(self, addedTask, dueDate, priorityLevel):              # adds tasks as checkboxes inside taskListFrame  # for the second version of this, it adds tasks as widgets instead of checkboxes
        if len(addedTask)<=50 and len(addedTask) > 0:                        # now has boundaries and invalid. date and task entry boxes cannot be empty. task entry box also has a character limit of 50. priority level also cannot be 0
            if self.entryDate.get() == "":
                self.addtaskframeLabel.config(text="Date entry box cannot be empty.", fg="black")
            else:
                if self.taskpriorityLevel.get() == 0:
                    self.addtaskframeLabel.config(text="Priority Level cannot be zero.", fg="black")
                else:
                    self.addtaskframeLabel.config(text="Task added successfully", fg="green")
                    with open("RegisteredUsers.json", "r") as fileread:
                        data = json.load(fileread)
                        taskpackAdd = [addedTask, dueDate, priorityLevel]
                        data["tasks"][self.iterate-1].append(taskpackAdd)
                        with open("RegisteredUsers.json", "w") as filewrite:
                            json.dump(data, filewrite)
                    self.displayTask(addedTask, dueDate, priorityLevel)
        elif len(addedTask)>50:
            print((len(addedTask)))
            self.addtaskframeLabel.config(text=f"Task has exceeded the task character limit of 50 by {(len(addedTask))-50}.", fg="red")
        elif len(addedTask) == 0:
            self.addtaskframeLabel.config(text="Task entry box cannot be empty.", fg="black")

    def RemoveTask(self, taskItem, listDelete):           # removes the task frame from the task list while also removing it from the json file and saving it
        taskItem.destroy()
        with open("RegisteredUsers.json", "r") as file:
            data = json.load(file)
            if listDelete in data["tasks"][self.iterate-1]:
                data["tasks"][self.iterate-1].remove(listDelete)
                with open("RegisteredUsers.json", "w") as file:
                    json.dump(data, file)
    
    def AddTasksFrame(self):        # this will be the mini frame when the user is adding new tasks, it will contain an entry box where the user can enter the task, it will also have an entry box where the user will enter the due date and finally it will have radio buttons where the user will enter the priority level
        self.taskFrame = Frame(self.container, borderwidth=2, relief="ridge", background= "#d2d3db")
        self.taskFrame.place(x=40, y=40, width=420, height=520)

        taskaddLabel = Label(self.taskFrame, text="New Task", font=("Corbel", 15), background= "#d2d3db")
        taskaddLabel.place(x=165, y=90)

        self.taskpriorityLevel = IntVar()

        prioritylevelLabel = Label(self.taskFrame, text="Priority Level", font=("Corbel", 10), background= "#d2d3db")
        prioritylevelLabel.place(x=170, y=225)

        self.level1Priority = Radiobutton(self.taskFrame, text="1", value=1, variable=self.taskpriorityLevel, background= "#d2d3db")
        
        self.level1Priority.place(x=135,y=250)

        self.level2Priority = Radiobutton(self.taskFrame, text="2", value=2, variable=self.taskpriorityLevel, background= "#d2d3db")
        self.level2Priority.place(x=165, y=250)

        self.level3Priority = Radiobutton(self.taskFrame, text="3", value=3, variable=self.taskpriorityLevel, background= "#d2d3db")
        self.level3Priority.place(x=195, y=250)

        self.level4Priority = Radiobutton(self.taskFrame, text="4", value=4, variable=self.taskpriorityLevel, background= "#d2d3db")
        self.level4Priority.place(x=225, y=250)

        self.level5Priority = Radiobutton(self.taskFrame, text="5", value=5, variable=self.taskpriorityLevel, background= "#d2d3db")
        self.level5Priority.place(x=255, y=250)

        entryTaskLabel = Label(self.taskFrame, text="Task:", font=("Corbel", 10), background= "#d2d3db")
        entryTaskLabel.place(x=115, y=146)

        lowestLabel = Label(self.taskFrame, text="Lowest", font=("Corbel", 10), background= "#d2d3db")
        lowestLabel.place(x=90, y=250)

        highestLabel = Label(self.taskFrame, text="Highest", font=("Corbel", 10), background= "#d2d3db")
        highestLabel.place(x=290, y=250)

        entryTask = Entry(self.taskFrame)
        entryTask.place(x=150, y=150, height=15)

        tasksAddButton = Button(self.taskFrame, text="Add task",command=lambda:self.AddTasks(entryTask.get(),self.entryDate.get(), self.taskpriorityLevel.get()), background="#fafafa")  # if this button is clicked, add tasks function is called where it will call the display function if the task is valid and add the tasks as widgets
        tasksAddButton.place(x=183, y=290, height= 17)

        taskframeClose = Button(self.taskFrame, text="Close", fg="red", command=lambda:self.AddTasksFrameclose(), background="#fafafa") # this closes the addtaskframe
        taskframeClose.pack()

        entryDateLabel = Label(self.taskFrame, text="Deadline:", font=("Corbel", 10), background= "#d2d3db")
        entryDateLabel.place(x=90, y=197)

        self.addtaskframeLabel = Label(self.taskFrame, text="", background= "#d2d3db")
        self.addtaskframeLabel.place(x=90, y=310)

        self.entryDate = Entry(self.taskFrame)
        self.entryDate.place(x=150, y=200, height=15)

        addtaskDescription = Label(self.taskFrame, text="To add a new task, enter the task in the 'Task:' entry box (The task has a 50 character limit). When you're done, enter when you want it to be done in the 'Deadline:' entry box. Then finally, select the priority level (How urgent the task is.) and click add task.", width=50, wraplength=200, background= "#d2d3db")
        addtaskDescription.place(x=35, y=330)

    def AddTasksFrameclose(self):           # this function will be used when the user will close the mini frame.
        self.taskFrame.place_forget()

# main program
root = Tk()
root.title("To do list")
app = ToDoList(root)
root.geometry("500x600")
root.resizable(0,0)
root.mainloop()