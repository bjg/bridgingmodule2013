'''
Created on 3 Sep 2013

@author: brian
'''
input = [1, 2, 4, '5']

def isInt(arg):
    if not type(arg) is int:
        raise ValueError(arg + " is not an int!")
    
[isInt(x) for x in input]