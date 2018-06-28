"""
This function allows the user to continuously enter positive integers until they
enter a negative number or 0. Returns the number of integers entered, the max value,
and the min value.
"""
def numbers():
    nums = []
    count = 0
    maximum = 0
    minimum = 0
    print( "Enter a negative number or '0' to calculate!" )
    num = int( input( "Enter a number: " ) )
    while num > 0:
        nums.append( num )
        count += 1
        num = int( input( "Enter a number: " ) )
    if count > 0:
        maximum = max( nums )
        minimum = min( nums )
    return ( count, maximum, minimum )
"""
This function calculates prints the sales receipt and finds the total cost given the
item name, sales tax rate, and list of purchase prices.
"""
def receipt( name, tax, *args ):
    print( "Name:", name )
    print( "Sales Tax:", str(tax), "%" )
    total = 0
    for arg in args:
        total += arg
    total = round( float( total + (total*tax) / 100 ), 2 )
    print( "Total Cost:", str( total ) )

"""
The main function handles the UI of the program and tests each function.
"""
def main():
    #test cases for min/max function
    for i in range(0,3):
        count, maximum, minimum = numbers()
        print( "Count:", count, "// Max:", maximum, "// Min:", minimum )
        print()
    #test cases for sales receipt function
    print( "===============================================\n" )
    receipt( "Fruits", 8, 80, 125, 45.5 )
    print()
    receipt( "Furniture", 10.5, 950 )
    print()
    receipt( "Toys", 7.5, 12, 5.5, 6.5, 7.5, 9.0 )

if __name__ == "__main__":
    main()

"""
Enter a negative number or '0' to calculate!
Enter a number: 0
Count: 0 // Max: 0 // Min: 0

Enter a negative number or '0' to calculate!
Enter a number: 5
Enter a number: -1
Count: 1 // Max: 5 // Min: 5

Enter a negative number or '0' to calculate!
Enter a number: 5
Enter a number: 6
Enter a number: 12
Enter a number: 8
Enter a number: 2
Enter a number: 18
Enter a number: 21
Enter a number: 3
Enter a number: -5
Count: 8 // Max: 21 // Min: 2

===============================================

Name: Fruits
Sales Tax: 8 %
Total Cost: 270.54

Name: Furniture
Sales Tax: 10.5 %
Total Cost: 1049.75

Name: Toys
Sales Tax: 7.5 %
Total Cost: 43.54
"""
