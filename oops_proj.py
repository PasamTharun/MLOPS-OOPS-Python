class chatBook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()
        
        
    
    def menu(self):
        user_input=input("""Welcome to ChatBook! How would you like to proceed?
                         1.press 1 to signup
                         2.press 2 to signin
                         3.press 3 to write a post 
                         4.press 4 to message with friend
                         5.press any other key to exit
                         """)
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
        email=input("Enter Your Email Here--->")
        pwd=input("Setup Your Password Here--->")
        self.username=email
        self.password=pwd
        print("Signup Successful!")
        print('\n')
        self.menu()
        
        
    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the menu")
        else:
            uname=input("Enter your email/Username here--->")
            pwd=input("Enter your password here--->")
            if self.username==uname and self.password==pwd:
                print("Signin Successful!")
                self.loggeding=True
            else:
                print("Invalid Credentials! Please try again.")
        print('\n')
        self.menu()
    
obj=chatBook()
