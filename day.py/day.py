#Write a program to enter a number and test if it is greater than 45.6. 
#If the number entered is greater than 45.6, the program needs to output the phrase Greater than 45.6.

# @ CODE SOLUTION @ #

# num = int(input('Enter a number: '))
# if num < 45.6: 
#     print("Less than 45.6")
# else:
#     print("Greater than 45.6")

#Test if a number grade is an A (greater than or equal to 90). If so, print "Great!".#

# @ CODE SOLUTION @ #

# grade = int(input("Enter a grade "))
# if grade >= 90:
#     print("Great! ") 
# else:
#     ("Better luck next time champ!")

# Test if a password entered is correct. The secret phrase is Ada Lovelace.
# @ CODE SOLUTION @ #

# password = input("Enter the password :")
# if password =="Ada Lovelace":
#     print("Correct!")
# if password!="Ada Lovelace":
#     print("Not correct")
                        # BOOLEANS AND IF STATEMENTS !! 
# Test if a date is a payday based on the day of the month (15th or the 30th).
# Enter today's day numerically: 17
# Sorry, not a payday.
# Enter today's day numerically: 30
# It's payday!

# @ CODE SOLUTION @ #
# date = int(input("Enter today's day numerically:"))
# if ((date == 15) or (date == 30)):
#     print("It's payday!")
# if(not((date==15) or (date==30))):
#     print("Sorry, not a payday.")

# Ask the user to enter a number for red, green, and blue components of an RGB value, which takes a certain amount of red, green, and blue colors and produces a new color. Test the numbers that are input by the user and check that each value is between 0 and 255 (inclusive). If a color's value is outside of this range, print which color's number is not correct (e.g., "Red number is not correct" if the red value is 300). Multiple colors may be out of range.
#  The order of the colors should be the same as the sample runs below; red, then green, then blue.

 # @ CODE SOLUTION @ #
# red = int(input("Enter the red:"))
# green = int(input("Enter the green:"))
# blue =int(input("Enter the blue:"))

      
# if (not ((red >=0) and (red <=255))):
#         print("Red number is not correct")

       
# if (not ((green >=0)and (green <=255))):
#         print("Green number is not correct")

# if (not ((blue >=0)and (blue <= 255))):
#         print("Blue number is not correct")

# More if-else statement expample code :
# Input a word. If it is "yellow," print "Correct."
#  Otherwise, print "Nope." What happens if you type in "YELLOW" or "YellOW?" Does the capitalizing make a difference?

# color = input("What color?")

# if color == "yellow":
#     print("Correct")
    
# else:
#     print("Nope")

# Write a program to convert a fraction to a decimal. Have your program ask for the numerator first, then the denominator. 
# Make sure to check if the denominator is zero. If it is, print out "Error - cannot divide by zero."
 # @ CODE SOLUTION @ #
     
# num=int(input("Numerator:"))

# den=int(input("Denominator:"))
# if (den !=0):
#     print("Decimal:" + str(num/den))
# else:
#     print("Error - cannot divide by zero.")

# Input a grade number [9-12] and print Freshman, Sophomore, Junior, or Senior. 
# If it is not in [9-12], print Not in High School.
 # @ CODE SOLUTION @ #
grade = int(input("What grade are you in?"))

if(grade == 9):
    print("Freshman")
elif(grade == 10):
    print("Sophomore")
elif(grade == 11):
    print("junior")
elif(grade ==12):
    print("Senior")
else:
    print("Not in High School")

