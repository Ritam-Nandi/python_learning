def view_password():
    with open("password.txt","r") as f:
        for line in f.readlines():
            username,password=line.split("|")
            print("Username: ",username,"| Password: ",password)

def add_password():
    username=input("Enter Username: ")
    password=input("Enter Password: ")
    
    with open("password.txt","a") as f:
        f.write((username+"|"+password+"\n")) 

print ("Do you want to View your passwords (view) or Enter a New Password (add)? Press q to quit anytime ")
choice = input("view|add|q")

while choice != "q":
    if choice == "view":
        view_password()
    elif choice == "add":
        add_password()
    else:
        print ("Wrong choice")

    print ("Do you want to View your passwords (view) or Enter a New Password (add)? Press q to quit anytime ")
    choice = input("view|add|q")        
