# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2015

@author: mike
'''

import sys

if __name__ == '__main__':
    print sys.version_info

    s = "41"
    print "Length of string is %d" % len(s)
    print "String %s " % s
    print "String as hex %s" %s.encode('hex')
    print "String as Ascii %s " % s.decode('hex')
    print "Sting as int %d " % int(s)
    print "Sting as binary %b " % int(s)

    msg = "315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e"
    print msg.decode('hex')
