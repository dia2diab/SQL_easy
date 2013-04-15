#! /usr/bin/env python

#This script is a part of SQL_easy
#written by DiaaDiab

from settings import *
import os
from dealway import *
import readline


class Structure(object):

    def __init__(self, MyConnection, Cursor):

        self.MyConnection = MyConnection
        self.Cursor = Cursor

    def Show_dbs(self):
        global UserName
        global PassWord
        print '[*]All DataBases:'
        statement = 'mysql -u%s -p%s --execute="SHOW DATABASES;"' % (UserName, PassWord)
        try:
            os.system(statement)
        except:
            print '[--]SyStem Error !!'

    def Create_db(self, db_name):
        MySQL_Query = 'create database %s' % db_name
        try:
            self.Cursor.execute(MySQL_Query)
            print '[*]Your DataBase has been Created:'
        except:
            print '[--]You have SQL error !!'

    def Show_tables(self, db_name):
        statement = 'mysql -u%s -p%s --execute="use %s; show tables;"' % (UserName, PassWord, db_name)
        try:
            os.system(statement)
            print '[*]DataBase Tables: '
        except:
            print '[--]SyStem Error !!'

    def Create_table(self, t_name):
        print '[!!]please never make id, it will make automatic by programme.'
        number_Of_fields = int(raw_input('How man field you want to make in your table!!: '))
        print '[+]Enter your fields following by press enter button after every field.'
        MySQL_Query = '(Id INT PRIMARY KEY AUTO_INCREMENT'
        cons = 0

        for i in range(number_Of_fields):
            fieled_name = raw_input('>>')

            if cons == number_Of_fields - 1:
                MySQL_Query += ', %s TEXT(200))' % fieled_name
            else:
                MySQL_Query += ', %s TEXT(200)' % fieled_name

            cons += 1

        Ct = 'create table %s' % t_name
        MySQL_Query = Ct + ' ' + MySQL_Query
        try:
            self.Cursor.execute(MySQL_Query)
            print '[*]Table has been Created.'
        except:
            print '[--]You have SQL error !!'

    def Drop_db(self, db_name):
        MySQL_Query = 'drop database %s' % db_name
        try:
            self.Cursor.execute(MySQL_Query)
            print '[*]Your DataBase has been Droped.'
        except:
            print '[--]You have SQL error !!'

    def Drop_table(self, t_name):
        MySQL_Query = 'drop table %s' % t_name
        try:
            self.Cursor.execute(MySQL_Query)
            print '[*]Your Table has been Created:'
        except:
            print '[--]You have SQL error !!'

    def SQL_Shell(self):
        command = 'mysql -u%s -p%s' % (UserName, PassWord)
        try:
            os.system(command)
        except:
            print '[--]SyStem Error !!'


def main():
    pass
if __name__ == '__main__':
    main()
