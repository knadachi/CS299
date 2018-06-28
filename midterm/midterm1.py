#Question 1
def calculate( name, base, *checks ):
    print( "Customer Name:", name )
    print( "Base Fee: $", end = "" )
    print( base )
    total = 0.0
    for check in checks:
        if check < 20:
            total += check * 0.10
        elif check > 20 and check <= 50:
            total += check * 0.07
        else:
            total += check * 0.05
    total += base
    print( "Total Service Fee: $", end = "" )
    print( total )
    return ( name, total )

#Question 2
def compare( list1, list2 ):
    if len( list1 ) != len( list2 ):
        print( "Lengths are not the same." )
    else:
        maxTagOne = None
        tuples = []
        for a,b in zip( list1, list2 ):
            tuples.append( (a, b,) )
            if b == 1:
                if maxTagOne == None or a > maxTagOne:
                    maxTagOne = a
        tuples.sort( key = lambda x: x[0] )
        tuplesEdit = []
        for tuple in tuples:
            if tuple[1] == 1:
                tuplesEdit.append( tuple )
        print( "Max Value with Tag 1:", maxTagOne )
        print( "Sorted Tuples:", tuples )
        print( "Sorted Tuples with Tag 1:", tuplesEdit )
        
#Test cases for Question 1
print( "------------" )
print( " Question 1" )
print( "------------" )
calculate( "Jack", 10, 15, 29, 18, 7 )
print()
calculate( "Joan", 10, 36 )
print()
calculate( "David", 20, 3, 5, 2, 6 )
print()
calculate( "Diana", 20 )
print()

#Test cases for Question 2
print( "------------" )
print( " Question 2" )
print( "------------" )
L1 = [ 13, 3, 25, 7, 21, 2, 50, 2, 13, 40, 34, 14, 6, 16 ]
L2 = [ 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1 ]
compare( L1, L2 )
print()
L1 = [ 45, 21, 4, 31, 2 ]
L2 = [ 1, 1, 1, 1, 1 ]
compare( L1, L2 )
print()
L1 = [ 13, 3, 45 ]
L2 = [ -1, -1, -1 ]
compare( L1, L2 )
