# BOOLEAN #
# Write a program to help you take care of your plants!
# A boolean variable called needs_water exists that represents whether or not one of your plants needs water. It is set to True and its value is being printed to the screen.
# Make another boolean variable called needs_to_be_repotted that represents whether or not you need to repot one of your plants. Set the value to False and print it to the screen.
# Your output should look like this:
# Needs water: True
# Needs to be repotted: False

needs_water = True
print("Needs water: " + str(needs_water))
needs_to_be_repotted = False
print("Needs to be reported :" + str(needs_to_be_repotted))

#  can_juggle = True

# The code below has problems. See if
# you can fix them!
# if can_juggle print("I can juggle!")
# else
# print("I can't juggle.")
# The right way is this : #

can_juggle = True

if can_juggle:
    print("I can juggle!")
else:
    print("I can't juggle.")


date = int(input("Enter today's day numerically:"))
if date<30:
    print("Sorry, not a payday.")
if date==30:
    print("It's payday!")

