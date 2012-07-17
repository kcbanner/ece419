#!/usr/bin/env python2

from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

import params


key = DSA.construct((1L, 1L, 1L, 1L, 1L))
