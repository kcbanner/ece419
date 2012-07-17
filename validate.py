#!/usr/bin/env python2

import sys
from optparse import OptionParser

def validate(p, q, g):
    p_length = p.bit_length()

    if (p_length % 64) != 0:
        print "p's bit length not a mulitple of 64"
        return False

    if not (p_length >= 512 and p_length <= 1024):
        print "p's bit length is not between 512 and 1024"
        return False

    # TODO: Make sure p is prime

    quotient, remainder = divmod(p - 1, q)

    if remainder != 0:
        print "q is not a prime factor of p"
        return False

    # g = u^{(p-1)/q}
    
    u = g ** (1/float(quotient))

    if not (u > 0 and u < p):
        print "g is invalid"
        return False
        
    return True

if __name__ == '__main__':
    #usage = "usage: %prog p q g"    
    #parser = OptionParser(usage=usage)
    #(options, args) = parser.parse_args()

    #if len(args) < 3:
    #    parser.print_usage()
    #    sys.exit(1)

    #p = int(args[0])
    #q = int(args[1])
    #g = int(args[2])

    p = 168199388701209853920129085113302407023173962717160229197318545484823101018386724351964316301278642143567435810448472465887143222934545154943005714265124445244247988777471773193847131514083030740407543233616696550197643519458134465700691569680905568000063025830089599260400096259430726498683087138415465107499
    q = 959452661475451209325433595634941112150003865821
    g = 94389192776327398589845326980349814526433869093412782345430946059206568804005181600855825906142967271872548375877738949875812540433223444968461350789461385043775029963900638123183435133537262152973355498432995364505138912569755859623649866375135353179362670798771770711847430626954864269888988371113567502852

    result = validate(p, q, g)

    print result
