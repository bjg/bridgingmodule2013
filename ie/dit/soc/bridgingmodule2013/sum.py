'''
Created on 3 Sep 2013

@author: brian
'''
def sum(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]
    else:
        return L[0] + sum(L[1:])
    
print sum([1, 2, 3, 4, 5])