import os,commands

f1=open("sites","r+")

a=f1.readlines()
print a

for b in a:
  print b
  os.chdir("/home/root_EB/ansible/.hostlist/host_vars/")
  c=open(b,"w")
  c.write("app_server:")
  c.close()
