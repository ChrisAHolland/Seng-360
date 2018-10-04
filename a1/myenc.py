'''
Chris Holland
V00876844
'''

from Crypto.Cipher import AES
import sys

plaintext = 'This is a top secret.'
ciphertext = '764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2'.decode('hex')
IV = 'aabbccddeeff00998877665544332211'.decode('hex')
filename = 'words.txt'
f = open(filename, 'r')

for line in f:
	line = line.strip('\n')
	
	if len(line) < 16:
		key = line + ('#'*(16-len(line)))

	aes = AES.new(key, AES.MODE_CBC, IV)
	cipher = aes.decrypt(ciphertext)
	cipher = cipher[:21]
	
	if cipher == plaintext:
		print(line)
		sys.exit()	

