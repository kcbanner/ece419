#!/usr/bin/env python2

import sys
from optparse import OptionParser
from crypto import generate_cert

if __name__ == '__main__':
    usage = "usage: %prog identity public_key p q g"    
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()

    if len(args) < 2:
        parser.print_usage()
        sys.exit(1)
        
    public_key = int(args[1])
    p = int(args[2])
    q = int(args[3])
    g = int(args[4])

    ca_sk = 432398415306986194693973996870836079581453988813
    ca_pk = 49336018324808093534733548840411752485726058527829630668967480568854756416567496216294919051910148686186622706869702321664465094703247368646506821015290302480990450130280616929226917246255147063292301724297680683401258636182185599124131170077548450754294083728885075516985144944984920010138492897272069257160

    generate_cert(args[0], public_key, p, q, g, ca_sk, ca_pk)
