import os
import datetime
import commands

q1=raw_input("Do you want check all sites(Y/n)?")

if q1.lower() == "n":
 sname=raw_input("Please enter site name to check: ")
 sn=sname.lower()
 os.system("ansible-playbook ../dc-check/dev_n_test_check.yml -i ../.hostlist/dev_test --limit "+sn+"")
else:
 print "Please wait.. this may take some time"
 output=commands.getoutput("ansible-playbook ../dc-check/dev_n_test_check.yml -i ../.hostlist/dev_test")
 print "*********************************************************"
 choice=raw_input("\nPress 1 for onscreen output..\nPress 2 for textfile output..\n")
 if choice == "1":
  print output
 elif choice =="2":
  os.chdir("/home/root_EB/results/")
  file_in=datetime.datetime.now().strftime("DevTest_%d_%m_%Y_%H_%M_%S_Info.txt")
  file_op=open(file_in,'w+') 
  file_op.write(output)
  file_op.close()
  print "Output file has been saved under /home/root_EB/results directory with today's timestamp."
