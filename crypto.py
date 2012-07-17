from datetime import datetime, timedelta
import hashlib
import random

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

def generate_cert(identity, public_key, p, q, g, ca_sk, ca_pk):   
    if public_key.bit_length() != 1024:
        raise ValueError('Private key not 1024 bits')

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
