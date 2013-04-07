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

def Info():
	'''this is information about previouse functions'''

	print '--------------------'
	print 'hashes.py :'
	print 'Part Of <SQL_easy>'
	print '--------------------'
	print 'Consist Of:'
	print '1-Encrypt function'
	print '''
		this function encrypt text that going
		to database to hashes for security it
		follow some Algorithms that go on (Two-Way)
		such as {base64, asciiHex, type7}.'''
	print '2-Decrypt function'
	print '''
		this function decrypt hashes that comming
		from database to your text follow. '''


def main():
	Info()


if __name__ == '__main__':
	main()



