class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()


    def menu(self):
        user_input=input("welcome to chatbook, please select an option: 1. signup 2. signin 3. write a post 4. message a friend 5. exit")

        if user_input=='1':
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()


obj=chatbook() #calling the constructor of the class, which will automatically call the menu method

        
