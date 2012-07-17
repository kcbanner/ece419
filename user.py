#!/usr/bin/env python2

import sys
import zmq
from optparse import OptionParser

if __name__ == '__main__':
    usage = "usage: %prog <identity> <ca address> <data file>"
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()

    if len(args) < 3:
        parser.print_help()
        sys.exit(1)
    
    identity = args[0]
    if len(identity) > 10:
        print "Identity must be a maximum of 10 characters"
        sys.exit(1)

    data_file = open(args[2], 'r')

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://' + args[1])

    message = "%s:%s" % (identity, )




    


