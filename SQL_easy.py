#! /usr/bin/env python

#This script is a part of SQL_easy
#written by DiaaDiab

from dealway import Dealing
from settings import *
from structure import Structure
#from hashes import Encrypt, Decrypt, Info
import readline

class SQL_easy(object):

	def MySQL_Screen(self):
		print 
                print '-----------------------------------------'
		print '[01]Show DataBases On Server. '
		print '[02]Create New DataBase. '
		print '[03]Show Tables In DataBase. '
		print '[04]Create New Table. '
		print '[05]Delete DataBase From Server. '
		print '[06]Delete Table From DataBase. '
		print '[07]Take MySQL Shell. '
		print '[08]Show All Records In Table. '
		print '[09]Add Record To Table. '
		print '[10]Update Record In Table. '
		print '[11]View Specific Record From Table. '
		print '[12]Take Dump From DataBase. '
		print '[00]Quit. '
                print '-----------------------------------------'
		print '***********Choose By Number***********'

        def repeat(self):
            ch = raw_input('[**](Q)uite, else Continue: ')
            ch = ch.lower()
            if ch == 'q':
                sys.exit()
            else:
                self.MySQL_Screen()

                

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
	    showing.MySQL_Screen()
	while True: 
		ch = raw_input('[**]Choice:')
		if ch == '1':
                    struc.Show_dbs()
                    showing.repeat()
		if ch == '2':
                    databaseName = raw_input('[*]Enter Your New DataBase Name: ')
		    struc.Create_db(databaseName)
                    showing.repeat()
		if ch == '3':
		    databaseName = raw_input('[*]Enter DataBase That You Want To Show Tables In It: ')
		    struc.Show_tables(databaseName)
                    showing.repeat()
		if ch == '4':
		    databaseName = raw_input('[*]Enter Which DataBase Name To Create Table In It: ')
		    deal.Change_db(databaseName)
		    tableName = raw_input('[*]Enter Your New Table Name: ')
		    struc.Create_table(tableName)
                    showing.repeat()
		if ch == '5':
                    databaseName = raw_input('[*]Enter DataBase Name That You Want To Drop It Down: ')
		    struc.Drop_db(databaseName)
                    showing.repeat()
		if ch == '6':
                    databaseName = raw_input('[*]Enter DataBase Name That You Want TO Drop Table from It: ')
		    deal.Change_db(databaseName)
		    tableName = raw_input('[*]Enter Table Name That You Want To Drop It: ')
		    struc.Drop_table(tableName)
                    showing.repeat()
		if ch == '7':
                    struc.SQL_Shell()
		    showing.MySQL_Screen()
                    showing.repeat()
		if ch == '8':
                    databaseName = raw_input('[*]Enter DataBase Name That You Want To Deal With It: ')
                    tableName = raw_input('[*]Enter Table Name That You Want To Deal With It: ')
                    deal.View_all(tableName, databaseName)
                    showing.repeat()
		if ch == '9':
                    databaseName = raw_input('[*]Enter DataBase Name That You Want To Deal With It: ')
                    deal.Change_db(databaseName)
                    tableName = raw_input('[*]Enter Table Name That You Want To Deal With It: ')
                    deal.Add(tableName)
                    showing.repeat()
                if ch == '10':
                    databaseName = raw_input('[*]Enter DataBase Name That You Want To Deal With It: ')
                    deal.Change_db(databaseName)
                    tableName = raw_input('[*]Enter Table Name That You Want To Deal With It: ')
                    deal.Update(tableName)
                    showing.repeat()
                if ch == '11':
                    databaseName = raw_input('[*]Enter DataBase Name That You Want To Deal With It: ')
                    deal.Change_db(databaseName)
                    tableName = raw_input('[*]Enter Table Name That You Want To Deal With It: ')
                    deal.View(tableName, databaseName)
                    showing.repeat()
                if ch == '12':
                    databaseName = raw_input('[*]Enter DataBase Name That You Want To Take Dump From It: ')
                    deal.Dump(databaseName)
                    showing.repeat()
                if ch == '0':
                    print '[**]bye'
                    sys.exit()
        

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 
        print '[-]Bye'
        sys.exit()
