from node import Room
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import pylab
import operator
from monster import Monster

new_dict = {}

def check(N, K, p, k):
    lst = []
    for i in xrange(N - K):
        lst.append(p)
    for i in xrange(K):
        lst.append(k)

    # If negative integer is present or sum is not even
    if min(lst) < 0 or (sum(lst) % 2 == 1):
        return False

    while (len(lst) > 0):

        lst.sort(reverse=True)
        x = lst.pop(0)

        if x == 0:
            return True
        if x < 0  or x > len(lst):
            return False

        for i in xrange(x):
            lst[i] -= 1

    return False

def generate_pre_dictonary(lst):
    for el in lst:
        new_dict.update({el: []})

def pl(lst):
    print("[ "),
    for el in lst:
        print(unicode(el.hasMoved) + " "),
    print (" ]\n")
m1 = Monster(1)
m2 = Monster(2)

r1 = Room(1)
r2 = Room(2)

lst1 = []
lst2 = []

lst1.append(m2)
lst2.append(m2)

print "Before: \n"

pl(lst1)
pl(lst2)

m2.hasMoved = True

print "After: \n"

pl(lst1)
pl(lst2)