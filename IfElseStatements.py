'If statement = executes if condition is true'

age = int(input("How old are you?: "))

if age == 40:
    print("dinosaur")
#executes when true, if false it proceeds to elif
elif age >= 30:
    print("fuck, you're old!")
elif age < 0:
    print("yo dad hasn't shot you out yet!")
#executes when true, if false it proceeds to else
else:
    print("haha, squirt!")
#when everything else is false, it ends up here
