#international morse-code
morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--.."
}


"""
function for encoding text to morse 

encode_morze('Morze code') returns ^^^_^^^___^^^_^^^_^^^___^_^^^_^___^^^_^^^_^_^___^_______^^^_^_^^^_^___^^^_^^^_^^^___^^^_^_^___^
encode_morze('Prometheus') returns ^_^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^^^_^^^___^___^^^___^_^_^_^___^___^_^_^^^___^_^_^
encode_morze('SOS') returns ^_^_^___^^^_^^^_^^^___^_^_^

"""

def encode_morze(text) :
 	morse = ""    #variable for encoded morse-code
  	index1 = 0   #variable to iterate through each part in morse-code of word
    #making text upper-case
	text = str(text).upper();  
	length1 = len(text)    #the length of text
	for symbol in text :   #iterate through each character
		index2 = 0    #variable to iterate through each symbol in morse-code of letter
		if symbol in morse_code : #if symbol is alphabetic
			letter_code = morse_code[symbol] #code of this letter in morse
			length2 = len(letter_code)   #length of letter-code
			for s in letter_code :   #iterate through each symbol in morse-code of letter
				#change "." to "^"
                if s == "." :  
					morse += "^"
                #change "-" to "^^^"
				elif s == "-" :
					morse += "^^^"
                #two symbols of morse-code contain each other with "_"
				if index2 != length2 - 1 :
					morse += "_"
				index2 += 1 #increment index2
            #two letters contain each other with "___"
			if index1 != length1 - 1 and index2 != length2 - 1 and text[index1 + 1] in morse_code or text[index1] == "-":
				morse += 3 * "_"
        #two words contain each other with "_______"
		if symbol == " " :
			morse +=  7 * "_"
		index1 += 1   #increment index1
	return morse
