import recon
prjID = "1"
rc = recon.recon(prjID=prjID)
query = "SELECT `address` FROM `subs` WHERE `prj` = '" + rc.prjname +r"' and `result` LIKE '%forbidden%'"
urls = rc.mysql_show(query)
for url in urls:
    rc.forbidden_solve(url["address"])