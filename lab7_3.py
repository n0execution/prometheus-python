#class which inherits str-type and has two new methods
class SuperStr(str) :
	def __init__(self, string) :
		self.string = string

	#function for defining whether can the string variable be received by multiple entire s
	def is_repeatance(self, s) :
		if type(s) != str or s == "" or self.string == "":	#s must be only str-type and we don't consider empty strings
			return False

		len_str1 = len(self.string)	#length of string
		len_str2 = len(s)	#length of s
		repeats = len_str1 / len_str2	#the number of repeats s in string
		if s * repeats == self.string :	#if s multiplied by repeats times equals string
			return True
		else :	#if we receive another string
			return False


	#function for defining whether the string is palindrom
	def is_palindrom(self) :
		length = len(self.string)	#length of string
		if length % 2 == 0 :	#if length is even
			if self.string[: length / 2].lower() == self.string[length / 2 :][::-1].lower() :	#if first half equals second half
				return True
			else :	
				return False
		else :	#if length is odd 
			if self.string[: length / 2].lower() == self.string[length / 2 + 1 :][::-1].lower() :	#if first half equals second
				return True
			else :
				return False




#EXAMPLES


"""
s = SuperStr('123123123123')
print s.is_repeatance('123') # True
print s.is_repeatance('123123') # True
print s.is_repeatance('123123123123') # True
print s.is_repeatance('12312') # False
print s.is_repeatance(123) # False

s3 = SuperStr('mystring1Gnirtsym')
print s3.is_palindrom()
"""
