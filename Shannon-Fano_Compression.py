# nodes are [letter, number, code]

from PriorityQueue import *

# function to split a priority queue into two lists of equal (more or less) value and add code
def split_equal_list(priorityq, letter_dict):
	if len(priorityq.return_all()) > 1:

		priorityq1 = PriorityQueue()
		priorityq2 = PriorityQueue()

		temp1 = priorityq.pop()
		temp1[2] += "0"
		priorityq1.add(temp1)
		count0 = temp1[1]

		temp1 = priorityq.pop()
		temp1[2] += "1"
		priorityq2.add(temp1)
		count1 = temp1[1]

		while not priorityq.empty():
			temp1 = priorityq.pop()
			if count0 + temp1[1] - count1 < count1 + temp1[1] - count0:
				temp1[2] += "0"
				priorityq1.add(temp1)
				count0 += temp1[1]
			
			else:
				temp1[2] += "1"
				priorityq2.add(temp1)	
				count1 += temp1[1]

		return [split_equal_list(priorityq1, letter_dict), split_equal_list(priorityq2, letter_dict)]

	else:
		# save code into dictionary
		letter_dict[priorityq.return_all()[0][0]] = priorityq.return_all()[0][2]
		return priorityq.return_all()


#https://stackoverflow.com/questions/51425638/how-to-write-huffman-coding-to-a-file-using-python#51425774
# function to generate a byte array from a string of 1s and 0s
def _to_Bytes(data):
	b = bytearray()
	for i in range(0, len(data), 8):
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

priorityq = PriorityQueue()

# insert everything into priority queue
for x in letter_dict:
	priorityq.add([x, letter_dict[x], ""])

# generate shannon-fano code
tree = split_equal_list(priorityq, letter_dict)

for x,y in letter_dict.items():
	print(x + " " + y)


# create compressed version in text format
file = open(file_name[0:-4] + "_SFcompressed.txt", "w")

result = ""

for x in text:
	result = result + letter_dict[x]
	file.write(letter_dict[x])

file.close()


# create compressed version in bin format
file = open(file_name[0:-4] + "_SFcompressed.bin", "wb")

file.write(_to_Bytes(result))
file.close()

# create compression code in text format
file = open(file_name[0:-4] + "_SFcode.txt", "w")
file.write(str(letter_dict))
file.close()


#https://stackoverflow.com/questions/51425638/how-to-write-huffman-coding-to-a-file-using-python#51425774
#https://docs.python.org/3/tutorial/classes.html#iterators
from typing import Generator
def reverse_encoding(content, _lookup) -> Generator[str, None, None]:
	while content:
		_options = [i for i in _lookup if content.startswith(i) and (any(content[len(i):].startswith(b) for b in _lookup) or not content[len(i):])]
		if not _options:
			raise Exception("Decoding error")
		yield _lookup[_options[0]]
		content = content[len(_options[0]):]

print(''.join(reverse_encoding(result, {b:a for a, b in letter_dict.items()})))