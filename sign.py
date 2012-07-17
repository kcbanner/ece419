#!/usr/bin/env python2

import sys
from crypto import validate, generate_cert, sign_cert, verify_cert
import params

p = params.p
q = params.q
g = params.g
ca_pk = params.ca_pk
ca_sk = params.ca_sk

print "Validating parameters:",
valid = validate(p, q, g)
if not valid:
    sys.exit(1)
else:
    print "OK"

print "Generating cert: OK"
cert = generate_cert('kcbanner', 'test')

print "Signing cert:",
r, s = sign_cert(cert, ca_pk, g, p, q, ca_sk)

print "\nCertifcate: %s" % cert
print "r: %s" % r
print "s: %s" % s

print "Verifying cert:",

verified = verify_cert(cert, r, s, ca_pk, g, p, q)
if verified:
    print "OK"
else:
    print "Fail"    
