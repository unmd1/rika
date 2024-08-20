import recon
import dict
rc=recon.recon(prjID="4")
dups = rc.mysql_show("SELECT `address` FROM `subs` WHERE `created_by` = 'duplicator'")
test = rc.mysql_show("SELECT `address` FROM `subs` WHERE `comment` = 'test'")
adresses= dict.dic_to_list(test,"address")
for dup in dups:
    dupio = dup["address"].replace("https://","").replace("http://","").replace("www.","").replace("\\n","").replace("\n","")
    if not dupio in adresses:
        print(dupio)



