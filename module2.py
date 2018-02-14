"""
function for converting non-negative number from one notation to another 

convert_n_to_m([123], 4, 3) returns False
convert_n_to_m("0123", 5, 6) returns 102
convert_n_to_m("123", 3, 5) returns False
convert_n_to_m(123, 4, 1) returns 000000000000000000000000000
convert_n_to_m(-123.0, 11, 16) returns False
convert_n_to_m("A1Z", 36, 16) returns 32E7

"""
def convert_n_to_m(x, n, m) :
	
	#dictionary for storing symbols with their values for notations with base more then 10
	dictionary = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16,'H': 17,
	'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 
	'R': 27,'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

	#if x is not integer number or string
	if type(x) != int and type(x) != long and type(x) != str :
		return False
	#if x is negative
	elif (type(x) == int or type(x) == long) and int(x) < 0 :
		return False

	x = str(x).upper()	#all symbols in dictionary are upper-case
	length = len(x)
	power = length - 1	#the first power must be less than length by 1
	result = ""	#variable for resulting number
	x_decimal = 0	#variable for storing number in decimal notation
	for digit in x :	#for each digit in x
		if digit in dictionary and dictionary[digit] >= n :	#if digit is not less then power of notation
			return False
		elif digit not in dictionary and int(digit) >= n :	#if digit is not less then power of notation
			return False

	n = long(n)
	power = long(power)
	if n == 1 :	#if power of notation is 1
		x_decimal = length
	else :
		for digit in x :	#convert x to decimal
			if digit in dictionary :	#if digit is in dict
				x_decimal += long(dictionary[digit]) * long(pow(n, power))	#each iteration add digit * n^power to x_decimal 
			else :
				x_decimal += long(digit) * long(pow(n, power))	#each iteration add digit * n^power to x_decimal
			power -= 1	#increment power

	number = x_decimal	#next operations we'll do with number
	if m == 1 :	#if notation of m is 1
		result = number * "0"	#result = "0000..."
	else :
		while number > 0 :	#convert number in decimal notation to m-al notation
			add = number % m 	#remain of division number by m
			if add > 9 :	#if remain is more than 9
				for key in dictionary.keys() :	#for each key in keys
					if add == dictionary[key] :	#if remain = value of dictionary[key]
						result += str(key)	#add key to the result
			else :
				result += str(add)	#add remain to result
			number = number / m 	#division of number by m
	result = result[::-1]	#reverse the result
	if result == "" :	#if the number is 0/00/000...
		result += '0'
	return result
