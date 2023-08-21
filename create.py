#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

f = cgi.FieldStorage()
img = f.getvalue('i')
cname = f.getvalue('n')
cmd = "sudo docker run -itd --name {} {}".format(cname,img)
op = subprocess.getoutput(cmd)
print(op)