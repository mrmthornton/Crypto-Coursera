'''
Created on Jan 24, 2014

@author: mike
'''


MSGS = ( "a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
len(MSGS)

#xor two strings of different lengths
def strxor(a, b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(k, m):
    c = strxor(k, m)
    print c.encode('hex')
    return c

if __name__ == "__main__":
    key = random(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]
    print ciphertexts
