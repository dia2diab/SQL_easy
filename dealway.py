#! /usr/bin/env python

#This script is a part of SQL_easy
#written by DiaaDiab

from settings import *
import os
import readline


class Dealing(object):

    def __init__(self, MyConnection, Cursor):

        self.MyConnection = MyConnection
        self.Cursor = Cursor

    def Change_db(self, db_name):
        MySQL_Query = 'use %s' % db_name
        try:
            self.Cursor.execute(MySQL_Query)
            print '[*]You have Changed DataBase.'
        except:
            print '[--]SyStem Error !!'

    def View_all(self, TableName, db_name):
        global UserName
        global PassWord

        statement = 'mysql -u%s -p%s --execute="use %s;select * from %s;"' % (UserName,
                PassWord, db_name, TableName)
        try:
            print '[*]All Record in your Table.'
            os.system(statement)
        except:
            print '[--]SyStem Error !!'

    def Update(self, TableName):
        numFields = self.Cursor.execute('show columns from %s' % TableName)
        fields = []
        for i in range(numFields.bit_length()):
            fields.append(self.Cursor.fetchone()[0])
        fields_tuple = tuple(fields)
        choice = int(raw_input('[-]You have {0} choose by number to edit field: '.format(fields_tuple)))
        if choice in range(1, len(fields) + 1):
            field_update = fields[choice - 1]
            fieldName = raw_input('[+]Enter %s that you want update: ' % field_update)
            fieldName = '\'' + fieldName + '\''
            ch = int(raw_input('[+]Enter field that you want to update it from {0}: '.format(fields_tuple)))
            field_up = fields[ch - 1]
            qu = raw_input('[+]Enter %s that you want update: ' % field_up)
            qu = '\'' + qu + '\''
            try:
                MySQL_Query = "update %s set %s=%s where %s=%s" % (TableName,
                        field_up, qu, field_update, fieldName)
                self.Cursor.execute(MySQL_Query)
                self.MyConnection.commit()
                print '[*]Already Update.'
            except:
                print '[--]You have SQL error !!'
        else:
            print '[--]SyStem Error !!'
            print '[**]Your Entered is wrong !!'

    def Add(self, TableName):
        numFields = self.Cursor.execute('show columns from %s' % TableName)
        fields = []
        for i in range(numFields.bit_length() + 2):
            fields.append(self.Cursor.fetchone()[0])
        data = {}
        data_tuple = ()
        for field in fields:
            if field != 'Id':
                data[field] = raw_input('[*]Enter {0}: '.format(field))
                data_tuple += (data[field], )
        fields.remove('Id')
        fields = tuple(fields)
        try:
            MySQL_Query = "insert into %s %s values %s" % (TableName, fields, data_tuple)
            print MySQL_Query
            exit()
            self.Cursor.execute(MySQL_Query)
            self.MyConnection.commit()
            print '[*]Addition Done.'
        except:
            print '[--]You have SQL error !!'

    def Delete(self, TableName):
        numFields = self.Cursor.execute('show columns from %s' % TableName)
        fields = []
        for i in range(numFields.bit_length()):
            fields.append(self.Cursor.fetchone()[0])
        fields_tuple = tuple(fields)
        choice = int(raw_input('[-]You have {0} choose by number: '.format(fields_tuple)))
        if choice in range(1, len(fields) + 1):
            field_deleted = fields[choice - 1]
            fieldName = raw_input('[+]Enter %s that you want to delete: ' % field_deleted)
            fieldName = '\'' + fieldName + '\''
            try:
                MySQL_Query = "delete from %s where %s=%s" % (TableName, field_deleted, fieldName)
                self.Cursor.execute(MySQL_Query)
                self.MyConnection.commit()
                print '[*]Deleting Done.'
            except:
                print '[--]You have SQL error !!'
        else:
            print '[--]SyStem Error !!'
            print '[**]Your Entered is wrong !!'

    def View(self, TableName, db_name):
        global UserName
        global PassWord

        numFields = self.Cursor.execute('show columns from %s' % TableName)
        fields = []
        for i in range(numFields.bit_length()):
            fields.append(self.Cursor.fetchone()[0])
        fields_tuple = tuple(fields)
        choice = int(raw_input('[-]You have {0} choose by number: '.format(fields_tuple)))
        if choice in range(1, len(fields) + 1):
            field_deleted = fields[choice - 1]
            fieldName = raw_input('[+]Enter %s that you want to Show: ' % field_deleted)
            fieldName = '\'' + fieldName + '\''
            try:
                statement = 'mysql -u%s -p%s --execute="use %s;select * from %s where %s=%s;"' % (UserName,
                        PassWord, db_name, TableName, field_deleted, fieldName)
                print '[*]Your Record: '
                os.system(statement)
            except:
                print '[--]SyStem Error !!'
        else:
            print '[--]SyStem Error !!'
            print '[**]Your Entered is wrong !!'

    def Dump(self, db_name):
        global UserName
        global PassWord

        statement = 'mysqldump -u%s -p%s %s > dump/%s.sql' % (UserName, PassWord, db_name, db_name)
        try:
            os.system(statement)
            print '[*]You have Dump File name.sql in dump directory.'

        except:
            print '[--]SyStem Error !!'


def main():
    pass


if __name__ == '__main__':
    main()
