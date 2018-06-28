#Question 1: Recursive function to reverse a string
def reverse( string ):
    if string == "":
        return ""
    else:
        return reverse( string[1:] ) + string[0]

#Question 2: Recursive function to display number sequence pattern
def pattern( num ):
    if num == 0:
        print( num, end = " " )
        return
    else:
        pattern( num - 1 )
        print( num, end = " " )
        pattern( num - 1 )

#Question 3: Generic search function using a specified comparison function
def generic_sort( function, aList ):
    return function( aList )

def descending( vals ):
    print( "Sorting list in descending order..." )
    for i in range( len( vals ) ):
        for j in range( 0, len( vals ) - i - 1 ):
            if vals[j] < vals[j+1]:
                temp = vals[j]
                vals[j] = vals[j+1]
                vals[j+1] = temp
    return vals

def alphabetical( vals ):
    print( "Sorting list in alphabetical order..." )
    for i in range( len( vals ) ):
        for j in range( 0, len( vals ) - i - 1 ):
            if vals[j] > vals[j+1]:
                temp = vals[j]
                vals[j] = vals[j+1]
                vals[j+1] = temp
    return vals

def alphabeticalTup( vals ):
    print( "Sorting tuple list in alphabetical order..." )
    for i in range( len( vals ) ):
        for j in range( 0, len( vals ) - i - 1 ):
            if vals[j][0] > vals[j+1][0]:
                temp = vals[j]
                vals[j] = vals[j+1]
                vals[j+1] = temp
            elif vals[j][0] == vals[j+1][0]:
                if vals[j][1] < vals[j+1][1]:
                    temp = vals[j]
                    vals[j] = vals[j+1]
                    vals[j+1] = temp
    return vals

#Question 4: Perform functions on a list of integers including doubling
#all values, squaring only odd elements, and finding all primes
def double( nums ):
    print( "Doubled values of elements in the list..." )
    return list( map( lambda x: x*2, nums ) )

def squareOdd( nums ):
    print( "Squared values of odd elements in the list..." )
    odd = list( filter( lambda x: x % 2 == 1, nums ) )
    return list( map( lambda x: x**2, odd ) )
    
def primes( nums ):
    print( "Prime elements in the list..." )
    return list( filter( isPrime, nums ) )

def isPrime( num ):
    if num <= 1:
        return False
    for i in range( 2, num ):
        if num % i == 0:
            return False
    return True

#Main function that contains the test cases
def main():
    print( "----------" )
    print( "Question 1" )
    print( "----------" )
    print( "abc ->", reverse( "abc" ) )
    print( "hello, world! ->", reverse( "hello, world!" ) )

    print( "\n----------" )
    print( "Question 2" )
    print( "----------" )
    for i in range( 0, 5 ):
        string = "pattern(" + str(i) + "): "
        print( string )
        pattern( i )
        print()

    print( "\n----------" )
    print( "Question 3" )
    print( "----------" )
    list1 = [5,2,12,4,9,13,22,1,6,17]
    list2 = ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta",
             "Alpine", "Samuel", "Bob", "Joy"]
    list3 = [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1),
             ("Alp", 2), ("Beta", 3), ("Alp", 1), ("Sam", 4),
             ("Bob", 2), ("Sam", 3)]
    print( generic_sort( descending, list1 ), "\n" )
    print( generic_sort( alphabetical, list2 ), "\n" )
    print( generic_sort( alphabeticalTup, list3 ), "\n" )

    print( "\n----------" )
    print( "Question 4" )
    print( "----------" )
    print( "Original List:" )
    L = list( range( 1, 101 ) )
    print( L, "\n" )
    print( double( L ), "\n" )
    print( squareOdd( L ), "\n" )
    print( primes( L ), "\n" )

if __name__ == "__main__":
    main()

'''
----------
Question 1
----------
abc -> cba
hello, world! -> !dlrow ,olleh

----------
Question 2
----------
pattern(0): 
0 
pattern(1): 
0 1 0 
pattern(2): 
0 1 0 2 0 1 0 
pattern(3): 
0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 
pattern(4): 
0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 4 0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 

----------
Question 3
----------
Sorting list in descending order...
[22, 17, 13, 12, 9, 6, 5, 4, 2, 1] 

Sorting list in alphabetical order...
['Alp', 'Alpine', 'Beta', 'Bob', 'Jolly', 'Joy', 'Kate', 'Kate', 'Sam', 'Samuel'] 

Sorting tuple list in alphabetical order...
[('Alp', 2), ('Alp', 1), ('Beta', 3), ('Bob', 2), ('Jolly', 1), ('Kate', 5), ('Kate', 3), ('Sam', 4), ('Sam', 3), ('Sam', 2)] 


----------
Question 4
----------
Original List:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100] 

Doubled values of elements in the list...
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200] 

Squared values of odd elements in the list...
[1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841, 961, 1089, 1225, 1369, 1521, 1681, 1849, 2025, 2209, 2401, 2601, 2809, 3025, 3249, 3481, 3721, 3969, 4225, 4489, 4761, 5041, 5329, 5625, 5929, 6241, 6561, 6889, 7225, 7569, 7921, 8281, 8649, 9025, 9409, 9801] 

Prime elements in the list...
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 
'''
