class ComboLock:
    #Constructor for ComboLock
    def __init__( self, combo ):
        self.combo = combo
        self.position = 0
        self.userCombo = []
        self.userTurns = []
        print( "Lock at position 0" )

    #Resets the lock to position 0
    def reset( self ):
        self.position = 0
        self.userCombo = []
        self.userTurns = []
        print( "Lock has been completely reset, now at position 0" )

    #Turns the lock a given number of ticks to the left
    def turnLeft( self, ticks ):
        print( "You turned the lock", ticks, "ticks to the left..." )
        self.position -= ticks
        if self.position < 0:
            self.position += 10
        self.position %= 10
        self.userCombo.append( self.position )
        self.userTurns.append( "Left" )
        print( "Lock at position", self.position )

    #Turns the lock a given number of ticks to the right
    def turnRight( self, ticks ):
        print( "You turned the lock", ticks, "ticks to the right..." )
        self.position += ticks
        if self.position > 9:
            self.position -= 10
        self.position %= 10
        self.userCombo.append( self.position )
        self.userTurns.append( "Right" )
        print( "Lock at position", self.position )

    #Attempts to open the lock using a list of the user's combination as well
    #as turns
    def open( self ):
        print( "\nAttempting to open lock with the following information..." )
        print( "Combination entered:", self.userCombo )
        print( "Turns performed:", self.userTurns )
        if len( self.userCombo ) == 3:
            if self.userCombo == self.combo:
                if self.userTurns[0] == self.userTurns[2] and self.userTurns[1] == "Left":
                    print( "Lock has opened successfully!\n" )
                else:
                    print( "Failed to open lock\n" )
            else:
                print( "Failed to open lock\n" )
        else:
            print( "Failed to open lock\n" )

#main method that contains the 3 test cases
def main():
    print( "------" )
    print( "Test 1" )
    print( "------" )
    test1 = ComboLock( [2, 7, 3] )
    print( "Combination is:", test1.combo, "\n" )
    test1.turnRight( 2 )
    test1.turnLeft( 3 )
    test1.turnRight( 7 )
    test1.open()
    test1.reset()
    test1.turnRight( 2 )
    test1.turnLeft( 5 )
    test1.turnRight( 6 )
    test1.open()

    print( "\n------" )
    print( "Test 2" )
    print( "------" )
    test1 = ComboLock( [5, 0, 9] )
    print( "Combination is:", test1.combo, "\n" )
    test1.turnRight( 5 )
    test1.turnLeft( 5 )
    test1.turnRight( 9 )
    test1.open()

    print( "\n------" )
    print( "Test 3" )
    print( "------" )
    test1 = ComboLock( [7, 4, 5] )
    print( "Combination is:", test1.combo, "\n" )
    test1.turnRight( 7 )
    test1.turnRight( 7 )
    test1.turnRight( 1 )
    test1.open()

if __name__ == "__main__":
    main()

'''
------
Test 1
------
Lock at position 0
Combination is: [2, 7, 3] 

You turned the lock 2 ticks to the right...
Lock at position 2
You turned the lock 3 ticks to the left...
Lock at position 9
You turned the lock 7 ticks to the right...
Lock at position 6

Attempting to open lock with the following information...
Combination entered: [2, 9, 6]
Turns performed: ['Right', 'Left', 'Right']
Failed to open lock

Lock has been completely reset, now at position 0
You turned the lock 2 ticks to the right...
Lock at position 2
You turned the lock 5 ticks to the left...
Lock at position 7
You turned the lock 6 ticks to the right...
Lock at position 3

Attempting to open lock with the following information...
Combination entered: [2, 7, 3]
Turns performed: ['Right', 'Left', 'Right']
Lock has opened successfully!


------
Test 2
------
Lock at position 0
Combination is: [5, 0, 9] 

You turned the lock 5 ticks to the right...
Lock at position 5
You turned the lock 5 ticks to the left...
Lock at position 0
You turned the lock 9 ticks to the right...
Lock at position 9

Attempting to open lock with the following information...
Combination entered: [5, 0, 9]
Turns performed: ['Right', 'Left', 'Right']
Lock has opened successfully!


------
Test 3
------
Lock at position 0
Combination is: [7, 4, 5] 

You turned the lock 7 ticks to the right...
Lock at position 7
You turned the lock 7 ticks to the right...
Lock at position 4
You turned the lock 1 ticks to the right...
Lock at position 5

Attempting to open lock with the following information...
Combination entered: [7, 4, 5]
Turns performed: ['Right', 'Right', 'Right']
Failed to open lock
'''
