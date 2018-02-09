import sys

string = sys.argv[1].lower()


new_string = ''
for letter in string :
	if letter != ' ' :
		new_string += letter

if new_string == new_string[::-1] :
	print "YES"
else :
	print "NO"
