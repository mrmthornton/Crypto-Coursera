# -*- coding: utf-8 -*-
'''
Created on Jan 24, 2014

@author: mike
'''

def strxor(a, b):     # xor two strings of different lengths
    '''
    Returns a string, the bitwise xor of the input strings, and of length equal
    to the shorter input string.

    @param a,b: strings of arbitrary length
    '''
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

def encrypt(k, m):
    '''
    A wrapper for debug. Eases examination of individual results.
    @param k, m: The key, k, and the message, m.
    '''
    c = strxor(k, m)
    #print c.encode('hex') # this is helpfull for debug
    return c

def random(size=16):
    '''
    @param size: the number of bits returned
    '''
    return open("/dev/urandom").read(size)


if __name__ == '__main__':

    MSGS = ( "a", "ab", "abc", "abcdefghijklmn")
    stringKey = ""
    stringKey = "".join('\0' for i in range(11))
    key = random(1024)

    print MSGS

    # encrypt the message using the generated key
    ciphertexts = [encrypt(key, msg) for msg in MSGS]
    print
    print "[non ascii]"

    # decrypt the message, with the same key
    result = [encrypt(key, cipher) for cipher in ciphertexts]
    print
    print result
