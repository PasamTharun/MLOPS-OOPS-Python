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
            self.my_post()
        elif user_input=='4':
            self.sendmsg()
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
                self.loggedin=True
            else:
                print("Invalid Credentials! Please try again.")
        print('\n')
        self.menu()
        
    def my_post(self):
        if self.loggedin==True:
            post=input("write your post here--->")
            print(f"following post has been posted:{post}")
        else:
            print("Please Signin first to write a post")
        print('\n')
        self.menu()
    
    def sendmsg(self):
        if self.loggedin==True:
            txt=input("write your messaget here--->")
            friend=input("Enter your friend's name here--->")
            print(f"your message:{txt} has been sent to {friend}")
        else:
            print("Please Signin first to message with friend")
        print('\n')
        self.menu()
    
obj=chatBook()
