import sys

if len(sys.argv) != 2 :
	print "error"
	exit()


string = sys.argv[1]
length = len(string)

for i in range(length) :
	num1 = string.find('(')
	num2 = string.find(')')

	if num1 < num2 and num1 != -1  and num2 != -1 :
		string = string.replace(string[num1], "", 1)
		num2 = string.find(')')
		string = string.replace(string[num2], "", 1)

if string == "" :
	print "YES"
else :
	print "NO"
