from datetime import datetime, timedelta
import hashlib
import M2Crypto
import random

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

def int2mpi(p):
    bn = M2Crypto.m2.hex_to_bn("%x" % p)
    mpi = M2Crypto.m2.bn_to_mpi(bn)
    return mpi

def generate_cert(identity, public_key, p, q, g, ca_sk, ca_pk): 
    if len(identity) > 10:
        raise ValueError('Identity too long')

    expiry = datetime.utcnow() + timedelta(days=365)
    data_field = identity + str(public_key) + expiry.strftime('%d-%m-%y')

    #k = random.randint(1, q - 1)
    k = 791602866227620675999682610123926798725884311007

    # r = g ** k mod q
    r = power_mod(g, k, q)

    hash = hashlib.sha1()
    hash.update(data_field)
    digest = int(hash.hexdigest(), 16)

    # h(m) = xr + ks (mod q)
    # get k^-1 mod q    

    k_inv = power_mod(k, q - 2, q)
    s = ((digest - (ca_sk * r)) / k_inv) % q

    print r, s
