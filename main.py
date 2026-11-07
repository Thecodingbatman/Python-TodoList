import sqlite3
connection = sqlite3.connect(r"C:\sqlite\userinfo")
print("This is a TODO list app")
registered = False
#MainLoop
while True:
    ToDoListAction = str(input("Please enter what you want to do: list, quit:\n ")).lower().strip()
    if ToDoListAction == "quit":
        break
    elif ToDoListAction == "list":
        if registered == False:
            print("Please register")
            name = str(input("Enter your Name: "))
            password = str(input("Enter your password: "))
            registered = True
            break
     