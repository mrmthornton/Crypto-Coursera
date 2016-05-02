# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2015

@author: mike
'''

import sys

if __name__ == '__main__':
    print sys.version_info

    s = "41"
    print "Length of string is {}".format(len(s))
    print "String {}".format(s)
    print "String as hex {}".format(s.encode('hex'))
    print "String as Ascii {}".format(s.decode('hex'))
    print "Sting as int {}".format(int(s))
    print "Sting as binary {:b}".format(int(s))

   
