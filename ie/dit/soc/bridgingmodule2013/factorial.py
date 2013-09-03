'''
Created on 3 Sep 2013

@author: brian
'''
def factI(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def factR(n):
    if n <= 1:
        return 1
    else:
        return n * factR(n - 1)

print [factI(n) for n in range(1, 10)]
print [factR(n) for n in range(1, 10)]