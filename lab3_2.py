#program for fibonacci numbers
import sys


n = int(sys.argv[1])	#n is the first argument

prev_1 = 0	#previous number 1
prev_2 = 1	#previous number 2

if n < 0 :
	print("Error. Negative number!")	#number cannot be negative
	result = None
elif n == 1 :
	result = 1
elif n == 0 :
	result = 0
else : 	#calculating fibonacci number for n
	for i in range(0, n - 1) :
		result = prev_1 + prev_2
		prev_1 = prev_2
		prev_2 = result

print(result)	#printing the result
