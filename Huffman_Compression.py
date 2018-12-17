# huffman nodes are [letter, number]

from PriorityQueue import *

# open file to be read
file = open("test.txt", "r")
text = file.read()

#check for empty text file
if text == "":
	print("Error: Empty Text")
else:
	letter_list = {text[0] : 1}

# place each letter into dictionary and count each letter
for x in range(1,len(text)):
	if text[x] in letter_list:
		letter_list[text[x]] = letter_list[text[x]] + 1
	
	else:
		letter_list[text[x]] = 1

priorityq = PriorityQueue()

# dictionary check
# for x in letter_list:	
	# print(x + " " + str(letter_list[x]))

# insert everything into priority queue
for x in letter_list:
	priorityq.add([x, letter_list[x]])
	
