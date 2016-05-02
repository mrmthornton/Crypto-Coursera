'''
Created on Aug 5, 2015

@author: mike
'''
import sys

MSGS = ("This is a secret message to test the encryption code for the first homework.",
        "This is a secret message") # 25 char

def strxor(a, b):     # xor two strings of different lengths
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])
    #if len(a) > len(b):
    #    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    #else:
    #    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def random(size=16):
    return open("/dev/urandom").read(size)


def encrypt(key, msg):
    c = strxor(key, msg)
    print c.encode('hex')
    return c

if __name__ == '__main__':

    key = random(1024)
    #key = "                         "
    #key = "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"
    
    print MSGS
    ciphertexts = [encrypt(key, msg) for msg in MSGS]
    for msg in ciphertexts:
        print msg.encode('hex'),
    print
    
    '''    
    print MSGS2
    ciphertexts2 = encrypt(key, MSGS2)
    for msg in ciphertexts2:
        print msg.encode('hex'),
    print
'''
    #msgXor = encrypt(ciphertexts, ciphertexts2)
    #print msgXor.encode('ascii')