'''
Created on 3 Sep 2013

@author: brian
'''

class Person(object):
    peopleCount = 0
    
    def __init__(self, name):
        self.name = name
        Person.peopleCount += 1
        
    def __str__(self):
        return self.name
    
    @staticmethod
    def count():
        return Person.peopleCount
    
p1 = Person('Larry')
p2 = Person('Moe')
p3 = Person('Curley')

print p1.count()

class SuperHero(Person):
    def __init__(self):
        super(SuperHero, self).__init__('Superman')
        
hero = SuperHero()
print SuperHero.count()

print hero.peopleCount

