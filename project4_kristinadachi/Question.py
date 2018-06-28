#Represents a short answer question
class Question:
    #Question constructor
    def __init__( self ):
        self.question = ""
        self.answer = ""

    #Sets the question text
    def setText( self, questionText ):
        self.question = questionText

    #Sets the answer for the current question
    def setAnswer( self, correctResponse ):
        self.answer = correctResponse

    #Checks if the user's answer is correct or not and prints the result
    def checkAnswer( self, response ):
        try:
            if self.answer == response:
                print( "Your answer is correct!" )
            else:
                print( "Your answer is incorrect! The correct answer is:", self.answer )
        except AttributeError:
            print( "Answer has not been set yet." )

    #Prints the current question
    def display( self ):
        print( self.question )

#Represents a multiple choice question that inherits from the Question class
class ChoiceQuestion( Question ):
    #ChoiceQuestion constructor
    def __init__( self ):
        self.choices = []

    #Allows user to add more choices as answers for the question and decides
    #whether it is correct or not
    def addChoice( self, choice, correct ):
        self.choices.append( choice )
        index = str( self.choices.index( choice ) + 1 )
        if correct:
            Question.setAnswer( self, index )

    #Overrides the display function in Question and prints out the multiple
    #choice question as well as possible answers
    def display( self ):
        num = 1
        print( self.question )
        string = ""
        for i in self.choices:
            string += "[" + str( num ) + "]" + str( i ) + "\n"
            num += 1
        print( string )

#Contains the test cases        
def main():
    #Question test cases
    for i in range( 1, 3 ):
        print( "\n------" )
        print( "Test", i )
        print( "------" )
        test = Question()
        test.setText( "What is Python?" )
        test.setAnswer( "A programming language." )
        test.display()
        userResponse = input( "Your response: " )
        test.checkAnswer( userResponse )

    #ChoiceQuestion test cases
    for i in range( 3, 5 ):
        print( "\n------" )
        print( "Test", i )
        print( "------" )
        test = ChoiceQuestion()
        test.setText( "In which country was the inventor of Python born?" )
        test.addChoice( "Australia", False )
        test.addChoice( "Canada", False )
        test.addChoice( "Netherlands", True )
        test.addChoice( "United States", False )
        test.display()
        userResponse = input( "Your response: " )
        test.checkAnswer( userResponse )
                
if __name__ == "__main__":
    main()

'''
------
Test 1
------
What is Python?
Your response: A programming language.
Your answer is correct!

------
Test 2
------
What is Python?
Your response: I don't know.
Your answer is incorrect! The correct answer is: A programming language.

------
Test 3
------
In which country was the inventor of Python born?
[1]Australia
[2]Canada
[3]Netherlands
[4]United States

Your response: 3
Your answer is correct!

------
Test 4
------
In which country was the inventor of Python born?
[1]Australia
[2]Canada
[3]Netherlands
[4]United States

Your response: 4
Your answer is incorrect! The correct answer is: 3
'''
