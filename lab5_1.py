#function that cleans list and returns elements without repeats

def clean_list(list_to_clean) :
	new_list = []	#list to be returned
	repeat = False	#additional boolean variable 
	for element in list_to_clean :	#for each element in list_to_clean
		for member in new_list :	#for each element in new_list
			if type(element) == type(member) and element == member :	#if elements are repeated
				repeat = True
		if not repeat :
			new_list.append(element)	#add element to new_list
		repeat = False
	return new_list
