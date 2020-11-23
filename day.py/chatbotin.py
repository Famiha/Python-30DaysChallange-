# Your chatbot should ask the user the following (minimum requirements for the grader) and then give answers depending on the answers the user inputs:

# at least 5 questions
# at least 2 if-elif-else statements
# the use of the random module and randomly generated numbers

#@ CODE SOLUTION @#

import random 

answer = input("How are you doing today?")
if answer=="Good"or answer=="good":
    print("We are glad you are good")
elif answer=="Bad":
    print("I am sorry for the bad day!")
else:
    print("Thats interesting!")

age = int(input("whats your age ?"))
if age>18:
    print("WOW, You are a adult now!")
elif age>=18:
    print("You are eligable!")
else:
    print("sorry You are too young.")
 
question= input("what is your favourite subject?")
if question=='science':
    print("WOW nice subject")
elif question=="english":
    print("Good choice")
else:
    print("Nice!")
x=random.randint(1,2)
if x==1:
    print("nice subject")
if x==2:
    print("wow")
else:
    ("AHA Very nice subject!!")

job= input('What do you want to be when you grow up?')
if job=="doctor":
    print('Wow! Its hard!')
elif job == "engineer":
    print("Cool, Nice choice.")
else:
    print("Nice career option!!") 
 

retire= int(input("What age do you want to retire?")) 
