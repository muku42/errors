#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys

def print_usage():
    """Print usage and exit"""
    sys.stderr.write("usage: python raise_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tzerodivision, overflow, attribute\n")
    sys.stderr.write("\tunbound, encode\n")
    sys.exit()

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
    assert 6*9 == 42 # nod to Hitchhiker's Guide to the Galaxy
    #raise AssertionError
elif error_type == "io":
    open('ministry_of_silly_walks.txt')
    #raise IOError
elif error_type == "import":
    from lumberjack import butteredscones
    #raise ImportError
elif error_type == "index":
    hhgg = [0,1,2,3,4,5]
    the_answer_to_life_the_universe_and_everything = hhgg[42]
    #raise IndexError
elif error_type == "key":
    monty = {"a" : 1, "b" : 2, "c" : 3}
    print(monty["python"])
    #raise KeyError
elif error_type == "name":
    qwerty = dvorak
    #raise NameError
elif error_type == "os":
    import os
    os.mkdir('slartibartfast')
    os.mkdir('slartibartfast')
    #raise OSError
elif error_type == "type":
    the_answer = 42
    to_life = str('forty-two')
    the_universe = the_answer + to_life
    #raise TypeError
elif error_type == "value":
    and_everything = int('eighty-eight')
    #raise ValueError
elif error_type == "zerodivision":
    zero_div = 42/0
    #raise ZeroDivisionError
elif error_type == "overflow":
    print (1e42**1e88)
elif error_type == "attribute":
    import math
    zaphod = math.prefect(42)
elif error_type == "unbound":
    counter = 0
    def increment():
        counter += 1
    increment()
elif error_type == "encode":
    u"\u0411".encode("iso-8859-15")
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()