#!/usr/bin/env python2

import sys
from optparse import OptionParser
from crypto import generate_cert



if __name__ == '__main__':
    usage = "usage: %prog identity"    
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()

    if len(args) < 2:
        parser.print_usage()
        sys.exit(1)
        
    identity = args[0]
    
