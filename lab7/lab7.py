import csv

#checks if the given name is in the dictionary; returns the total
#scores for that name and 0 otherwise
def getTotalScore( name, dictionary ):
    try:
        total = 0
        for score in dictionary[name]:
            total += score
        return total
    except KeyError:
        print( name, "is not in the gradebook." )
        return 0

#reads the grades_csv.csv file and converts the data into a
#dictionary whose keys are the names and values are the list of
#grades
def readFile( fileName ):
    names = []
    scores = []
    with open( fileName, newline="" ) as file:
        reader = csv.reader( file )
        for line in reader:
            scores.append( line )
    names, scores = clean( names, scores )
    return dict( zip( names, scores ) )

#writes another csv file called gradebook.csv that includes the total
#scores as well as the original file
def writeFile( fileName, dictionary ):
    first = True
    with open( fileName, newline="" ) as infile:
        reader = csv.reader( infile )
        with open( "gradebook.csv", "w", newline="" ) as outfile:
            writer = csv.writer( outfile )
            for line in reader:
                if first == True:
                    line.append( "Total" )
                    first = False
                else:
                    line.append( getTotalScore( line[0].replace( ",", "" ), dictionary ) )
                writer.writerow( line )
    
#removes the header of the grades_csv.csv file and updates the names
#and scores lists
def clean( names, scores ):
    updatedScores = []
    scores.pop( 0 )
    for s in scores:
        names.append( s.pop( 0 ).replace( ",", "" ) )
    return names, scores

#checks the given dictionary for any illegal scores (any non-numerical
#character); returns the illegal character count as well as the updated
#dictionary (score with an illegal character is treated as a 0)
def checkIllegal( dictionary ):
    illegalCount = 0
    updatedNames = dictionary.keys()
    updatedScores = []
    for scores in dictionary.values():
        temp = []
        for score in scores:
            try:
                temp.append( float( score ) )
            except ValueError:
                illegalCount += 1
                temp.append( 0.0 )
        updatedScores.append( temp )
    updatedDict = dict( zip( updatedNames, updatedScores ) )
    return illegalCount, updatedDict

#runs the program and handles the UI
def main():
    cont = True
    tempGradebook = readFile( "grades_csv.csv" )
    illegal, gradebook = checkIllegal( tempGradebook )
    writeFile( "grades_csv.csv", gradebook )
    print( "File read and gradebook generated." )
    print( "Number of illegal scores:", illegal )
    while cont :
        print( "----------------------------------" )
        print( "Enter a name (lastname firstname) to find their total score or 'Q' to quit." )
        name = input( "Please enter a name: " )
        if name.lower() == "q":
            cont = False
        else:
            total = getTotalScore( name, gradebook )
            if total != 0:
                print( "Total Score for", name, end="" )
                print( ":", total )

if __name__ == "__main__":
    main()

'''
File read and gradebook generated.
Number of illegal scores: 9
----------------------------------
Enter a name (lastname firstname) to find their total score or 'Q' to quit.
Please enter a name: Alfaro Mary
Total Score for Alfaro Mary: 680.5
----------------------------------
Enter a name (lastname firstname) to find their total score or 'Q' to quit.
Please enter a name: Adachi Kristin
Adachi Kristin is not in the gradebook.
----------------------------------
Enter a name (lastname firstname) to find their total score or 'Q' to quit.
Please enter a name: q
'''
