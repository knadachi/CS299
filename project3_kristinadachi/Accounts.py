#reads from given file and returns a list of values
def readFile( fileName ):
    data = []
    file = open( fileName )
    for line in file:
        temp = line.split( " " )
        data = data + temp
    data = removeExtra( data )
    return data

#removes extra characters from the given list
def removeExtra( aList ):
    newList = []
    for i in aList:
        newList.append( i.strip() )
    return newList

#creates a dictionary using listA as keys and listB as values
def createDict( listA, listB ):
    return dict( zip( listA, listB ) )

#prompts user for username and password (successful login if both
#are correct and unsuccessful otherwise)
def login( accounts ):
    print( "--------------------------" )
    user = input( "Username: " )
    for key in accounts.keys():
        if key == user:
            pw = accounts[user]
            enteredPw = input( "Password: " )
            if pw == enteredPw:
                print( "Login successful!" )
            else:
                print( "Incorrect password." )
            return
    print( "Username doesn't exist." )

#prompts user for a new username and password
def createUser( accounts ):
    print( "--------------------------" )
    user = input( "Choose a username: " )
    if validateUser( accounts, user ):
        pw = input( "Choose a password: " )
        if validatePw( pw ):
            accounts[ user ] = pw
            print( "Sucesssfully created new user." )

#validates given username:
# [1] cannot already be in the dictionary
# [2] must begin with a letter
# [3] can only contain letters or digits
def validateUser( accounts, user ):
    for key in accounts.keys():
        if key == user:
            print( "Username is taken." )
            return False
        else:
            if not user[0].isalpha():
                print( "Username is invalid." )
                return False
            for i in user:
                if not i.isalpha() and not i.isdigit():
                    print( "Username is invalid." )
                    return False
    return True

#validates given password:
# [1] length must be at least 8
# [2] must contain at least 3 of the following...
#      [a] uppercase letters
#      [b] lowercase letters
#      [c] digits
#      [d] special characters (#, $, ^, *, +, =, -, _)
def validatePw( pw ):
    count = 0
    counts = [ 0, 0, 0, 0 ]
    special = [ '#', '$', '^', '*', '+', '=', '-', '_' ]
    if len( pw ) < 8:
        print( "Password is invalid." )
        return False
    for i in pw:
        if i.isupper():
            counts[0] += 1
        elif i.islower():
            counts[1] += 1
        elif i.isdigit():
            counts[2] += 1
        elif i in special:
            counts[3] += 1
    for i in counts:
        if i > 0:
            count += 1
    if count < 3:
        print( "Password is invalid." )
        return False
    return True
            
#performs the UI of the program
def UI():
    cont = True
    names = readFile( "names.txt" )
    passwords = readFile( "codes.txt" )
    accounts = createDict( names, passwords )
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

#main method that starts the program
def main():
    UI()

if __name__ == "__main__":
    main()

'''
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 2
--------------------------
Choose a username: Kristin123
Choose a password: Kristin321
Sucesssfully created new user.
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 2
--------------------------
Choose a username: tEsTiNg
Choose a password: testing54321*
Sucesssfully created new user.
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 2
--------------------------
Choose a username: Pikachu
Choose a password: pikapikachuuu1*^*
Sucesssfully created new user.
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 1
--------------------------
Username: yoyo333
Password: fail
Incorrect password.
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 1
--------------------------
Username: Kristin123
Password: failagain
Incorrect password.
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 1
--------------------------
Username: Pikachu
Password: pikapikachuuu1*^*
Login successful!
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 1
--------------------------
Username: lisaAn1
Password: X&amp;122343
Login successful!
--------------------------
What would you like to do?
   [1] Login
   [2] Create new user
   [3] Quit
Your choice: 3
'''
