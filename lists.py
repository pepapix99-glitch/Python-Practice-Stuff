'LIST = used to store multitple items in a single variable'

stuff = ["shampoo", "conditioner", "soap", "motor oil", "peanutt butter"]
#all the things inside a list is called ELEMENT
stuff[3] = "lotion"
#print(stuff[3])

stuff.append("moisturizer")
#(APPEND)adds element

stuff.remove("conditioner")
#(REMOVE)removes the element

stuff.pop()
#(POP)removes the last element

#stuff.clear()
#(CLEAR)duh, clears the list

for things in stuff:

    print(things)
