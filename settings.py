#! /usr/bin/env python

#This script is a part of SQL_easy
#written by DiaaDiab

import sys
import readline
from subprocess import Popen
from platform import platform as OS

try:
    import MySQLdb
except:
    print '[*]Install Module <MySQL> for python.'
    sys.exit()

HostName = None   # remove None and set your host of MySQL server
UserName = None   # remove None and set user of MySQL server
PassWord = None   # remove None and set password of MySQL server


def InitConnection():
    '''set things to connect to MySQL'''
    global HostName
    global UserName
    global PassWord

    if None in (HostName, UserName, PassWord):
        print '[*] you must verify variables in settings.py to allow'
        print '[*] programme to connect to MySQL>Line number (15, 16, 17)'
        # fire up a text editor
        choice = raw_input("\n[+] Should I fire up a text ediror for you (y/n)? ")
        if choice == 'y':
            if 'linux' in OS().lower():
                    Popen('vi settings.py', shell=True).wait()
            elif 'windows' in OS().lower():
                Popen('notepad settings.py', shell=True).wait()
            else:
                msg = "[+] Could not detect the running OS "
                msg += 'please, edit settings.py manually'
                exit(msg)
        else:
            print "[+] Thanks for using SQL Easy"
            sys.exit()

    try:
        MyConnection = MySQLdb.connect(
                host=HostName,
                user=UserName,
                passwd=PassWord
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
