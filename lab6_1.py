#function for counting "holes" in numbers
def count_holes(n) :
	#amount of holes for each digit
	case = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 1, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1}
	count = 0	#variable for counting holes
	flag = True	#additional boolean variable
	number = ''	#string for storing number without zeros at the beginning
	if type(n) != long and type(n) != int : #n should be int or long
		if type(n) != str : #if n has other type than string
			return 'ERROR'
		else :
			if not n.isdigit() :	#if n is string it shouldn't consist real number 
				return 'ERROR'

	num = str(n)	#convert num into a string
	if len(num) == 1 and num == '0':	#if num is '0'
		return 1
	for digit in num :
		if digit == '0' and not flag :	#if digit is zero and not at the beginning of num
			number += digit
		elif digit != '0' :		#if digit is not '0' 
			number += digit
			flag = False

	for digit in number :	#counting amount of holes in number using dictionary case
		count += case[digit]
	return count
