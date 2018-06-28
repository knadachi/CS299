#Question 1
class BinaryNumber:
    def __init__( self, val ):
        temp = ""
        for i in val:
            if i == str(0) or i == str(1):
                temp += i
        self.val = temp
        if self.val == "":
            self.val = "0"

    def value( self ):
        rev = self.val[-1::-1]
        val = 0
        exp = 0
        for i in rev:
            if i == str(1):
                val += ( 2**exp )
            exp += 1
        return val
            

#Test Cases
test1 = BinaryNumber( "11101" )
test2 = BinaryNumber( "" )
test3 = BinaryNumber( "01E1310x1" )
test4 = BinaryNumber( "E3x5k" )
print( test1.value() )
print( test2.value() )
print( test3.value() )
print( test4.value() )

'''
29
0
29
0
'''
