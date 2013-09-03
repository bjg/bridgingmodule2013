'''
Created on 3 Sep 2013

@author: brian
'''
import sys
import os

def f2c(t):
    return (t - 32) * 5/9

def c2f(t):
    return t * 9/5 + 32

progname = os.path.basename(sys.argv[0])
if len(sys.argv) < 3:
    raise ValueError(progname + ": Expecting flag and temperature list")
flag = sys.argv[1]
temperatures = [float(x) for x in sys.argv[2:]]
if flag == "f2c":
    print [f2c(t) for t in temperatures]
elif flag == "c2f":
    print [c2f(t) for t in temperatures]
else:
    raise ValueError(progname + ": Invalid flag %s" % flag)