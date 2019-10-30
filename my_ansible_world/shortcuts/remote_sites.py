import os
import commands
import datetime

def app_func():
 
 while True:

  q1=raw_input("Do you want check all sites at a time(Y/n)?")
 
  if (q1.lower() == "n") or (q1.lower() == "no"):

   sname=raw_input("Please enter site name to check: ")
 
   sn=sname.lower()

   os.system("ping "+sn+" -c 5") 

   os.system("ansible-playbook ../remote-site-check/all-app-disk-mem-up.yml -i ../.hostlist/sites --limit "+sn+" --ask-vault-pass ")
   #os.system("ansible-playbook ../remote-site-check/app-site.yml -i ../.hostlist/sites --limit "+sn+" ")
   #os.system("ansible-playbook ../remote-site-check/disk-info.yml -i ../.hostlist/sites --limit "+sn+" ")
   #os.system("ansible-playbook ../remote-site-check/mem-up-info.yml -i ../.hostlist/sites --limit "+sn+" ")

  elif (q1.lower()== "yes") or (q1.lower()== "y"):

     print "Please wait... This may take some time..."
  
     #output=commands.getoutput("ansible-playbook /home/root_EB/ansible/remote-site-check/all-app-disk-mem-up.yml -i /home/root_EB/ansible/.hostlist/sites")
     output=commands.getoutput("ansible-playbook /home/root_EB/ansible/remote-site-check/all-app-disk-mem-up.yml -i /home/root_EB/ansible/.hostlist/sites --ask-vault-pass")
     #output=commands.getoutput("ansible-playbook /home/root_EB/ansible/remote-site-check/mem-up-info.yml -i /home/root_EB/ansible/.hostlist/sites")

     print "********************************************************************************************************"

     choice=raw_input("\nPress 1 for onscreen output..\nPress 2 for textfile output..\n")

     if choice == "1":
  
       print output

     elif choice =="2":

      os.chdir("/home/root_EB/results/")

      file_in=datetime.datetime.now().strftime("all_remote_site_status_%d_%m_%Y_%H_%M_%S_Info.txt")

      file_op=open(file_in,'w+')

      file_op.write(output)

      file_op.close()

      print "Output file "+file_in+" has been saved under /home/root_EB/results directory with today's timestamp."
      
  else:
 
      print "\nInvalid input.. Program terminated..\n"
      
      print "Please try again... \n"
     
      break
  
  break

app_func()
 
 
