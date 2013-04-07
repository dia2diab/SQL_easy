#! /usr/bin/env python

#This script is a part of SQL_easy
#written by DiaaDiab

import sys


try:
	import MySQLdb
except:
	print '[*]Install Module <MySQL> for python.'


HostName = None   # remove None and set your host of MySQL server
UserName = None   # remove None and set user of MySQL server
PassWord = None   # remove None and set password of MySQL server

def InitConnection():
	'''set things to connect to MySQL'''

	global HostName
	global UserName
	global PassWord


	if None in (HostName, UserName, PassWord):
		print '[*]you must verify variables in setting.py to allow'
		print '[*]programme to connect to MySQL>Line number (15, 16, 17)'
		sys.exit()

	try:
		MyConnection = MySQLdb.connect(
			host = HostName,
			user = UserName,
			passwd = PassWord,
			)

		Cursor = MyConnection.cursor()
		print '[+]Connection done.'
		print '[+]MySQL in your help !!'

	except:
		print '[*]you have an error in your connection'
		print '[*]make sure to verify parameters and try again'
		sys.exit()

	return (MyConnection, Cursor)

def main():
	pass


if __name__ == '__main__':
	main()
