print
print "String Exercise" 
print

# part 1 - looping through strings

s = "i hate to write python" # a string

for item in s: # for loop to print each character in the s string
	print item

print "the 5th character is: ", s[4]
print "the last character is: ", s[-1]
print "the length of the string is: ", len(s)

print s[0], s[0][0], s[0][0][0] # printing the first item (exercise)

# part 2

string = "99 big red balloons floating through the bright blue sky"
split_string = string.split() # splits the string into seperate words

print "split_string: ", split_string # prints the split_string

for item in split_string: # for word in the split_string
	if item.find('b') > -1: # if letter "b" found, see below for explan.
		print "I found 'b' in:", item # print which word "b" was found in
	else:
		print "I didn't find the letter 'b' anywhere"

print "end of search"

"""
If you use item.find('b'), then it will return either a number greater than 0
if it has found the letter 'b', or it will return -1 if it didnt find the letter
anywhere. However, since python considers -1 to be "True", then you have to add
a variable which considers cases only where the result is > -1.
"""

# part 3

something = "completely different"
dir(something) # prints the directory of everything that can be done 
print "number of 't' characters: ", something.count('t')
print "location of 'plete': ", something.find("plete")
print something.find('e') # returns '5' as the first 'e' is at the 5th index
print something.find('e',6) # finds the next 'e' after the 5th index

something.split('e') # splits the word by the letter 'e'
thing2 = something.replace("different", "idiotic") # replace words in strings
print thing2

print thing2.lower()
print thing2.upper()
print thing2.title() # sets first letter of each word as upper case, rest as lower


print



