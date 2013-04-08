#! /usr/bin/env python

#This script is a part of SQL_easy
#written by DiaaDiab


import sys

try:
	from passlib.hash import cisco_type7
except:
	print '[*]Install Module <passlib> for python.'
	sys.exit()


def Encrypt(algo, text):
	'''(algo, text) > hashes'''

	if algo == 'base64':
		return text.encode('base64')

	if algo == 'asciiHex':
		return text.encode('hex')

	if algo == 'type7':
		return cisco_type7.encrypt(text)


def Decrypt(algo, hashed):
	'''(algo, hashed) > text'''

	if algo == 'base64':
		return hashed.decode('base64')

	if algo == 'asciiHex':
		return hashed.decode('hex')

	if algo == 'type7':
		return str(cisco_type7.decode(hashed))

def main():
    pass

if __name__ == '__main__':
	main()



