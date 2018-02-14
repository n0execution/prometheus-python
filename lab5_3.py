"""
function for calculating superfibonacci numbers
it is a list of whole numbers with the property that,
every n term is the sum of m previous terms

super_fibonacci(2, 1) returns 1
super_fibonacci(3, 5) returns 1
super_fibonacci(8, 2) returns 21
super_fibonacci(9, 3) returns 57

"""
def super_fibonacci(n, m) :
	#checking for some special cases
	if n <= m or m == 1 :
		return 1

	#making list of [1, 1, 1...] with length of m
	new_list = [1 for x in range(m)]

	for i in range(m, n) :
		length = len(new_list)
		#appending the sum of m last elements to list
		new_list.append(sum(new_list[length - m :]))

	return new_list[n - 1]
