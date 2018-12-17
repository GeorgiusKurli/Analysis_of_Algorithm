# huffman nodes are [letter, number]

from PriorityQueue import *

# recursive function used to assign code for each letter
def assign_code(tree, letter_dict, code = ""):
	
	# base case
	if isinstance(tree[0], str):
		letter_dict[tree[0]] = code
		return letter_dict

	# recursive case
	else:
		letter_dict = assign_code(tree[0][0], letter_dict, code + "0")
		return assign_code(tree[0][1], letter_dict, code + "1")


# open file to be read
file_name = "test.txt"
file = open(file_name, "r")
text = file.read()
file.close()

#check for empty text file
if text == "":
	print("Error: Empty Text")
else:
	letter_dict = {text[0] : 1}

# place each letter into dictionary and count each letter
for x in range(1,len(text)):
	if text[x] in letter_dict:
		letter_dict[text[x]] = letter_dict[text[x]] + 1
	
	else:
		letter_dict[text[x]] = 1

priorityq = PriorityQueue()

# insert everything into priority queue
for x in letter_dict:
	priorityq.add([x, letter_dict[x]])

flag = True

# building huffman tree
while flag:
	temp1 = priorityq.pop()
	temp2 = priorityq.pop()
	
	if priorityq.empty():
		flag = False

	templist = [[temp1,temp2], temp1[1]+temp2[1]]
	priorityq.add(templist)

# dictionary check
# for x in letter_dict:
# 	print(x + " " + str(letter_dict[x]))

letter_dict = assign_code(priorityq.pop(), letter_dict)

# dictionary check
# for x in letter_dict:
# 	print(x + " " + str(letter_dict[x]))

file = open(file_name[0:-4] + "_compressed.bin", "wb")
binary_array = []
for x in text:
	binary_array.append(int(letter_dict[x]))


file.write(bytearray(binary_array))
file.close()