#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

f = cgi.FieldStorage()
cname = f.getvalue('n')
cmd = "sudo docker rm -f {}".format(cname)
op = subprocess.getoutput(cmd)
print(op)
