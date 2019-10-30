import os
import crypt

print "Hi, Please enter a plain text to encrypt"
pswd=raw_input("Enter Plain text to encrypt: ")
\
print "Press 1 for SHA-512 method\nPress 2 for SHA-256 method\nPress 3 for MD5 method"

choice=raw_input("Choose Encryption in above list: ")

if choice=="1":
   a=crypt.crypt("$pswd", "$5$sha-512")

elif choice=="2":
   a=crypt.crypt("$pswd", "$5$sha-256")

elif choice=="3":
   a=crypt.crypt("$pswd", "$5$MD5")

print "\n*******************PLEASE COPY BELOW ENCRYPTED TEXT***************\n"
print "**** ",a," ****"
print "\n*******************PLEASE COPY ABOVE ENCRYPTED TEXT***************\n"
