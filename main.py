# If = Do some code only IF some condition is True
# Else do somenthing else

age = int(input("Enter your age:"))


if  age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to sign up!")
else:
    print("Sorry! You are not signed up")