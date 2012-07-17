from datetime import datetime, timedelta
from Crypto.Util import number, _number_new
from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

# a ** k mod m
def power_mod(a, k, m):
    reduced = a % m
    r = 1
    exponent = k
    while exponent > 0:
        if (exponent % 2 == 1):
            r = r * reduced
            r = r % m

        exponent = exponent / 2
        r = (r * r) % m

    return r

def validate(p, q, g):
    p_length = p.bit_length()

    if (p_length % 64) != 0:
        print "p's bit length not a mulitple of 64"
        return False

    if not (p_length >= 512 and p_length <= 1024):
        print "p's bit length is not between 512 and 1024"
        return False

    if not number.isPrime(p):
        print "p not prime"
        return False

    try:
        _number_new.exact_div(p - 1, q)
    except ValueError:
        print "q is not a prime factor of p"
        return False

    # g = u^{(p-1)/q}

    u = power_mod(g, 1 / _number_new.exact_div(p - 1, q), p)
    print u

    if not (u > 0 and u < p):
        print "g is invalid"
        return False
        
    return True

def generate_cert(identity, data): 
    if len(identity) > 10:
        raise ValueError('Identity too long')

    expiry = datetime.utcnow() + timedelta(days=365)
    data_field = identity + str(data) + expiry.strftime('%d-%m-%y')

    return data_field

def sign_cert(cert, ca_pk, g, p, q, ca_sk):
    key = DSA.construct((ca_pk, g, p, q, ca_sk))
    hash = SHA.new(cert).digest()
    k = random.StrongRandom().randint(1, key.q - 1)
    signature = key.sign(hash, k)

    if key.verify(hash, signature):
        print "OK"
    else:
        print "Failed"

    return signature

def verify_cert(cert, r, s, ca_pk, g, p ,q):
    key = DSA.construct((ca_pk, g, p, q))
    hash = SHA.new(cert).digest()
    
    return key.verify(hash, (r, s))
