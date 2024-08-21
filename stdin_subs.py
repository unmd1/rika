import sys
import recon
import dict
rc = recon.recon(prjID="5")
all_subs = rc.mysql_show("SELECT `address` FROM `subs`")
allio = dict.dic_to_list(all_subs,"address")
for line in sys.stdin:
    
    line = line.replace("http://","").replace("https://","").replace("www.","").replace("/","").strip()
    if not line in allio:
        rc.insert_subs(line,rc.prjname,line+"duplicator","new","justFind","rika","duplicator",rc.prjname)