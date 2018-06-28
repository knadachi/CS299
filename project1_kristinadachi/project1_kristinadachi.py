import random
import time

"""
#1: This function takes in user input and displays the resulting acronym. It omits some
conjunctive words from the given input and uses the first character of each word.
"""
def acronym():
    delete = [ "and", "by", "in", "of", "on" ]
    string = input( "What would you like to convert to an acronym?: " )
    for word in delete:
        if word in string:
            string = string.replace( word, "" )
    print( "Acronym: ", ''.join( word[0].upper() for word in string.split() ) )

"""
#2: This function takes in a number and determines if it is a perfect number or not. Returns
true if it is a perfect number and false otherwise.
"""
def perfectNum( num ):
    sum = 0
    string = str( num ) + "="
    for i in range( 1, num ):
        if num % i == 0:
            sum += i
            string += str( i ) + "+"
    if sum == num:
        print( string[:-1] )
        return True
    else:
        print( str( num ), "is not a perfect number." )
        return False

"""
#3: This function uses the MonteCarlo method to calculate pi. It prints the value of n, the
value of pi, and the execution time.
"""
def findPi( n ):
    start = time.time()
    count = 0
    for i in range( 0, n ):
        x = random.uniform( 0, 1 )
        y = random.uniform( 0, 1 )
        if (x**2 + y**2)**(1/2) <= 1:
            count += 1
    pi = 4 * count / n
    end = time.time()
    print( "n:", n )
    print( "Pi:", pi )
    print( "Time:", round( end - start, 6 ), "seconds" )

"""
This part of the program runs the test cases for the three functions.
"""
print( "============" )
print( " Question 1" )
print( "============" )
for i in range( 0, 4 ):
    acronym()

print( "\n============" )
print( " Question 2" )
print( "============" )
print( perfectNum( 6 ) )
print( perfectNum( 28 ) )
print( perfectNum( 325 ) )
print( perfectNum( 496 ) )

print( "\n============" )
print( " Question 3" )
print( "============" )
findPi( 100 )
findPi( 1000 )
findPi( 10000 )

"""
============
 Question 1
============
What would you like to convert to an acronym?: North Atlantic Treaty Organization
Acronym:  NATO
What would you like to convert to an acronym?: light amplification by stimulated emission of radiation
Acronym:  LASER
What would you like to convert to an acronym?: United States of America
Acronym:  USA
What would you like to convert to an acronym?: American Automobile Association
Acronym:  AAA

============
 Question 2
============
6=1+2+3
True
28=1+2+4+7+14
True
325 is not a perfect number.
False
496=1+2+4+8+16+31+62+124+248
True

============
 Question 3
============
n: 100
Pi: 3.0
Time: 0.0 seconds
n: 1000
Pi: 3.096
Time: 0.002006 seconds
n: 10000
Pi: 3.1416
Time: 0.013495 seconds
"""
