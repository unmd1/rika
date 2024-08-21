import recon
import json
prjID = "5"
rc = recon.recon(prjID=prjID)
query = "SELECT `result` FROM `subs` WHERE `prj` = '" + rc.prjname +r"' and `result` LIKE '%forbidden%'"
urls=[]
urls_d = rc.mysql_show(query)
for url in urls_d:
    url_d_l = json.loads(url["result"])["url"]
    if not url_d_l in urls:
        urls.append(url_d_l)
for url in urls:
    rc.forbidden_solve(url)