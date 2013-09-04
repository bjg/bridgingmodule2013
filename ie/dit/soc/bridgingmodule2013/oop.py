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
    
    def someMethod(self):
        self.someAttr = "A String"
    
    @staticmethod
    def count():
        return Person.peopleCount
    
p1 = Person('Larry')
p2 = Person('Moe')
p2.anotherAttr = "Another string"
p3 = Person('Curley')
p3.someMethod()

print p1.count()
print p2.anotherAttr
print p3.someAttr

class SuperHero(Person):
    def __init__(self):
        super(SuperHero, self).__init__('Superman')
        
hero = SuperHero()
print SuperHero.count()

print hero.peopleCount

