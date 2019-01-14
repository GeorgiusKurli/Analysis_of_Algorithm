from Huffman_Compression import *
from ShannonFano_Compression import *
from Decompression import *

flag = True
while flag:
	answer = input("1.Huffman compression 2.Shannon-Fano compression 3.Decompress 4.Exit\n")

	if answer == "1":
		answer = input("Please input file name\n")
		huffman_compression(answer)

	elif answer == "2":
		answer = input("Please input file name\n")
		sf_compression(answer)

	elif answer == "3":
		answer = input("Please input file name\n")
		decompress(answer)

	elif answer  == "4":
		flag = False
	