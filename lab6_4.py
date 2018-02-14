"""
function for searching the most frequent word in text

find_most_frequent('Hello,Hello, my dear!') returns ['hello']
find_most_frequent('to understand recursion you need first to understand recursion...') returns ['recursion', 'to', 'understand']
функції: find_most_frequent('Mom! Mom! Are you sleeping?!!!') returns ['mom']

"""
def find_most_frequent(text) :
	alphabet = "abcdefghijklmnopqrstuvwxyz"	#additional variable of alphabet
	text = text.lower()	#convert all text to lower-case
	word = ""	#at the beginning word is empty
	times = {}	#dictionary for storing words with amount of their repeats
	result = []	#resulting list
	for symbol in text :	#iterate through each character of text
		#making a word
		if alphabet.count(symbol) == 1 :	
			word += symbol
		#add the word to dictionary
		elif word != "":
			#if the dictionary is empty or word is not in dictionary.times()
			if times == {} or not word in times.keys():
				times[word] = 1
			#if the word is in dictionary.keys()
			else :
				times[word] += 1
			#set to zero word-variable
			word = ""
	most_times = max(times.values())	#variable of the most-freqeuntly words
	#iterate through each key in keys
	for key in times.keys() :
		#if the value of key equals to most_times
		if times[key] == most_times :
			result.append(key)
	result = sorted(result)	#sort the resulting list
	return result
