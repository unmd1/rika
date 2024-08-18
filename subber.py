import recon
import sys
# import os
# import tldextract
# import re
# import requests




# def geturltxt(txt,domain):
#     URLs=[]
#     if domain in txt:
#         indexes = [ (i.start(), i.end()) for i in re.finditer(domain, txt)]
#         for index in indexes:
#             start=0
#             try:
#                 if start == 0 : start = txt[0:index[0]].rindex('"')+1
#             except:
#                 start = 0
#             end = index[1]
#             URLs.append(txt[start:end])
#     return URLs


# print(geturltxt('',''))
# src_directory = r"H:\HUNT\tikkie\httpx"
project_address = sys.argv[1]
rc = recon.recon(prjID="1")
for scope in rc.scopes:
    print(scope)
    rc.subfinder(scope)
    rc.crtsh(scope)

rc.run_command_json("python3 stdout.py SELECT_-address-_FROM_-subs-_WHERE_-prj-_=_!"+ rc.prjname +"! address | httpx -silent -j -irrb -srd " + project_address)
rc.run_command2("python3 subdomain_duplicate.py 0 0 1 | dnsx -silent | httpx -silent | python3 stdin_subs.py")


