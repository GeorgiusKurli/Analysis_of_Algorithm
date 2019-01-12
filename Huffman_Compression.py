# nodes are [letter, number]

from PriorityQueue import *

# recursive function used to assign code for each letter
def assign_code(tree, letter_dict, code = ""):
	
	# base case checks if a letter is found
	if isinstance(tree[0], str):
		# assign code into dictionary for the letter
		letter_dict[tree[0]] = code
		return letter_dict

	# recursive case
	else:
		letter_dict = assign_code(tree[0][0], letter_dict, code + "0")
		return assign_code(tree[0][1], letter_dict, code + "1")


#https://stackoverflow.com/questions/51425638/how-to-write-huffman-coding-to-a-file-using-python#51425774
# function to convert a string of 1s and 0s into bytes
# if bytes is not filled, zeroes will be added
def _to_Bytes(data):
	b = bytearray()
	for i in range(0, len(data), 8):
		# add a byte into the bytearray
		b.append(int(data[i:i+8], 2))
	return bytes(b)


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

priorityq = ReversePriorityQueue()

# insert everything into priority queue
for x in letter_dict:
	priorityq.add([x, letter_dict[x]])

flag = True

# building huffman tree
while flag:
	# take 2 lowest nodes
	temp1 = priorityq.pop()
	temp2 = priorityq.pop()
	
	# check if 2 nodes are left
	if priorityq.empty():
		flag = False

	# combine the two nodes and place it back into the priority queue
	templist = [[temp1,temp2], temp1[1]+temp2[1]]
	priorityq.add(templist)

# assign code for each letter and store into dictionary
letter_dict = assign_code(priorityq.pop(), letter_dict)


# create compressed version in text format
file = open(file_name[0:-4] + "_huffcompressed.txt", "w")

result = ""

for x in text:
	result = result + letter_dict[x]
	file.write(letter_dict[x])

file.close()

# create compressed version in bin format
file = open(file_name[0:-4] + "_huffcompressed.bin", "wb")
file.write(_to_Bytes(result))
file.close()



# create compression data(bitcount dictionary) in text format
file = open(file_name[0:-4] + "_huffcode.txt", "w")
file.write(str(len(result)))
file.write(str(letter_dict))
file.close()

print(letter_dict)
print(result)