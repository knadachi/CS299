import string
import random

#Uses the provided key to encrypt the given plaintext using substitution cipher
def substitutionEncrypt( plainText, key ):
    alphabet = string.ascii_lowercase
    encrypted = ""
    for i in plainText:
        index = alphabet.index( i )
        encrypted += key[ index ]
    return encrypted

#Generates and returns a random key by shuffling the US alphabet
def keyGen():
    key = list( string.ascii_lowercase )
    random.shuffle( key )
    return ''.join( key )

#Prints the key used, the original strings, and their encryptions
def testDrive( key, *texts ):
    if key == "":
        key = "bpzhgocvjdqswkimlutneryaxf"
    print( "Key:", key )
    for text in texts:
        print( " ", text, "->", substitutionEncrypt( text, key ) )

#Test cases
print( "-------\nTest 1:\n-------" )
testDrive( "", "face", "blow" )
print( "\n-------\nTest 2:\n-------" )
testDrive( keyGen(), "face", "blow" )
print( "\n-------\nTest 3:\n-------" )
testDrive( "", "wonderful", "python", "java", "doedlugvusu" )
print( "\n-------\nTest 4:\n-------" )
testDrive( keyGen(), "wonderful", "python", "java", "doedlugvusu" )

'''
-------
Test 1:
-------
Key: bpzhgocvjdqswkimlutneryaxf
  face -> obzg
  blow -> psiy

-------
Test 2:
-------
Key: vjzlaciqyngudbksmhoxtfrwep
  face -> cvza
  blow -> jukr

-------
Test 3:
-------
Key: bpzhgocvjdqswkimlutneryaxf
  wonderful -> yikhguoes
  python -> mxnvik
  java -> dbrb
  doedlugvusu -> highsecrete

-------
Test 4:
-------
Key: ympbrxhovltdqznkjciawufges
  wonderful -> fnzbrcxwd
  python -> keaonz
  java -> lyuy
  doedlugvusu -> bnrbdwhuwiw
'''
