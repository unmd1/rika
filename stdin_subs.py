import sys
import recon
for line in sys.stdin:
    rc = recon.recon(prjID="1")
    rc.insert_subs(line,rc.prjname,line+"duplicator","new","justFind","rika","duplicator",rc.prjname)