"""
function for searching saddle-point of matrix

1 2 3
3 2 1
saddle_point([[1,2,3],[3,2,1]]) returns False

8 3 0 1 2 3 4 8 1 2 3
3 2 1 2 3 9 4 7 9 2 3
7 6 0 1 3 5 2 3 4 1 1
saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]]) returns (1, 2)

21
saddle_point([[21]]) returns (0, 0)

"""
def saddle_point(matrix) :
	result = ()	#the result must be tuple with indexes of saddle
	new_list = []	#aditional list
	index1 = 0	#index of saddle by rows
	length = len(matrix)	#length of matrix
	if length == 1 :
		return (0, 0)


	for row in matrix :	#for each row in matrix
		n_of_row = 0	#additional variable for rows
		saddle_matrix = []	#additional list for containing column
		saddle_min = min(row)	#minimal element of row
		if row.count(saddle_min) == 1 :	#if there is only one minimal element in row
			index2 = row.index(saddle_min)	#index of minimal element of this row by columns
			for row in matrix :	#making a list containing a saddle-column
				saddle_matrix.append(matrix[n_of_row][index2])	
				n_of_row += 1
			saddle_max = max(saddle_matrix)	#maximum of saddle-column
			#if there is only one maximum element of column and it equals to our saddle-element
			if saddle_matrix.count(saddle_max) == 1 and saddle_min == saddle_max :
				new_list.append(index1)
				new_list.append(index2)
				result = tuple(new_list)	#convert resulting list to tuple
		index1 += 1	#incrementing index1
	if result  :
		return result
	else :
		return False
