# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2015

@author: mike
'''

import sys
import string


s = str("0x1000")
print "The length of string myString %d" % len(s)
hexNum = string.atoi(s, 0)
print "The number in base 16 is %x " %hexNum


if __name__ == '__main__':
    print sys.version_info
