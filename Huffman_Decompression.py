
file_name = "test_compressed.bin"

# read the code file
file = open(file_name[0:-15] + "_code.txt")
letter_dict = eval(file.read())
file.close()

file = open(file_name, "rb")
result = file.read()
print(result)
file.close()

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

# print(''.join(reverse_encoding(result, {b:a for a, b in letter_dict.items()})))