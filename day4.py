# Loops 
#Loops basically means repeating numbers and strings

#   FOR LOOP  #
# For loop is used for printing something like a list 
#or a tuple all at a same time
## Break statement ##
# This statement stops from printing the loop#

###  To write a loop ###
# for x in fruits :

languages = ["Python","Java","C+"]
for x in languages:
    print(x , end=" ") ## end=" " is for adding everything in a same line.

languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "C#":


        print(language + " found")
        break

numbers = [1,2,34,5,46,62,6,77,3347,743,7788,8,88,99,9]
for num in numbers:
    if num == 1 or 56 or 77 or 99:
        print("You Got it")
        break


 