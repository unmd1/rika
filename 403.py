import recon
import json
prjID = "1"
rc = recon.recon(prjID=prjID)
query = "SELECT `result` FROM `subs` WHERE `prj` = '" + rc.prjname +r"' and `result` LIKE '%forbidden%'"
urls = rc.mysql_show(query)
for url in urls:
    url_org = json.loads(url["result"])["url"]
    rc.forbidden_solve(url_org)