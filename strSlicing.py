'Slicing = creating a substring by extracting elements form another string'
#note, you can use either of these stuff:
'indexing[]     or      slice()'
#used for slicing objects
#three optional arguments are = [start(inclusive):stop(exclusive):step(hopscotch on steroids)]

name = "Pepa Pix"

'START INDEX'
#note!! >> the first index is always zero(0)
#note!! >> the first index is inclussive while the last is exclussive so ya gotta count extra, dont be dumb.
#   example >>  1.) first_half = name[0:4]
#                   output: Pep
#               2.) first_half = name[0:5]
#                   output: Pepa

first_half = name[0:5]
#if lazy, this works too. shit's the same output: first_half = name[:5]
second_half = name[5:8]
#if lazy, just do this. same shit: second_half = name[5:]

'STEP'
step_whut = name[0:8:3]
#confusing skip counting, hopscotch on steroids
#basically it hops over characters, in this case it's 3 so when it lands on the 3rd letter is what's gon be displayed
'index'
#   0   1   2   3   4   5   6   7
#   P   e   p   a   _   P   i   x
#   ^   -   -   ^   -   -   ^   -
#   |land       |land       |land
'output = Pai'

'fun addition, makes stuff reversed'
backwards = name[7::-1]
#note! >> the first letter is always assigned zero(0) that's why [0:8:-1] wont work
#if lazy this works too: backwards = name[::-1]

#print(backwards)

'SLICING'

website = "http://potato.com"
website2 = "http://dumdum.com"
webname = slice(7,-4)

print(website[webname])
print(website2[webname])
#bruh, remember to use the names you assigned variables to.
