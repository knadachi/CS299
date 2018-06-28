#Question 3
def createDict( accounts ):
    usernames = []
    passwords = []
    for i in accounts:
        usernames.append( i[0] )
        passwords.append( i[1] )
    return dict( zip( usernames, passwords ) )

def createUser( accounts ):
    user = input( "Choose a username: " )
    if not checkDup( user, accounts ):
        pw = input( "Choose a password: " )
        accounts[user] = pw
        print( "Successfully created new user." )

def checkDup( user, accounts ):
    for key in accounts.keys():
        if key == user:
            print( "Username is taken." )
            return True
    return False

def login( accounts ):
    user = input( "Username: " )
    for i in range( 3, 0, -1 ):
        for key in accounts.keys():
            if key == user:
                pw = accounts[user]
                enteredPw = input( "Password: " )
                if pw == enteredPw:
                    print( "Login successful!" )
                    return
                else:
                    print( "Incorrect password." )
                    if i == 1:
                        print( "Login attempt failed." )
                        return
    print( "Username does not exist." )

def UI( accounts ):
    cont = True
    while( cont ):
        print( "--------------------------" )
        print( "What would you like to do?" )
        print( "   [1] Login" )
        print( "   [2] Create new user" )
        print( "   [3] Quit" )
        choice = input( "Your choice: " )
        if choice == "1":
            login( accounts )
        elif choice == "2":
            createUser( accounts )
        elif choice == "3":
            cont = False
        else:
            print( "Invalid input." )

def main():
    aList = [("Ted", "p123"), ("Kelly", "highwind11&&"), ("Kristin", "pw12345") ]
    accounts = createDict( aList )
    UI( accounts )

if __name__ == "__main__":
    main()

'''
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 1
Username: Kristin
Password: pw12345
Login successful!
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 1
Username: WrongUser
Username does not exist.
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 1
Username: Ted
Password: Test
Incorrect password.
Password: Hello
Incorrect password.
Password: Hi
Incorrect password.
Login attempt failed.
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 2
Choose a username: NewUser
Choose a password: NewPassword
Successfully created new user.
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 2
Choose a username: NewUser
Username is taken.
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 3
'''
