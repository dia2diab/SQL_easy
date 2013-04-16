#! /usr/bin/env python

#This script is a part of SQL_easy
#written by DiaaDiab

from dealway import Dealing
from settings import *
from structure import Structure
#from hashes import Encrypt, Decrypt, Info
import readline


class SQL_easy(object):

    def MySQL_Screen_1(self):
        print
        print '-----------------------------------------'
        print '[01]Show DataBases On Server. '
        print '[02]Create New DataBase. '
        print '[03]Delete DataBase From Server. '
        print '[04]Use One Of DataBase.'
        print '[05]Take MySQL Shell. '
        print '[06]Take Dump From DataBase. '
        print '[00]Quit. '
        print '-----------------------------------------'
        print '***********Choose By Number***********'

    def MySQL_Screen_2(self):
        print '-----------------------------------------'
        print '[01]Show Tables In DataBase. '
        print '[02]Create New Table. '
        print '[03]Show All Records In Table. '
        print '[04]Add Record To Table. '
        print '[05]Update Record In Table. '
        print '[06]View Specific Record From Table. '
        print '[07]Delete Table From DataBase. '
        print '[08]Exit Current DataBase. '
        print '[00]Quit. '
        print '-----------------------------------------'
        print '***********Choose By Number***********'

    def repeat_1(self):
        ch = raw_input('[**](Q)uite, else Continue: ')
        ch = ch.lower()
        if ch == 'q':
            sys.exit()
        else:
            self.MySQL_Screen_1()

    def repeat_2(self):
        ch = raw_input('[**](Q)uite, else Continue: ')
        ch = ch.lower()
        if ch == 'q':
            sys.exit()
        else:
            self.MySQL_Screen_2()

def main():
    print '''
     #####   #####  #
    #     # #     # #               ######   ##    ####  #   #
    #       #     # #               #       #  #  #       # #
     #####  #     # #               #####  #    #  ####    #
          # #   # # #               #      ######      #   #
     #    # #    #  #               #      #    # #    #   #
     #####   #### # #######         ###### #    #  ####    #
                            #######
    '''
    # initialize programme
    MyConnection, Cursor = InitConnection()
    # structure instance
    struc = Structure(MyConnection, Cursor)
    # dealway instance
    deal = Dealing(MyConnection, Cursor)
    if MyConnection != None and Cursor != None:
        # display screen for user
        showing = SQL_easy()
        showing.MySQL_Screen_1()
    while True:
        ch = raw_input('[**]Choice:')

        if ch == '1':
            struc.Show_dbs()
            showing.repeat_1()

        if ch == '2':
            databaseName = raw_input('[*]Enter Your New DataBase Name: ')
            struc.Create_db(databaseName)
            showing.repeat_1()

        if ch == '3':
            databaseName = raw_input('[*]Enter DataBase Name That You Want To Drop It Down: ')
            struc.Drop_db(databaseName)
            showing.repeat_1()

        if ch == '4':
            databaseName = raw_input('[*]Enter DataBase Name That You Want To Use It: ')
            deal.Change_db(databaseName)
            showing.MySQL_Screen_2()
            while True:
                ch = raw_input('[**] Choice: ')

                if ch == '1':
                    struc.Show_tables(databaseName)
                    showing.repeat_2()

                if ch == '2':
                    tableName = raw_input('[*]Enter Your New Table Name: ')
                    struc.Create_table(tableName)
                    showing.repeat_2()
                if ch == '3':
                    tableName = raw_input('[*]Enter Table Name That You Want To Deal With It: ')
                    deal.View_all(tableName, databaseName)
                    showing.repeat_2()
                if ch == '4':
                    tableName = raw_input('[*]Enter Table Name That You Want To Deal With It: ')
                    deal.Add(tableName)
                    showing.repeat_2()
                if ch == '5':
                    tableName = raw_input('[*]Enter Table Name That You Want To Deal With It: ')
                    deal.Update(tableName)
                    showing.repeat_2()

                if ch == '6':
                    tableName = raw_input('[*]Enter Table Name That You Want To Deal With It: ')
                    deal.View(tableName, databaseName)
                    showing.repeat_2()
                if ch == '7':
                    tableName = raw_input('[*]Enter Table Name That You Want To Drop It: ')
                    struc.Drop_table(tableName)
                    showing.repeat_2()
                if ch == '8':
                    showing.MySQL_Screen_1()
                    break
                if ch == '0':
                    print '[**]bye'
                    sys.exit()

        if ch == '5':
            struc.SQL_Shell()
            showing.MySQL_Screen_1()

        if ch == '6':
            databaseName = raw_input('[*]Enter DataBase Name That You Want To Take Dump From It: ')
            deal.Dump(databaseName)
            showing.repeat_1()

        if ch == '0':
            print '[**]bye'
            sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print
        print '[-] Bye'
        sys.exit()
