'''
Created on 3 Sep 2013

@author: brian
'''

try:
    n = 1 / 0
except ZeroDivisionError as e:
    print e
    