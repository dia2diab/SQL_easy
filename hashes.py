#! /usr/bin/env python

#This script is a part of SQL_easy
#written by DiaaDiab


def Encrypt(algo, text):
    '''(algo, text) > hashes'''

    if algo == 'base64':
        return text.encode('base64')

    if algo == 'asciiHex':
        return text.encode('hex')


def Decrypt(algo, hashed):
    '''(algo, hashed) > text'''

    if algo == 'base64':
        return hashed.decode('base64')

    if algo == 'asciiHex':
        return hashed.decode('hex')


def Hashing(data):
    '''(data) > hashed'''
    hashed = Encrypt('base64', data)
    hashed = Encrypt('asciiHex', hashed)
    return hashed


def Cracking(hash):
    '''(hashed) > data'''
    data = Decrypt('asciiHex', hash)
    data = Decrypt('base64', data)
    return data


def Sulting(data):
    '''(data) > sulted'''
    sult = '5a476c685953426b615746690a'
    sulted = data[0] + sult + data[1:]
    return sulted


def Rm_sulting(hashed):
    '''(hashed) > data'''
    data = hashed[0] + hashed[27:]
    return data


def _to_db(data):
    return Sulting(Hashing(data))


def _from_db(data):
    return Cracking(Rm_sulting(data))


def main():
    pass

if __name__ == '__main__':
    main()
