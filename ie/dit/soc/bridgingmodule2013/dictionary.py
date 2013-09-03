'''
Created on 3 Sep 2013

@author: brian
'''
dict = {'a': 1, 'b': 2, 'c': 3, 'd': "a string", 'e': 1}

dict['f'] = 'some other string'
dict['j'] = [1, 2, 4, 5, 6]
dict['k'] = {"A": 10, "B": 20}

del dict['b']
print "Deleted ", dict.pop('d', None)
    
for k, v in dict.iteritems():
    print k, v

