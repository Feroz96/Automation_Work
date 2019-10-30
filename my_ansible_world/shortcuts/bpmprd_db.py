import os

os.system("ansible-playbook ../dc-check/bpm_prd_.yml -i ../.hostlist/bpm_prod --tags df1,df2 --limit bpmprod_db")


