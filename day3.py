# #All the commands that I have covered so far
# #Practice Problems :
# # 1.Write a Python program to print the following string in a specific format (see the output). Go to the editor
# # Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

# # Twinkle, twinkle, little star,
# # 	How I wonder what you are! 
# # 		Up above the world so high,   		
# # 		Like a diamond in the sky. 
# # Twinkle, twinkle, little star, 
# # 	How I wonder what you are

# print("Twinkle, twinkle, little star")
# print(" 	How I wonder what you are!")
# print("Up above the world so high,")
# print(" 		Like a diamond in the sky.")
# print("Twinkle, twinkle, little star,")
# print("   How I wonder what you are")

# # Write a Python program to display the current date and time.
# # Sample Output :
# # Current date and time :
# # 2014-07-05 14:34:14

# print("Current date and time :\n2014-07-05 14:34:14" )

# #Write a Python program which accepts the radius of a circle from the user and compute the area.

# radius= int(input("Enter a number :"))
# area = (3.142*(radius**2))
# print("Area of the circle is :" , area)

# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
 
# first_name = (input("Enter your first name :")) 
# last_name = (input("Enter your last name :"))
# print("Result:"+ last_name + " " + first_name )

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)

#  Write a Python program to display the first and last colors from the following list. Go to the editor
# color_list = ["Red","Green","White" ,"Black"]

# colors = ["Red","Green","White" ,"Black"]
# print(colors[0] +" "+ colors[-1])

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615
 
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
