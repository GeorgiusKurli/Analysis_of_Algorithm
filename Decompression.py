#https://stackoverflow.com/questions/51425638/how-to-write-huffman-coding-to-a-file-using-python#51425774
#https://docs.python.org/3/tutorial/classes.html#iterators
from typing import Generator
def reverse_encoding(content:str, _lookup) -> Generator[str, None, None]:
	while content:
		_options = [i for i in _lookup if content.startswith(i) and (any(content[len(i):].startswith(b) for b in _lookup) or not content[len(i):])]
		if not _options:
			raise Exception("Decoding error")
		yield _lookup[_options[0]]
		content = content[len(_options[0]):]


def decompress(file_name):

	# read the code file
	if file_name[-16:-14] == "SF":
		file = open(file_name[0:-17] + "_SFcode.txt")
		flag = True
	else:
		file = open(file_name[0:-19] + "_huffcode.txt")
		flag = False

	data = file.read()

	# find first occurence of {
	tempint = data.find("{")

	# slice to obtain bitcount
	bitcount = int(data[0:tempint])

	# slice to obtain dictionary
	data = data[tempint:]

	# evaluate str into dictionary
	letter_dict = eval(data)
	file.close()

	# read bin file
	file = open(file_name, "rb")
	binary_data = file.read()
	file.close()

	result = ""

	# adding up all bits found in the bin file
	for x in binary_data:
		# formats the integer into binary string with padding of 0 on the left until 8 char is reached
		result += format(x,"08b")

	# obtain last byte
	tempdata = result[-8:]

	# remove extra zeroes by calculating how many additional zeroes were added
	tempdata = tempdata[8-bitcount%8:]

	# removing last byte
	result = result[0:-8]

	# adding last byte with extra zeroes removed
	result += tempdata

	original_text = ''.join(reverse_encoding(result, {b:a for a, b in letter_dict.items()}))
	print(original_text)

	# write original file
	if flag == True:
		file = open(file_name[0:-17]+".txt", 'w')
	else:
		file = open(file_name[0:-19]+".txt", 'w')
		
	file.write(original_text)
	file.close()
