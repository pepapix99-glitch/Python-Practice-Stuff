'While Loops = statement that will execute its block of code as long as it remains true. once the condition becomes true, it executes.'
#Note!! >> unlimited

#name = ""

#while 1==1:
#    print("em stuck!")

#while len(name) == 0:
#    name = input("What's your name? ")

#print("Hello "+ name)

#====================================

'For loop = a statement that will execute its block of code a limited amount of times'
#Note!! >> limited

#for i in range(10):
#    print(i)
# the i is short for Index, it's a variable. could be anything
# "in" literally means inside. "from in" or "put it in"

#for i in range(50, 100):
#    print(i)

#for i in "Pepa Pix":
#    print(i)

#import time
# "time" is a module imported. this module allows stuff bout time functions and delays
# "import" keyword that brings in modules

#for seconds in range(10, 0, -1):
#    print(seconds)
#    time.sleep(1)
#print("Happy New Year!!")
# "sleep" function that pauses the program according to the number indicated

#====================================================
'Nested loops = loop in a loop'
'             = INNER loop will finish all of its interactions before finishing one iteration of the OUTER loop'

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input("Type any symbol because why not: ")

#for i in range(rows): 
#    for j in range(columns):
#        print(symbol, end="")
#    print()

#for stuff in range(rows):
#    for this in range(columns):
#        print(symbol, end="")
#    print()
#======================================================
'Loop Control Statements = changes a loop from its normal sequence'

'break = used to BREAK the loop entirely'
'continue = skips to the next iteration of the loop'
'pass = does nonthing, just acts as a placeholder'

'(BREAK)'
#(keep the first letter capitalized when saying True/False)

#name = input("Speak thou name!!: ")

#while True:
#    name = input("Speak thou name!!: ") 
#    if name != "":
#        break

'(CONTINUE)'
#phone_number = input("What's your phone number?: ")   

#for i in phone_number:
#    if i == "-":
#        continue
#    print(i, end="")

'(PASS)'

#for i in range(1,21):
#    if i ==13:
#        pass
#    else:
#        print(i)
#====================================================