#modules used for csv files, histogram, and drawing
import csv
import numpy as np
import turtle

#reads the earthquake magnitudes from the given file
def readFile( fileName ):
    mags = []
    updatedMags = []
    with open( fileName, newline="" ) as file:
        reader = csv.reader( file )
        for row in reader:
            mags.append( row[4] )
    mags = remove( mags, "mag", "" )
    for i in mags:
        mag = float( i )
        if mag > 0.0:
            updatedMags.append( mag )
    return updatedMags

#removes the specified strings from the given list
def remove( aList, *args ):
    for arg in args:
        aList = [i for i in aList if i != arg]
    return aList

#uses turtle to draw the horizontal and vertical axes of the histogram
def drawSetup( bins, verticalInc, upper ):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.pensize( 2 )
    pen.penup()

    #horizontal axis
    pen.goto( -360, -325 )
    c = 0
    for i in bins:
        pen.forward( 60 )
        pen.penup()
        pen.goto( pen.xcor(), pen.ycor() - 20 )
        pen.write( i )
        pen.goto( pen.xcor(), pen.ycor() + 20 )
        if c == int( len(bins) / 2 ):
            pen.goto( pen.xcor() - 25, pen.ycor() - 50 )
            pen.write( "Magnitude of Earthquake" )
            pen.goto( pen.xcor() - 50, pen.ycor() + 750 )
            pen.write( "Earthquakes Histogram (Past 30 Days)" )
            pen.goto( pen.xcor() + 75, pen.ycor() - 700 )
        c += 1
        pen.pendown()

    #vertical axis
    pen.penup()
    pen.goto( -300, -325 )
    pen.setheading( 90 )
    pen.pendown()
    for i in range( int( upper / verticalInc ) ):
        pen.forward( 40 )
        pen.goto( pen.xcor() - 30, pen.ycor() )
        pen.write( (i+1) * verticalInc )
        pen.goto( pen.xcor() + 30, pen.ycor() )
        pen.penup()
        if i == int( int(upper/verticalInc) / 2 ):
            pen.goto( pen.xcor() - 120, pen.ycor() - 20 )
            pen.write( "Number\nof\nEarthquakes" )
            pen.goto( pen.xcor() + 120, pen.ycor() + 20 )
        pen.pendown()
    pen.hideturtle()

#uses turtle to draw the bars of the histogram
def drawBars( hist ):
    pen = turtle.Turtle()
    pen.penup()
    pen.goto( -300, -325 )
    pen.setheading( 90 )
    pen.pendown()
    for i in hist:
        val = i / 5
        pen.forward( val )
        pen.setheading( 0 )
        pen.forward( 60 )
        pen.setheading( 270 )
        pen.forward( val )
        pen.setheading( 90 )
    pen.hideturtle()

#main function that reads the earthquake data csv file to get the
#magnitudes and draws the histogram using numpy and turtle
def main():
    mags = readFile( "all_month_recent.csv" )
    hist, bins = np.histogram( mags )
    drawSetup( bins, 200, 3400 )
    drawBars( hist )

#used to run the main method automatically
if __name__ == "__main__":
    main()
