names = [ 'joe', 'tom', 'barb', 'sue', 'sally' ]
scores = [ 10, 17, 20, 18, 15 ]
ages = [ 20, 17, 19, 18, 22 ]

#Returns a dictionary given two lists.
def makeDict( list1, list2 ):
    return dict( zip( list1, list2 ) )

#Returns a set given two lists.
def makeSet( list1, list2 ):
    return set( zip( list1, list2 ) )

#Returns a frozen set given two lists.
def makeFrozenSet( list1, list2 ):
    return frozenset( zip( list1, list2 ) )

#Returns the intersection of two given sets.
def findIntersection( set1, set2 ):
    return set1.intersection( set2 )

#Returns the median score in the given dictionary.
def getMedianScore( scoreDict ):
    scoreList = list( dict( scoreDict ).values() )
    scoreList.sort()
    length = len( scoreList )
    if length % 2 == 0:
        return ( scoreList[ length//2 ] + scoreList[ (length//2)-1 ] ) / 2
    else:
        return scoreList[ length//2 ]

#Returns the score of the given name in the dictionary and -1 if the name is
#not in the dictionary.
def getScore( name, dictionary ):
    if name not in dict( dictionary ):
        print( name + " is not in the dictionary." )
        return -1
    else:
        return dict( dictionary )[ name ]

'''
Question 1
(a) True
(b) True
(c) TypeError: '>' not supported between instances of 'int' and 'str'
(d) [2, 3, 4, 5, 1, 0]
(e) False
(f) True
(g) False
(h) True
(i) True
(j) P
(k) [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
'''
print( "------------" )
print( " Question 1" )
print( "------------" )
print( "Answers to Question 1 are in my comments." )
print()

#Question 2
print( "------------" )
print( " Question 2" )
print( "------------" )
scoreDict = makeDict( names, scores )
print( scoreDict )
print()

#Question 3
print( "------------" )
print( " Question 3" )
print( "------------" )
set1 = makeSet( names, scores )
set2 = makeFrozenSet( names, ages )
print( "Set:", set1 )
print( "Frozen Set:", set2 )
print( "Intersection:", findIntersection( set1, set2 ) )
print()

#Question 4
print( "------------" )
print( " Question 4" )
print( "------------" )
scoreDict[ 'john' ] = 19    #adds new entry with name 'john' with score of 19
scoreDict[ 'sue' ] = 20     #sue's score is updated to 20 when attempting to add a new entry with the same name
scoreDict[ 'sally' ] = 19   #sally's score is updated to 19
del scoreDict[ 'tom' ]      #delete tom and his score

print("Names:\tScores:")
scoreDict = sorted( scoreDict.items() )
for item in scoreDict:
    print( item[0] + "\t" + str( item[1] ) )
print()

#Question 5
print( "------------" )
print( " Question 5" )
print( "------------" )
print( "Median Score:", str( getMedianScore( scoreDict ) ) )
print()

#Question 6
print( "------------" )
print( " Question 6" )
print( "------------" )
print( "Testing 'ana'..." )
print( "Score:", getScore( 'ana', scoreDict ) )
print( "Testing 'barb'..." )
print( "Score:", getScore( 'barb', scoreDict ) )

'''
------------
 Question 1
------------
Answers to Question 1 are in my comments.

------------
 Question 2
------------
{'joe': 10, 'tom': 17, 'barb': 20, 'sue': 18, 'sally': 15}

------------
 Question 3
------------
Set: {('sue', 18), ('tom', 17), ('barb', 20), ('sally', 15), ('joe', 10)}
Frozen Set: frozenset({('sue', 18), ('barb', 19), ('tom', 17), ('sally', 22), ('joe', 20)})
Intersection: {('tom', 17), ('sue', 18)}

------------
 Question 4
------------
Names:	Scores:
barb	20
joe	10
john	19
sally	19
sue	20

------------
 Question 5
------------
Median Score: 19

------------
 Question 6
------------
Testing 'ana'...
ana is not in the dictionary.
Score: -1
Testing 'barb'...
Score: 20
'''
