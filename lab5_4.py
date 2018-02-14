"""
function for searching file in folder

file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt') returns 'C:/ideas.txt'
file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], \
'find.me') returns False
file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', \
['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', \
['user3', ['temp'], ], 'hey.py'], 'hereiam.py') returns '/home/user2/desktop/new folder/hereiam.py'

"""
def file_search(folder, filename) :
	#first element of list is the name of folder
	address = folder[0]
	if filename in folder : 	#if file exists in this folder
		address = address + '/' + filename
		return address
	for directory in folder : #searching file in internal folders
		if type(directory) == list :
			new_address = file_search(directory, filename)		#recursion
			if new_address != False :	#if file was found in directory
				address = address + '/' + new_address
				break
	#if file was not found
	if address == folder[0] :
		return False
	#if file is found
	else :
		return address
