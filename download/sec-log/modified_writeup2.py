#! /usr/bin/env python
''' Multiplicative attack on fixed pattern padding RSA - SHA2017 Crypto 2
    Chosen plaintext attack to selectively forge signature:
    The server asks for an RSA signature of string begin with
    'ticket:admin|root|'

    let t be an random string starts with that token, and construct 3 numbers
    such that:
        t * 0xff__...__ == 0xff__...__ * 0xff__...__ mod n
            ^^^^^^^^^^^    ^^^^^^^^^^^   ^^^^^^^^^^^
                  a             b               i
    then 
        (t**d) * (a**d) == (b**d) * (i**d) mod n
            ^
      private_key

    then We can calculate the signature:
        (t**d) == (b**d) * (i**d) * invert((a**d), n)
        ^^^^^^
      signature

    To find a, b, i whose most significant byte are 0xff, I generated some
    random `i0 = i / a` (don't compute i0 this way, read on) starts with 0xff and brute force b until its most
    significant byte is also 0xff.
        b = t / i0
    if b starts with 0xff, then we are done.

    We can choose a as long as a begins with nine `1`s (so that i = a * i0 begins
    with 0xff).

    With a, b, i chosen, we can now forge the signature.
'''

import random
import string
import gmpy2
import socket
from pdb import set_trace

n = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385618630224045260938256521594051014100163503337502422415671183189322191205776067978479547419392319431496088564871089271483778027246774457788805555615297270366146466252347288451288375751247197329959735437170802389801569971064368598028871180778637354490929426176883740658057736936793507039520194977558948892181985349

# Translate a number to a string (byte array), for example 5678 = 0x162e = \x16\x2e
def num2str(n):
    d = ('%x' % n)
    if len(d) % 2 == 1:
        d = '0' + d
    return d.decode('hex')
# Translate byte array back to number \x16\x2e = 0x162e = 5678
def str2num(s):
    return int(s.encode('hex'),16)

ticket = 'ticket:admin|root|'
t = str2num(ticket)
# t = str2num(ticket+''.join(random.choice(string.ascii_lowercase) \
 #                           for _ in range(20)))

def randb():
    ''' Generate random b with most significant byte 0xff
    '''
    while True:
        len = random.randint(0, 511)
        if len % 2 == 1:
            len += 1
            yield int('ff'+''.join(random.choice('0123456789abcdef') for
                                _ in range(len)), 16)

def run(t, n):
    ''' Brute force i0 such that its most significant byte is 0xff.
        To get `i` whose most significant byte is 0xff, this function computes 
        `i0`, which is multiplied with `a`, which begins with 9 `1`s
    '''
    print "[*] Brute force begins..."
    for i0 in randb():
        b = gmpy2.invert(i0, n) * t % n
        if (b.bit_length() & 7) == 0 and hex(b)[2:4] == 'ff':
            return b, i0


def get_signature(s, x):
    s.sendall('3')
    s.recv(1024)
    if hex(x)[-1] == 'L':
        s.sendall(hex(x)[4:-1])
    else:
        s.sendall(hex(x)[4:])
    s.recv(1024)
    return int(str(s.recv(1024).strip().split('\n')[0]), 16)


def get_flag(s, sigt):
    s.sendall('2')
    s.recv(1024)
    s.sendall(hex(sigt)[2:-1])
    s.recv(1024)
    return s.recv(1024).strip()


if __name__ == '__main__':
    print "t = %s" % num2str(t)
    print("t = 0x%x" % t)
    b, i = run(t, n)
    # a = 0xffffffL # choose an arbitrary a
    # i = i0 * a % n

    assert hex(b)[2:4] == 'ff'
    assert hex(i)[2:4] == 'ff'
    # assert hex(a)[2:4] == 'ff'
    assert b * i % n == t % n
    print "b = 0x%x" % b
    print "i = 0x%x" % i
    # print "a = 0x%x" % a
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(('secure-login.stillhackinganyway.nl', 12345))
    s.connect(('localhost', 12345))
    s.recv(1024)
    sigb = get_signature(s, b)
    print "sigb = 0x%x" % sigb
    sigi = get_signature(s, i)
    print "sigi = 0x%x" % sigi
    # siga = get_signature(s, a)
    # print "siga = 0x%x" % siga

    sigt = (sigb * sigi % n)
    # sigt = ((sigb * sigi % n) * gmpy2.invert(siga, n)) % n
    print "sigt = 0x%x" % sigt
    print "------------=====FLAG=====-----------------"
    print get_flag(s, sigt) # flag{8f898e19de410591acbcdbfae798d603}
