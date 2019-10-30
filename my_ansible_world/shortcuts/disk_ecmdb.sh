
ansible-playbook ../dc-check/ecm_prd_.yml -i ../.hostlist/ecm_prod --tags df1,df2 --limit ecmprod_db
