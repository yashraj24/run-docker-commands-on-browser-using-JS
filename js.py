#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

#this will take value from user(will type on the url itself) and print it
f = cgi.FieldStorage()
cmd = f.getvalue("x")
#print(cmd)

o = subprocess.getoutput("sudo " + cmd)
print(o)


