"""
XOR with some hex value to get the result
this is done for finding if a particular entry has been 
encrypted using xor
get results of two or three values to see if encryption 
used is xor
"""

import binascii

asciiPchars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"\#$%&\\\'()*+,-./:;<=>?@[]^_`{|}~"
acsiiChars = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95', '\x96', '\x97', '\x98', '\x99', '\x9a', '\x9b', '\x9c', '\x9d', '\x9e', '\x9f', '\xa0', '\xa1', '\xa2', '\xa3', '\xa4', '\xa5', '\xa6', '\xa7', '\xa8', '\xa9', '\xaa', '\xab', '\xac', '\xad', '\xae', '\xaf', '\xb0', '\xb1', '\xb2', '\xb3', '\xb4', '\xb5', '\xb6', '\xb7', '\xb8', '\xb9', '\xba', '\xbb', '\xbc', '\xbd', '\xbe', '\xbf', '\xc0', '\xc1', '\xc2', '\xc3', '\xc4', '\xc5', '\xc6', '\xc7', '\xc8', '\xc9', '\xca', '\xcb', '\xcc', '\xcd', '\xce', '\xcf', '\xd0', '\xd1', '\xd2', '\xd3', '\xd4', '\xd5', '\xd6', '\xd7', '\xd8', '\xd9', '\xda', '\xdb', '\xdc', '\xdd', '\xde', '\xdf', '\xe0', '\xe1', '\xe2', '\xe3', '\xe4', '\xe5', '\xe6', '\xe7', '\xe8', '\xe9', '\xea', '\xeb', '\xec', '\xed', '\xee', '\xef', '\xf0', '\xf1', '\xf2', '\xf3', '\xf4', '\xf5', '\xf6', '\xf7', '\xf8', '\xf9', '\xfa', '\xfb', '\xfc', '\xfd', '\xfe', '\xff']

lst = [] # contains all 256 hex combinations
l = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
lst1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',':','/','.','~']

hexinput1 =( "cbd0d1759d87869c")
hexinput = ("cbd1d3d991")

hs = [] #list of hex format of input
for i in range(0,len(hexinput),2):
	hs.append(hexinput[i:i+2])
	
print str(hs)

for i in l:
	for j in l:
		lst.append(i+j)

xored = ""


# for i in lst:
	# xored += "Xoring with: 0x"+i+"\t"
	# for j in hs:
		# xored += chr(int("0x"+i,16)^int("0x"+j,16))
	# xored +="\n"
	# # f = open("Xor_combinations.txt",'ab')
	# # f.write(xored+"\n")
	# # f.close()
	# # xored = ""
# fo = open("Xor_combinations.txt",'wb')
# fo.write(xored)
# fo.close()

# for i in lst:
	# if chr(ord("w")^int(("0x"+i),16)) == '\x9c': # here 'M' is the testing value
		# print "XOR with : 0x"+i

		
		#j = list of xoring bytes
		#l = inputhex bytes i in hs
for i in hs:
	for j in lst:
		for k in acsiiChars:
			if chr(ord(k)^int(("0x"+j),16)) == chr(int("0x"+i,16)):	# 0x can be removed
				what =  hex(ord(k))
				witth = chr(int(("0x"+j),16))
				if witth in asciiPchars:
					fo = open("guessed.txt",'ab')
					txt = "0x"+i+":\t"+str(what)+"\t"+str(witth)+"\r\n"
					fo.write(txt)
					fo.close()
	fs = open("guessed.txt",'ab')
	fs.write("------------------------\n")
	fs.close()
		
