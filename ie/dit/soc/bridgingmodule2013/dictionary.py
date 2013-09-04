'''
Created on 3 Sep 2013

@author: brian
'''
aDictionary = {'a': 1, 'b': 2, 'c': 3, 'd': "a string", 'e': 1}

aDictionary['f'] = 'some other string'
aDictionary['j'] = [1, 2, 4, 5, 6]
aDictionary['k'] = {"A": 10, "B": 20}

del aDictionary['b']
print "Deleted ", aDictionary.pop('d', None)
    
for k, v in aDictionary.iteritems():
    print k, v

