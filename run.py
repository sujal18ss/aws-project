#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

f=cgi.FieldStorage()
cmd=f.getvalue("x")
o=subprocess.getoutput("sudo "+cmd)
print(o)