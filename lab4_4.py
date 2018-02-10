#finds all "lucky tickets" in range between two inputted numbers
#"lucky" are tickets which sum of first three digits equals to sum of three last
import sys

if len(sys.argv) != 3 :		#if number of arguments does not equal 3
	print "error1"
	exit()			#exit

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
new_string = ""		#variable for expanded number
count = 0	#variable for counting "happy" numbers

if a1 < 0 or a1 > a2 or a2 > 999999 :
	print "error2"
	exit()


while a1 <= a2 :
	string = str(a1)
	length = len(string)
	
	if length != 6 :
		for element in range(6 - length) :
			new_string += '0'
	new_string += string

	sum1 = 0 
	sum2 = 0

	for i in range(3) :
		sum1 += int(new_string[i])
	for j in range(3, 6) :
		sum2 += int(new_string[j])
	if sum1 == sum2 :
		count += 1

	a1 += 1
	new_string = ""

print count
