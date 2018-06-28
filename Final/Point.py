#Question 2
class Point:
    def __init__( self, xc=0, yc=0 ):
        self.x = xc
        self.y = yc

    def setx( self, xc ):
        self.x = xc

    def sety( self, yc ):
        self.y = yc

    def get( self ):
        return( self.x, self.y )

    def move( self, dx, dy ):
        self.x = self.x + dx
        self.y = self.y + dy

    def __eq__( self, other ):
        return self.x == other.x and self.y == other.y

    def __add__( self, other ):
        tempx = self.x + other.x
        tempy = self.y + other.y
        return Point( tempx, tempy )

p1 = Point( 3, 5 )
p2 = Point( 0, 0 )
print( "P1 =", p1.get() )
print( "P2 =", p2.get() )
p2.move( 3, 5 )
if( p2 == p1 ):
    print( "two points together" )
else:
    print( "two points apart" )
p3 = p1 + p2
print( "P3 is:", p3.get() )

'''
P1 = (3, 5)
P2 = (0, 0)
two points together
P3 is: (6, 10)
'''
