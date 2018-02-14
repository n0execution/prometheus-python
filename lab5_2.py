"""
function returns amount of different digits of b that are in a
counter(12345, 567) returns 1
counter(1233211, 12128) returns 2
 counter(123, 45) returns 0
"""
def counter(a, b) :
    count = 0
	flag = False	#additional boolean variable 
	str_a = str(a)
	str_b = str(b)

	new_str_a = ''
	new_str_b = ''

	new_str_a += str_a[0]
	new_str_b += str_b[0]


	#cleaning argument 1 from repeated members
	for i in str_a :
		for k in new_str_a :
			if i == k :
				flag = True
		if not flag :
			new_str_a += i
		flag = False
	print new_str_a

	#cleaning argument 2 from repeated members
	for i in str_b :
		for k in new_str_b :
			if i == k :
				flag = True
		if not flag :
			new_str_b += i
		flag = False
	print new_str_b

	#finding confirmity
	for i in new_str_b :
		if new_str_a.find(i) != -1 :
			count += 1
	return count
