import turtle

digits = { 0: "11000", 1: "00011", 2: "00101",
           3: "00110", 4: "01001", 5: "01010",
           6: "01100", 7: "10001", 8: "10010",
           9: "10100" }

#Sets up the turtle module
draw = turtle.Turtle()
draw.pensize( 3 )
draw.setheading( 90 )
draw.penup()
draw.setpos( -250, 0 )
draw.pendown()
draw.shape( "turtle" )

#Draws a short line
def drawShortLine():
    global draw
    draw.forward( 25 )
    draw.penup()
    draw.setpos( draw.xcor() + 10, draw.ycor() - 25 )
    draw.pendown()

#Draws a long line
def drawLongLine():
    global draw
    draw.forward( 50 )
    draw.penup()
    draw.setpos( draw.xcor() + 10, draw.ycor() - 50 )
    draw.pendown()

#Draws a single digit in the form of a barcode (short line for 0 and
#long line for 1)
def drawDigit( num ):
    for i in digits[ int( num ) ]:
        if i == "0":
            drawShortLine()
        else:
            drawLongLine()

#Moves the pen down
def reset():
    global draw
    draw.penup()
    draw.sety( draw.ycor() - 120 )
    draw.goto( -250, draw.ycor() )
    draw.pendown()

#Calculates the check digit of a given zipcode
def checkDigit( zipcode ):
    sum = 0
    for num in zipcode:
        sum += int( num )
    return str( ( 10 - sum ) % 10 )

#Draws the barcode for a given zipcode
def drawBarcode( zipcode ):
    print( "Now drawing barcode for", zipcode, end = "...\n" )
    drawLongLine()
    zipcode = str( zipcode ).replace( "-", "" )
    zipcode += checkDigit( zipcode )
    for num in zipcode:
        drawDigit( num )
    drawLongLine()
    reset()

#Test cases
drawBarcode( "55555-1237" )
drawBarcode( "91768-1234" )
drawBarcode( "20500-0000" )
print( "Done." )
        
