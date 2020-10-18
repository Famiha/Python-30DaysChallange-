# ## List ####  (Ordered & Changeable )##

# name = ("Arman","John", "Kamal","John","Clair","Karen","Samantha","")

# # # print(f"Here is the list of the name and the position is given below:\n Goalkeeper is {name[0]} \n Wrestler is {name[1]} \n Cricketer is {name[2]}")

# # name.pop()
# # print(name)

# number = [ 10, 30, 50, 60 , 24, 5, 9]
# number.sort()
# print(number)

## Tuples (Ordered & Unchangeable )

## Dictonaries (Unordered & Changeable )##

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(car['year'])



## Conditional Statement ##

# age = 18

# if age==18:
#     print('He is eligible for this content')
# else:
#     print('He is not eligbe! Turn 18 idiot')

## Write a code where user will give a number(input) 
# and you have predefined an another number.
#  If it matches with your number then print().
#  Else print('You failed')

### Write your code below  ###
# num = int(input("Enter a number:"))
# num_2 = 44 
# age = 12
# if num == num_2: 
#     if age>18:
#         print("Your guess was right")
#     else:
#         print('You are under age')
# elif num == 30:
#     print("Number was half right")
# else:
#     print("you failed")


## MATH, History, Biology , 2 sub( Add them Then take average if average 80 A+, 70 A, 65 A-, 60 B, 50 B- , else F)
# Math = int(input("Enter an number :"))
# History = int(input("Enter an number :"))
# Biology = int(input("Enter an number :"))
# Arts =  int(input("Enter an number :"))
# Chemistry =  int(input("Enter an number :"))

# avg = (Chemistry + Arts + Biology + History + Math)/5 
# print(avg)
# if avg >= 80 :
#     print('You got A+')
# elif avg <= 70 :
#     print('You got A')
# elif avg <= 65 :
#     print('You got A-')
# elif avg <= 60:
#     print('You got B ')
#  elif avg <= 50 :
#     print('You got a B-')
# else :
#     print('Sorry Idiot You fail')



# price of house is 1 million dollars. If buyer has good credit , they need to put down  10 %.
#Otherwise they need to put down 20 %. Print the down payment.

# price = 1000000
# has_good_credit = False


# if has_good_credit:
#     print(0.1 * price)
# else :
#     print(0.2 * price)


# age gender 
# age = int(18)
# gender_is_male = True
# gender_is_female = True
# if age >= 18:
#     if gender_is_female:
#         print("You are eligable")
#     else:
#         print("Sorry your gender isn't correct")
# else:
#     print("You're under age")

# when is a number even?

user_input = int(input("Enter an number :"))
reverse = reversedint((user_input))
print('reverse:')
