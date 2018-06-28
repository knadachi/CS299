import csv
import urllib.request

#Question 1: Read book.txt and copy to a new file called myBook.txt
def copyBook():
    infile = open( "book.txt", "r", newline="" )
    outfile = open( "myBook.txt", "w", newline="" )
    for line in infile:
        outfile.write( line )
    infile.close()
    outfile.close()

#Question 2: Read planets.csv file, add 2 moons to each planet, and
#            write to another file called myPlanets.csv
def editPlanets():
    planets = []
    with open( "planets.csv", newline="" ) as file:
        reader = csv.reader( file )
        for row in reader:
            if row[10] != "\tMoon":
                moons = int( row[10] ) + 2
                row[10] = "\t" + str( moons )
            planets.append( row )
    with open( "myPlanets.csv", "w", newline="" ) as file:
        writer = csv.writer( file )
        writer.writerows( planets )

#Question 3: Read in data from a website
def website():
    page = urllib.request.urlopen('https://www.github.com/')
    data = page.readlines()
    print( data[0:10] )

#Test all three questions
copyBook()
editPlanets()
website()
        
