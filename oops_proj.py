class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()


    def menu(self):
        user_input=input("welcome to chatbook, please select an option: 1. signup 2. signin 3. write a post 4. message a friend 5. exit")

        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()

    def signup(self):
        email=input("enter your email")
        password=input("setup your password")
        self.username=email
        self.password=password
        print("signup successful, please login to continue")
        print("\n")
        self.menu() #after signup, we are calling the menu method again to allow the user to select the signin option and login to their account
    
    def signin(self):
        if self.username=='' or self.password=='':
            print("no user found, please signup first")
            self.menu()
        else:
            email=input("enter your email")
            password=input("enter your password")
            if email==self.username and password==self.password:
                print("signin successful, welcome to chatbook")
                self.loggedin=True
            else:
                print("invalid credentials, please try again")
                self.menu()
        print("\n")
        self.menu() #after signin, we are calling the menu method again to allow the user to select other options like write a post or message a friend

    

    

obj=chatbook() #calling the constructor of the class, which will automatically call the menu method

        
