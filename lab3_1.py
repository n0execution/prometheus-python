import sys


a = float(sys.argv[1])	#a is the first argument
b = float(sys.argv[2])	#b is the second argument
c = float(sys.argv[3])	#c is the third argument

if (a + b > c) & (a + c > b) & (b + c > a) :
	print("triangle")	#two sides > than the other
else :
	print("not triangle")	#two sides <= than the other
