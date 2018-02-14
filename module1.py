#program for encoding inputted text by bacon
import sys

if len(sys.argv) != 2 :
	print "error"
	exit()

key = 'aaaaabbbbbabbbaabbababbaaababaab'	#key for encoding
alphabet = 'abcdefghijklmnopqrstuvwxyz'		#variable with alphabet
text = sys.argv[1] 	#inputted text in argument
new_text1 = ''	#text without whitespaces
new_text2 = ''	#text divided into parts of 5 symbols
new_text3 = ''	#text to decode using key
counter = 0	#additional variable which helps to divide text into parts
check = ''	#variable for searching some combination of 'a' and 'b' in key
result = ''	#resulting message


for letter in text :	#delete all whitespaces in text
	if letter != ' ' :
		new_text1 += letter 

for letter in new_text1 :	#divide text into parts of 5 symbols
	if counter % 5 != 0 :
		new_text2 += letter
		counter += 1
	else :
		if counter != 0 :
			new_text2 += ' '
		new_text2 += letter
		counter += 1


for letter in new_text2 :	#replace each lower case to 'a' and upper to 'b'
	if letter != ' ' :
		if letter.lower() == letter :
			new_text3 += 'a'
		else :
			new_text3 += 'b'
	else :
		new_text3 += ' '

counter = 1

for letter in new_text3 :	#decoding combination of 'a' and 'b' using key
	if counter % 6 != 0 :
		check += letter
		counter += 1
		if counter  % 6 == 0 :
			index = key.find(check)
			if index != -1 :
				result += alphabet[index]
			check = ''	
	else :	
		counter += 1

print result 	#printing the result 
