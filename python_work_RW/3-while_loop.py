print
print "While Loops Exercise"
print

""" 

#
part 1

i = 13
while i > 14: # this is a while loop that will never be called as i<14
	print i 

# this is a while loop that will last forever cos i>14 and there is no change in i over time
i = 15
while i > 14: 
	print i 

# this is a while loop that changes over time
i = 15
while i > 0:
	print i
	i -= 1 # basically, i = i - 1
"""

# part 2

mylist = [23, 'hi', 2.4e-10]
count = 0
while count < 3:
	item = mylist[count]
	print item, mylist.index(item)
	count += 1

# part 3

x = ""
if x: print x, 'is True'
else: print 'False'

	

print
