import os
import datetime

filename1 = datetime.datetime.now().strftime("Dev_Test_%d_%m_%Y-%H_%M_%S_info.txt")

print filename1

os.chdir('/home/root_EB/results')
f1=open(filename1,'w')
f1.write("HI There!")
f1.close()
