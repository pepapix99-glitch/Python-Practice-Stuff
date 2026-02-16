'Logical Operators: (and, or, not) used to check if two or more conditional statements'

temp = int(input("What is the temperature outside?: "))

#note!! =>> (AND) is used when both statements are true   
if temp >= 0 and temp <= 30:
    print("the temparature is good today!")
    if temp >= 26:
        print("eugh, it hot!!")
    elif temp <= 25:
        print("damn it cold!!")
    print("Time to touch grass boi.")

#note!! =>> (OR) only one needs to be true
elif temp < 0 or temp > 30:
    print("temperature is cray cray!!")
    if temp < 0:
        print("WEAR 5 LAYERS OF SWEATERS!!")
    elif temp > 30:
        print("THE FIRES OF HELL IS SURFACING!!")
    print("THE RAPTURE IS HERE!!")

#note!! =>> (NOT) flips true statements to false and vice versa
#can surround one or more conditional statements
#me no likey this inverted crap
#if not(temp >= 0 and temp <= 30):
#    print("temperature is cray cray!!")
#    if temp < 0:
#        print("WEAR 5 LAYERS OF SWEATERS!!")
#    elif temp > 30:
#        print("THE FIRES OF HELL IS SURFACING!!")
#    print("THE RAPTURE IS HERE!!")
#elif not(temp < 0 or temp > 30):
#    print("the temparature is good today!")
#    if temp >= 26:
#        print("eugh, it hot!!")
#    elif temp <= 25:
#        print("damn it cold!!")
#    print("Time to touch grass boi.")
