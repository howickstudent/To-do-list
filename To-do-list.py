from tkinter import *
import json

class ToDoList():
    def __init__(self, root): # the main thing that this function does is initializing and creating the container for the other frames.
        self.root = root

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
        menuFrame = Frame(self.container)
        menuFrame.grid(row=0, column=0, sticky="nsew", ipadx=300, ipady=600)

        menuLabel = Label(menuFrame, text="Menu", font=("Corbel", 50, "bold"))
        menuLabel.place(x= 170, y=150)

        menuButton = Button(menuFrame, text="Login", command=lambda:self.ShowFrame("LoginFrame"), padx=20, pady=6)   # once the login button has been pressed it will call the login frame which was stored in the dictionary.
        menuButton.place(x=220,y=240)                       

        return menuFrame                  # returning the frame so it will be stored in the dictionary.
    
    def LoginFrame(self):                 # the login frame which will be shown when they exit the menu frame after pressing the login button.
        loginFrame = Frame(self.container)
        loginFrame.grid(row=0, column=0, sticky="nsew", ipadx=300, ipady=600)
        
        loginLabel = Label(loginFrame, text="Login", font=("Corbel", 50, "bold"), wraplength=200)
        loginLabel.place(x= 160, y=130)

        loginLabelUser = Label(loginFrame, text= "User:", font=("Corbel", 13))
        loginLabelUser.place(x=133, y=236)

        loginEntryUser = Entry(loginFrame)
        loginEntryUser.place(x= 185, y=240)

        loginLabelPassword = Label(loginFrame, text= "Password:", font=("Corbel", 13))
        loginLabelPassword.place(x=98, y=275)

        loginEntryPassword = Entry(loginFrame)
        loginEntryPassword.place(x=185, y=280)

        self.loginButton = Button(loginFrame, text="Login", width=10, command=lambda:self.LoginVerif(loginEntryUser.get(), loginEntryPassword.get()))
        self.loginButton.place(x=206, y=320)

        regismenuButton = Button(loginFrame, text="Register Instead", width=12, command=lambda:self.ShowFrame("RegisterFrame"))
        regismenuButton.place(x=200, y=500)

        self.loginText = Label(loginFrame, text="")
        self.loginText.place(x=204, y=300)
        return loginFrame
    
    def LoginVerif(self, username, password):       # login verification
        successuser = 0
        successpass = 0
        iterate = 0
        try:
            with open("RegisteredUsers.json", "r") as file:  # it will read the file and once it finds the username and corresponding password, it will successfully log them in and change the login button to continure where it will lead them to the to do list program.
                data = json.load(file)
                for fileusernames in data["users"]: 
                    iterate += 1
                    if username == fileusernames:
                        successuser += 1
                        if password == data["passwords"][iterate-1]:
                            self.loginText.config(text="Successfully logged in!", fg="green")
                            self.loginText.place(x=185, y=300)
                            self.loginButton.config(text="Continue", command=lambda:self.ShowFrame("ToDoListFrame"))
                            successpass += 1 
                    elif successuser == 0:
                        self.loginText.config(text="User not found.", fg="red")
        except FileNotFoundError:
            with open("RegisteredUsers.json", "w") as file:
                defaultData = {"users": ["1", "ken", "3"], "passwords": ["1", "password", "3"], "tasks": [["1task1", "1task2"], ["usertask1", "usertask2"], ["3task1", "3task2"]]}
                json.dump(defaultData, file)

    def RegisFrame(self):                 # the login frame which will be shown when they exit the menu frame after pressing the login button.
        regisFrame = Frame(self.container)
        regisFrame.grid(row=0, column=0, sticky="nsew", ipadx=300, ipady=600)
                                                                                            # it is basically the same as the login menu with the difference being the register button and there will also be a back button when they have finished registering.
        regisLabel = Label(regisFrame, text="Register", font=("Corbel", 50, "bold"), wraplength=600)
        regisLabel.place(x= 120, y=130)

        regisLabelUser = Label(regisFrame, text= "User:", font=("Corbel", 13))
        regisLabelUser.place(x=133, y=236)

        regisEntryUser = Entry(regisFrame)
        regisEntryUser.place(x= 185, y=240)

        regisLabelPassword = Label(regisFrame, text= "Password:", font=("Corbel", 13))
        regisLabelPassword.place(x=98, y=275)

        regisEntryPassword = Entry(regisFrame)
        regisEntryPassword.place(x=185, y=280)

        backButton = Button(regisFrame, text="Back", command=lambda:self.ShowFrame("LoginFrame")) # if the back button is pressed it will call the showframe function and show the login frame.
        backButton.place(x=300, y=320)

        regisButton = Button(regisFrame, text="Register", width=10, command=lambda:self.Register(regisEntryUser.get(), regisEntryPassword.get()))  # when the register button has been clicked it will run the register function however the register function will need the username and password as parameters so i will use .get() to obtain it from the entry boxes.
        regisButton.place(x=206, y=320)

        self.regisText = Label(regisFrame, text="")
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
                        data["tasks"].append(["task1", "task2"])
                        json.dump(data, filewrite)              # if it is confirmed that the username and password are not yet added it will then add it to the json file 
                        self.regisText.config(text="User registered.", fg="green")
                        self.regisText.place(x=203, y=300)
        except FileNotFoundError:
            with open("RegisteredUsers.json", "r") as fileread:
                data = json.load(fileread)
                with open("RegisteredUsers.json", "w") as file:
                    defaultData = {"users": ["1", "ken", "3"], "passwords": ["1", "password", "3"], "tasks": [["1task1", "1task2"], ["usertask1", "usertask2"], ["3task1", "3task2"]]}
                    json.dump(defaultData, file)

    def todolistFrame(self):
        todoFrame = Frame(self.container)
        todoFrame.grid(row=0, column=0, sticky="nsew", ipadx=300, ipady=600)
        
        return todoFrame
# main program
root = Tk()
app = ToDoList(root)
root.geometry("500x600")
root.resizable(0,0)
root.mainloop()