#!/usr/bin/env python3

def hello_world():
    return "Hello, World!"


a = hello_world # without () at the end we do not call the function we only make a point to hello_world
print(a()) # this works and print "Hello, World!"
print(a) # This does not work (see the message  to understand)
