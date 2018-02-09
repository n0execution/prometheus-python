import sys

number = len(sys.argv) - 1

new_string = ''
new_list = sys.argv[:0:-1]

for i in new_list :
	new_string += i
	if i != new_list[number - 1] :
		new_string += ' '

print new_string
