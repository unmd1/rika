import recon
import dict
rc=recon.recon(prjID="1")
subs = rc.mysql_show("SELECT `address` from `subs`")
dik = dict.dic_to_list(subs,"address")
final_subs = {}
values=[]
values_ = []
outputs=[]

for sub in subs:
    sub_org = sub["address"].replace("www.","")

    if "." in sub_org and len(sub_org.split("."))>3:

        sp_subs = sub_org.split(".")

        for i in range(0,len(sp_subs)-2):

            temp_sub = sub_org.split(".")

            value= [temp_sub[i],"subdomain_duplicate.py",rc.prjname,"","","","","","subdomain_duplicate",rc.prjname]
            if not value in values:
                values.append(value)


            temp_sub[i]="*"
            final = ".".join(temp_sub)


            if not final in final_subs:
                final_subs.update({final:1})
            else:
                final_subs[final]+=1



# rc.mysql_insert_to_many(rc.value_wordlist(),values,"wordlist")
for final_sub in final_subs:
    if final_subs[final_sub] > 3 :
        for values_2 in values:
            outputs.append(final_sub.replace("*",values_2[0]))
outputs = set(outputs) - set(dik)
for output in outputs:
    print(output)