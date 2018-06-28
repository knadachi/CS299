#Weight and Height inputted by user
weight = float( input( "Enter weight in pounds: " ))
height = float( input( "Enter height in inches: " ))

#BMI calculated using given weight and height
bmi = round( weight / (height**2) * 703, 1 )
print( "BMI: ", bmi )

#uses the calculated BMI to determine status
if bmi < 18.5:
    print( "Status: Underweight" )
elif bmi <= 24.9:
    print( "Status: Normal" )
elif bmi <= 29.9:
    print( "Status: Overweight" )
else:
    print( "Status: Obese" )

"""
========
 Output
========

Enter weight in pounds: 160
Enter height in inches: 80
BMI:  17.6
Status: Underweight

Enter weight in pounds: 160
Enter height in inches: 70
BMI:  23.0
Status: Normal

Enter weight in pounds: 160
Enter height in inches: 65
BMI:  26.6
Status: Overweight

Enter weight in pounds: 160
Enter height in inches: 60
BMI:  31.2
Status: Obese
"""
